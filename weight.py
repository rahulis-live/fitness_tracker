# read  and write new weight from and to weight.csv file

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def show_weight_graph():
    df = pd.read_csv("weight.csv",header= 0)
   
    x =df["Date"]
    y =df["Weight"]

    plt.plot(x,y,c = 'blue',marker='o')
    plt.xlabel("Date")
    plt.ylabel("Weight")
    plt.title("Weight Progress Over Time")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()