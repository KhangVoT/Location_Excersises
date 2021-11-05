import os
import glob
import pandas as pd


def merge_df(input_path, output_path):
    os.chdir(input_path)
    file_list = sorted(glob.glob("*.txt"))

    dfs = dict()

    for file in file_list:
        if "_sorted" not in file:
            dfs[file] = pd.read_csv(file, header=None, delim_whitespace=True)

    df = pd.merge(dfs["Location_Exercise_1.txt"], dfs["Location_Exercise_2.txt"], on=[0, 1])
    df.to_csv(output_path + "/combined.txt", sep="\t", index=False, header=["X", "Y", "t1", "t2"])


def main(input_path, output_path):
    merge_df(input_path, output_path)


if __name__ == "__main__":
    raw_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/01_raw"
    combined_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/02_reformated"

    main(raw_path, combined_path)
