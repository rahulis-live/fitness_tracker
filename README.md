# 🏋️‍♂️ Fitness Tracker

A simple desktop application built with Python and Tkinter to help you track your daily weight and workout activity. Visualize your progress using graphs powered by Matplotlib and manage your health goals with ease.

---

## 📌 Features

- 📆 Log daily weight entries
- ✅ Record whether you did your workout or not
- 📈 Visualize weight trends over time (line chart)
- 🥧 View workout completion ratio (pie chart)
- 💾 Data stored in `.csv` files for easy access and editing
- 🖥️ User-friendly GUI using Tkinter

---

## 📁 Project Structure


fitness_tracker/
│
├── ui.py             # Main GUI window for tracking and visualization
├── weight.py         # Shows weight progress graph
├── workout.py        # Shows workout completion pie chart
├── weight.csv        # Stores date and weight (auto-created if not present)
├── workout.csv       # Stores date and workout status (Yes/No)
└── README.md         # Project documentation


## 🖼️ Screenshots

### Main UI Window
![Main UI](main_ui.png)

### Weight Progress Graph
![Weight Graph](weight_graph.png)

### Workout Completion Chart
![Workout Pie Chart](workout_chart.png)
