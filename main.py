import os
import glob
import pandas as pd

import merge_EQ_files
import plot_info
import calculations
import time


def main():
    raw_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/01_raw"
    combined_path = "/Users/khangvo/Python_Projects/Location_Excersises/files/02_reformated"

    merge_EQ_files.main(raw_path, combined_path)
    # plot_info.main(combined_path)
    calculations.main(combined_path)


if __name__ == "__main__":
    # timer start
    time_start = time.perf_counter()

    main()

    # timer end
    time_end = time.perf_counter()
    time_total = time_end - time_start
    print("Elapsed time: " + str(time_total) + " seconds")
