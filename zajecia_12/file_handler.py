import csv

class FileHandler:
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.transformations = transformations
        self.data = self.load_data()

    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file, delimiter=",")
            temp_matrix = []
            for row in reader:
                temp_row = []
                for element in row:
                    temp_row.append(float(element))
                temp_matrix.append(temp_row)
        return temp_matrix

    def save_data(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            operation = transformation_list[0]
            direction = transformation_list[1]
            index = int(transformation_list[2])
            value = float(transformation_list[3])
            # operation, direction, index, value = transformation_list
            if direction == "row":
                self.row_operations(index, value, operation)
            elif direction == "col":
                self.col_operations(index, value, operation)
            else:
                print("We don't have such an option")


    def row_operations(self, index, value, operation):
        for position, item in enumerate(self.data):
            if operation == "add":
                self.data[index][position] += value
            else:
                self.data[index][position] *= value


    def col_operations(self, index, value, operation):
        for row in self.data:
            if operation == "add":
                row[index] += value
            else:
                row[index] *= value

