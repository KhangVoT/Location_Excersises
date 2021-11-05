import os
import pandas as pd
import matplotlib.pyplot as plt


def ploting(input_path):
    os.chdir(input_path)

    df = pd.read_csv("combined.txt", sep="\t")

    plt.scatter(df["X"], df["Y"])
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()


def main(input_path):
    ploting(input_path)


if __name__ == "__main__":
    combined_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/02_reformated"
    main(combined_path)
