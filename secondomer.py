import tkinter as tk
import time

def start_cronometru():
    global running, start_time
    running=True
    start_time = time.time() - elapsed_time
    update_cronometru()

def stop_cronometru():
    global running
    running =False

def reset_cronometru():
    global elapsed_time
    elapsed_time = 0
    cronometru_label.config(text="Cronometru 00:00:00.000")

def update_cronometru():
    if running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        ore, rem = divmod(elapsed_time , 3600)
        minute, secunde=divmod(rem, 60)
        secunde , milisecunde = divmod(secunde, 1)
        cronometru_label.config(text=f"Secondomer: {int(ore):02d}:{int(minute):02d}:{int(secunde):02d}.{int(milisecunde * 1000):03d}")
        cronometru_label.after(1, update_cronometru)

app =tk.Tk()
app.title("Secondamer")

cronometru_label = tk.Label(app, text="Secondamer: 00:00:00.000", font=("Helvetica", 24))
cronometru_label.pack()

button_frame = tk.Frame(app)
button_frame.pack()

start_button = tk.Button(button_frame, text="Start", command=start_cronometru)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(button_frame, text="Stop", command=stop_cronometru)
stop_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_cronometru)
reset_button.pack(side=tk.LEFT, padx=10)

running = False
elapsed_time = 0

app.mainloop()