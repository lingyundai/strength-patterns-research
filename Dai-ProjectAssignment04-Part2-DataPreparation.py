#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:13:09 2023

@author: lingyundai
"""

# import needed libraries
import pandas as pd
import matplotlib.pyplot as plt

# read dataset from aws s3 bucket
powerlifting_data = pd.read_csv("https://ait580.s3.amazonaws.com/Dai-ProjectAssignment04.csv")


# perform some basic explorations on dataset

# print out the first 10 rows
print(powerlifting_data.head(10))
# print out the last 10 rows
print(powerlifting_data.tail(10))


# see data types and check if there is any missing data

# the result shows that squat, bench, deadlift columns have
# missing data. The missing values are intentional, since 
# some people attend meet to do deadlift only, squat only, bench only,
# or push-pull (bench-deadlift) only. They should NOT be "handled"
# as they are missing by the design of the powerlifting meet, another reason
# being that total and dots are based on lifters recorded lifts, filling in the
# missing values here will make total and dots columns useless. 
print(powerlifting_data.info())
# see dataset numerical data descriptive statistics 
print(powerlifting_data.describe())

# perform some basic summarizations and explorations on
# columns that we will use to answer research questions --
# 1. do female powerlifters that have high deadlift records also have high squat records?
# 2. do female powerlifters with high body weight also achieve high total record in deadlift, bench, and squat?
# 3. what age range has the strongest bench records among female powerlifters?

# squat - RATIO
squat_stats = powerlifting_data.groupby('Squat').describe()
print("Squat: ", squat_stats)
# use histogram to see the distribution of the squat records
plt.figure()
plt.hist(powerlifting_data.Squat, edgecolor='black')
plt.xlabel("Squat (kg)")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Squat Records")
plt.savefig("Squat-Records-Histogram-plot.png")
# plt.show()

# deadlift - RATIO
deadlift_stats = powerlifting_data.groupby('Deadlift').describe()
print("Deadlift: ", deadlift_stats)
# use histogram to see the distribution of the deadlift records
plt.figure()
plt.hist(powerlifting_data.Deadlift, edgecolor='black')
plt.xlabel("Deadlift (kg)")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Deadlift Records")
plt.savefig("Deadlift-Records-Histogram-plot.png")
# plt.show()

# weight - RATIO
weight_stats = powerlifting_data.groupby('Weight').describe()
print("Weight: ", weight_stats)
# use histogram to see the distribution of the lifter body weights
plt.figure()
plt.hist(powerlifting_data.Weight, edgecolor='black')
plt.xlabel("Body Weight (kg)")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Body Weights")
plt.savefig("Body-Weight-Histogram-plot.png")
# plt.show()

# total - RATIO
total_stats = powerlifting_data.groupby('Total').describe()
print("Total: ", total_stats)
# use histogram to see the distribution of the total weight lifted
plt.figure()
plt.hist(powerlifting_data.Total, edgecolor='black')
plt.xlabel("Total Weight Lifted (kg)")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Total Records")
plt.savefig("Total-Records-Histogram-plot.png")
# plt.show()

# dots - RATIO
dots_stats = powerlifting_data.groupby('Dots').describe()
print("Dots: ", dots_stats)
# use histogram to see the distribution of the dots 
# dots is lifter weight lifted to lifter body weight ratio
plt.figure()
plt.hist(powerlifting_data.Dots, edgecolor='black')
plt.xlabel("Weight Lifted to Body Weight Ratio")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Dots Records")
plt.savefig("Dots-Records-Histogram-plot.png")
# plt.show()

# age - RATIO
age_stats = powerlifting_data.groupby('Age').describe()
print("Age: ", age_stats)
# use histogram to see the distribution of the age
plt.figure()
plt.hist(powerlifting_data.Age, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Age")
plt.savefig("Lifter-Age-Histogram-plot.png")
# plt.show()

# bench - RATIO
bench_stats = powerlifting_data.groupby('Bench').describe()
print("Bench: ", bench_stats)
# use histogram to see the distribution of the age
plt.figure()
plt.hist(powerlifting_data.Bench, edgecolor='black')
plt.xlabel("Bench (kg)")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Bench Records")
plt.savefig("Bench-Records-Histogram-plot.png")
# plt.show()

# extract month for date column
compete_month = pd.DatetimeIndex(powerlifting_data['Date']).month
# compete month - ORDINAL
# use histogram to see the distribution of the month
plt.figure()
plt.hist(compete_month, edgecolor='black')
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Distribution of Compete Month")
plt.savefig("Compete-Month-Histogram-plot.png")
# plt.show()

# Equip - NOMINAL
# equip means the gear/equipment the competitor is allowed to use.
# wraps means gears are allowed including knee wraps,
# raw means no gear used.
# use histogram to see the distribution of the equip
plt.figure()
plt.hist(powerlifting_data.Equip, edgecolor='black')
plt.xlabel("Equipment Division")
plt.ylabel("Count")
plt.title("2023 USPC Female Powerlifters: Equipment Division")
plt.savefig("Equip-Histogram-plot.png")
plt.show()

# export cleaned dataset to a csv file
powerlifting_data.to_csv("Dai-ProjectAssignment04-Cleaned.csv", index=False)

