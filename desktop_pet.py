import tkinter as tk
import time
import random
import os
print(os.getcwd())
Base_dir = os.path.dirname(os.path.abspath(__file__))


class Pet:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)
        self.window.configure(bg="black")
        self.window.attributes("-transparentcolor", "black")

        # loading images
        self.walk_right = [
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-0.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-1.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-2.png")),
        ]
        # idle blink gif frames (example)
        self.idle_frames = [
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-0.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-1.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-2.png")),
        ]
        self.img = self.walk_right[0]
        self.walk_left = [
    frame.subsample(-1, 1) for frame in self.walk_right
]
        self.width = self.img.width()
        self.height = self.img.height()

        #window label
        self.label = tk.Label(self.window, image=self.img, bg="black", bd=0)
        self.label.pack()

        #screen
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.ground_y = self.screen_height - self.height - 40

        #physics
        self.x = 100
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.gravity = 1.4

        #state of ai
        self.state = "idle"        # "idle" or "move"
        self.direction = 1         # 1 = right, -1 = left
        self.state_end_time = time.time() + random.uniform(2, 5)

        #timing
        self.last_update = time.time()
        self.walk_timer = time.time()
        self.idle_timer = time.time()
        self.frame_index = 0
        self.idle_index = 0

        self.update()
        self.window.mainloop()

    def update(self):
        now = time.time()
        dt = now - self.last_update
        self.last_update = now

        #state machine
        if now >= self.state_end_time:
            if self.state == "idle":
                self.state = "move"
                self.direction *= -1
                speed = random.uniform(0.8, 2)
                self.vx = speed * self.direction
                self.state_end_time = now + random.uniform(4, 9)

            else:
                self.state = "idle"
                self.vx = 0
                self.state_end_time = now + random.uniform(2, 5)

        #physics
        self.vy += self.gravity * dt * 60
        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60

        # ground
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vy = 0

        # screen edges
        if self.x <= 0:
            self.x = 0
            if self.vx < 0:
                self.vx *= -1

        elif self.x >= self.screen_width - self.width:
            self.x = self.screen_width - self.width
            if self.vx > 0:
                self.vx *= -1

        #animation
        if self.state == "idle":
            if now - self.idle_timer > random.uniform(0.3, 1.0):
                self.idle_timer = now
                self.idle_index = (self.idle_index + 1) % len(self.idle_frames)
                self.img = self.idle_frames[self.idle_index]
                self.label.configure(image=self.img)

        else:
            if now - self.walk_timer > 0.12:
                self.walk_timer = now
                self.frame_index = (self.frame_index + 1) % len(self.walk_right)
                if self.vx < 0:
                 self.img = self.walk_left[self.frame_index]
                else:
                 self.img = self.walk_right[self.frame_index]

                self.label.configure(image=self.img)

        #aplying position
        self.window.geometry(
            f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}"
        )
        self.window.after(16, self.update)

Pet()