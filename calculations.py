import os
import numpy as np
import pandas as pd


def calc_eps():

    eps1 = []
    x1 = []
    y1 = []
    t1 = []

    eps2 = []
    x2 = []
    y2 = []
    t2 = []

    df = pd.read_csv("combined.txt", sep="\t")

    for i in range(0, 101, 1):
        for j in range(0, 101, 1):
            distance = np.sqrt((i - df["X"])**2 + (j - df["Y"])**2)

            time = distance/6

            residual1 = df["t1"] - time
            residual2 = df["t2"] - time

            avg_r1 = residual1.mean()
            avg_r2 = residual2.mean()

            squared_residual1 = (residual1 - avg_r1)**2
            squared_residual2 = (residual2 - avg_r2)**2

            final_residual1 = squared_residual1.sum()
            final_residual2 = squared_residual2.sum()

            eps1.append(final_residual1)
            x1.append(i)
            y1.append(j)
            t1.append(avg_r1)

            eps2.append(final_residual2)
            x2.append(i)
            y2.append(j)
            t2.append(avg_r2)

    # min_eps1 = min(eps1)
    # index_eps1 = eps1.index(min_eps1)
    # print(min_eps1)
    # print(x1[index_eps1])
    # print(y1[index_eps1])
    # print(t1[index_eps1])
    #
    # min_eps2 = min(eps2)
    # index_eps2 = eps2.index(min_eps2)
    # print(min_eps2)
    # print(x2[index_eps2])
    # print(y2[index_eps2])
    # print(t2[index_eps2])

    return min(eps1), min(eps2)


def calc_sigma_sqrt(eps1, eps2):
    df = pd.read_csv("combined.txt", sep="\t")

    for i in range(0, 101, 1):
        for j in range(0, 101, 1):
            distance = np.sqrt((i - df["X"]) ** 2 + (j - df["Y"]) ** 2)

            time = distance / 6

            residual1 = df["t1"] - time * eps1
            residual2 = df["t2"] - time * eps2

            avg_r1 = residual1.mean()
            avg_r2 = residual2.mean()

            squared_residual1 = (residual1 - avg_r1) ** 2
            squared_residual2 = (residual2 - avg_r2) ** 2

            final_residual1 = squared_residual1.sum()
            final_residual2 = squared_residual2.sum()

            return final_residual1 / 10, final_residual2 / 10


def calc_chi_sqrt(eps1, eps2, sigma1, sigma2):
    df = pd.read_csv("combined.txt", sep="\t")

    for i in range(0, 101, 1):
        for j in range(0, 101, 1):
            distance = np.sqrt((i - df["X"]) ** 2 + (j - df["Y"]) ** 2)

            time = distance / 6

            residual1 = df["t1"] - time * eps1
            residual2 = df["t2"] - time * eps2

            avg_r1 = residual1.mean()
            avg_r2 = residual2.mean()

            squared_residual1 = (residual1 - avg_r1) ** 2
            squared_residual2 = (residual2 - avg_r2) ** 2

            final_residual1 = squared_residual1.sum()
            final_residual2 = squared_residual2.sum()

            return final_residual1 / sigma1, final_residual2 / sigma2



def main(input_path):
    os.chdir(input_path)

    eps1, eps2 = calc_eps()

    sigma1, sigma2 = calc_sigma_sqrt(eps1, eps2)

    chi1, chi2 = calc_chi_sqrt(eps1, eps2, sigma1, sigma2)

    print(chi1)
    print(chi2)


if __name__ == "__main__":

    combined_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/02_reformated"
    main(combined_path)
