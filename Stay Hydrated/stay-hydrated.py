import time
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

INTERVAL = 1800  # 30 minutes in seconds
GIF_PATH = "water_meme.gif"

def show_reminder() -> None:
    root = tk.Tk()
    root.title("Stay Hydrated Reminder")

    gif = Image.open(GIF_PATH)
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

    label = tk.Label(root, image=frames[0])
    label.pack(padx=20, pady=20)

    text_label = tk.Label(root, text="Time to drink water!", font=("Arial", 14))
    text_label.pack(pady=(0, 20))

    root.update_idletasks()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def animate(frame_index=0) -> None:
        try:
            label.config(image=frames[frame_index])
        except tk.TclError:
            return
        next_frame = (frame_index + 1) % len(frames)
        label.after(50, animate, next_frame)

    animate()
    root.after(5000, root.destroy)
    root.mainloop()

print(f"Reminding you to drink water every {INTERVAL} seconds...")
print("Press Ctrl+C to stop.")

while True:
    time.sleep(INTERVAL)
    show_reminder()
