# songzhihao
# 开发时间: 2023/9/11 18:10
import numpy as np
import pandas as pd
import glob
import csv
import os
import matplotlib.pyplot as plt

# Get a list of all CSV files in a directory
read_csv_files = glob.glob(r'D:\PythonPycharmProjections\pythontest\2-R2059-1800V-sample-*.csv')


# Create an empty list storing the full names of the CSV files in the current directory
# read_csv_files = []


# Get the name of the CSV file in the current directory
# def name():
#     # Read in the names of all files in the current directory
#     a = os.listdir(r'D:\AdataAve\decay\12.11-1＃')
#     for j in a:
#         # Determine if it is a CSV file, if so store it in the list
#         if os.path.splitext(j)[1] == '.csv':
#             read_csv_files.append(j)


# Loop through each CSV file and append its contents to the combined dataframe
def read_to_df(csv_files):
    # Create an empty dataframe to store the combined data
    x_collection = pd.DataFrame()
    y_collection = pd.DataFrame()
    y_normalization = pd.DataFrame()
    # dfX:read_x(Column 3); dfY:read_y(Column 4)
    for csv_file in csv_files:
        dfX = pd.read_csv(csv_file, usecols=[3], header=None)
        dfY = pd.read_csv(csv_file, usecols=[4], header=None)
        dfY = dfY * -1
        norm_Y = (dfY - dfY.min().iloc[0]) / (dfY.max().iloc[0] - dfY.min().iloc[0])
        x_collection = pd.concat([x_collection, dfX], axis=1, ignore_index=True)
        y_collection = pd.concat([y_collection, dfY], axis=1, ignore_index=True)
        y_normalization = pd.concat([y_normalization, norm_Y], axis=1, ignore_index=True)

    return x_collection, y_collection, y_normalization


x_result, y_result, y_norm = read_to_df(read_csv_files)

# mean
y_mean = pd.DataFrame(y_result.mean(axis=1))
# First normalise and then average
y_norm_mean = pd.DataFrame(y_norm.mean(axis=1))
# First average and then normalise
y_mean_norm = (y_mean - y_mean.min().iloc[0]) / (y_mean.max().iloc[0] - y_mean.min().iloc[0])

# result to csv
result = pd.concat([x_result.iloc[:, 0], y_mean, y_norm_mean, y_mean_norm], axis=1)
result.columns = ['x', 'y_mean', 'y_norm_mean', 'y_mean_norm']
# output result to .CSV file 
# Column 1: x; Column 2: average value of y;
# Column 3: First normalise and then average; Column 4:First average and then normalise
result.to_csv("./out_Result.csv", encoding='utf-8', index=True)

"""
for i in range(len(read_csv_files)):
    plt.plot(x_result.iloc[:, i], y_result.iloc[:, i], linewidth=0.5)

plt.show()

"""

"""
energy = np.empty(0)
for i in range(len(read_csv_files)):
    energy = np.append(energy, y_result.iloc[:, i].sum())
"""

"""
max_values = y_result.max(axis=0)

"""
