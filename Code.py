import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

import pandas as pd
import numpy as np
import seaborn as sns

# Read the CSV file
DataSet = pd.read_csv('1.csv')

DataSet['class'] = DataSet['class'].map({'tested_positive': 1, 'tested_negative': 0})
DataSet.set_index(pd.RangeIndex(start=0, stop=len(DataSet)), inplace=True)
print(DataSet.describe())
# Calculate means for each column
def meansplot():
    means = DataSet.mean()

    fig, ax = plt.subplots()

    bars = plt.bar(means.index, means.values)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.xlabel('Columns')
    plt.ylabel('Mean Values')
    plt.title('Means of Columns')

    plt.savefig('mean')
    plt.clf()

def stdplot():
    std = DataSet.std()

    fig, ax = plt.subplots()

    bars = plt.bar(std.index, std.values)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.xlabel('Columns')
    plt.ylabel('Std Values')
    plt.title('Std of Columns')
    plt.savefig('Std')
    plt.clf()

def Medianplot():
    Median = DataSet.median()

    fig, ax = plt.subplots()

    bars = plt.bar(Median.index, Median.values)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.xlabel('Columns')
    plt.ylabel('Median Values')
    plt.title('Median of Columns')

    plt.savefig('Median')
    plt.clf()

def plotting(pltname):

    plt2.scatter(DataSet.index,DataSet[pltname])

    plt2.xlabel('Index')
    plt2.ylabel(pltname)
    plt2.title(f'Plot of {pltname}')
    plt2.savefig(f'scatter_of_{pltname}')
    plt.clf()


def pieplot(Cname):
    counts = DataSet[Cname].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)

    plt.title(f'Distribution of {Cname}')

    plt.savefig('piplot')
    plt.clf()


def heatmap():
    Matrix=DataSet.corr()
    plt.figure(figsize=(21, 21))
    sns.heatmap(Matrix, annot=True, cmap='Reds', linewidths=0.8, fmt='.3f')
    plt.title("Correlation Matrix Heatmap")
    plt.savefig('heatmap')
    plt.clf()

meansplot()
stdplot()
Medianplot()
heatmap()
pieplot('class')
Strings=['plas','age','preg','insu','mass','pedi','age','class']
for i in Strings:
    plotting(i)