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

## ⚙️ Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter
- **Data Handling:** pandas
- **Data Visualization:** matplotlib
- **Storage:** CSV files
- 

## 📁 Project Structure

```bash
fitness_tracker/
├── ui.py          # Main GUI window for tracking and visualization
├── weight.py      # Shows weight progress graph
├── workout.py     # Shows workout completion pie chart
├── weight.csv     # Stores date and weight (auto-created if not present)
├── workout.csv    # Stores date and workout status (Yes/No)
└── README.md      # Project documentation
```


## 🖼️ Screenshots

### Main UI Window
![Main UI](main_ui.png)

### Weight Progress Graph
![Weight Graph](weight_graph.png)

### Workout Completion Chart
![Workout Pie Chart](workout_chart.png)

## 🖥️ Requirements

- **Python Version:** 3.x
- **Required Libraries:**
  
  pip install pandas matplotlib


## 🚀 How to Run

1.Clone the Repository
```bash
git clone https://github.com/rahulis-live/fitness_tracker.git
```
2.Install Required Libraries

Make sure Python 3.x is installed, then run:
```bash
pip install pandas matplotlib
```
3.Run the Application
```bash
python ui.py

```
## Author

Name: Rahul Chandran
LinkedIn: Rahul Chandran
