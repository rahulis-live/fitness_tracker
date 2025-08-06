import pandas as pd
import matplotlib.pyplot as plt

def show_workout_graph():
    df = pd.read_csv("workout.csv", header=0)
    
    counts = df["Workout"].value_counts()

    # Define labels and colors
    labels = ['Workout Done (Yes)', 'Workout Missed (No)']
    colors = ['#4CAF50', '#F44336']
    values = [counts.get('Yes', 0), counts.get('No', 0)]

    wedges, texts, autotexts = plt.pie(
        values,
        labels=['Yes', 'No'],
        colors=colors,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Workout Completion Ratio")
    plt.axis("equal")

    # Add custom legend (text box on side)
    plt.legend(
        wedges,
        labels,
        title="Workout Status",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    plt.tight_layout()
    plt.show()








# import pandas as pd
# from datetime import datetime
# import matplotlib.pyplot as plt

# def show_workout_graph():
#     df = pd.read_csv("workout.csv",header= 0)
    
#     counts = df["Workout"].value_counts()

#     plt.pie(counts,labels=counts.index,autopct="%1.1f%%", startangle=90)
#     plt.title("Workout Completion Ratio")
#     plt.axis("equal")
#     plt.show()