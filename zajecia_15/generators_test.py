import os
import psutil
import csv

def get_processed_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)

def read_data_to_list(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        return [row for row in csv_reader]

def read_data_generator(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            yield row

print(f"Memory usage before reading file: {get_processed_memory_usage()} MB")
data = read_data_to_list("Electric_Vehicle_Population_Data.csv")
print(f"Memory usage after reading to list: {get_processed_memory_usage()} MB")

del data

print(f"Memory usage after cleanup: {get_processed_memory_usage()} MB")
data_generator = read_data_generator("Electric_Vehicle_Population_Data.csv")
for line in data_generator:
    pass
print(f"Memory usage after generator: {get_processed_memory_usage()} MB")