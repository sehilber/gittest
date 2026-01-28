import tkinter as tk
import random

class AimTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aim Trainer")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.score = 0
        self.target_radius = 40
        self.target = None

        self.fehler = 0

        # TIMER FEATURE
        self.time_left = 30  # 30 Sekunden Spielzeit
        self.game_active = True

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 16))
        self.score_label.pack()

        self.fehler_label = tk.Label(root, text=f"fehler : {self.fehler}", font=("Helvetica", 16))
        self.fehler_label.pack()

        # Timer Label
        self.timer_label = tk.Label(root, text=f"Zeit: {self.time_left}", font=("Helvetica", 16))
        self.timer_label.pack()

        self.canvas.bind("<Button-1>", self.check_hit)
        self.canvas.bind("<Button-2>", self.check_fehler)

        self.move_target()
        self.update_timer()  # Startet Timer

    def move_target(self):
        if self.target:
            self.canvas.delete(self.target)

        x = random.randint(self.target_radius, 800 - self.target_radius)
        y = random.randint(self.target_radius, 600 - self.target_radius)
        self.target = self.canvas.create_oval(
            x - self.target_radius, y - self.target_radius,
            x + self.target_radius, y + self.target_radius,
            fill="orange"
        )

    def check_hit(self, event):
        if not self.game_active:
            return

        x, y = event.x, event.y
        target_coords = self.canvas.coords(self.target)
        target_x = (target_coords[0] + target_coords[2]) / 2
        target_y = (target_coords[1] + target_coords[3]) / 2

        distance = ((x - target_x)**2 + (y - target_y)**2)**0.5

        if distance <= self.target_radius:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_target()

    def check_fehler(self, event):
        if not self.game_active:
            return

        x, y = event.x, event.y
        target_coords = self.canvas.coords(self.target)
        target_x = (target_coords[0] + target_coords[2]) / 2
        target_y = (target_coords[1] + target_coords[3]) / 2

        distance = ((x - target_x)**2 + (y - target_y)**2)**0.5

        if distance >= self.target_radius:
            self.fehler += 1
            self.fehler_label.config(text=f"fehler: {self.fehler}")

    # Timer-Funktion
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Zeit: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.game_active = False
            self.timer_label.config(text="Zeit vorbei!")
            self.canvas.delete(self.target)


if __name__ == "__main__":
    root = tk.Tk()
    app = AimTrainer(root)
    root.mainloop()
