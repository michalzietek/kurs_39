import csv
import os

def load_data(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            print(row)

def save_data(path):
    with open(path, mode="a") as file:
        writer = csv.writer(file)
        writer.writerow(["Zuza", "3", 18])


os.chdir("/home/michal/Documents")
save_data("example.csv")
load_data("example.csv")