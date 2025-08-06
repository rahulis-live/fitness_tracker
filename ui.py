import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import weight
import workout

def submit_entry():
    weight_val = entry_weight.get()
    workout_val = var_workout.get()

    try:
        w = float(weight_val)
    except ValueError:
        messagebox.showerror("Invalid Input", "Weight must be a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open("weight.csv", "a") as f:
        f.write(f"{date},{w}\n")

    with open("workout.csv", "a") as f:
        f.write(f"{date},{workout_val}\n")

    messagebox.showinfo("Saved", "Data saved successfully.")
    entry_weight.delete(0, tk.END)
    var_workout.set("Yes")

# GUI Layout
root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("350x350")

tk.Label(root, text="Daily Fitness Entry", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter your weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Workout today?").pack()
var_workout = tk.StringVar(value="Yes")
tk.Radiobutton(root, text="Yes", variable=var_workout, value="Yes").pack()
tk.Radiobutton(root, text="No", variable=var_workout, value="No").pack()

tk.Button(root, text="Submit Entry", command=submit_entry, bg="#4CAF50", fg="white").pack(pady=10)

# ✅ Use specific function calls now
tk.Button(root, text="Show Weight Progress", command=weight.show_weight_graph).pack(pady=5)
tk.Button(root, text="Show Workout Progress", command=workout.show_workout_graph).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
