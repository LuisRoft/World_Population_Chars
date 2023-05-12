import csv

def read_csv(path):
    with open(path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            iter = zip(header, row)
            dict_data = dict(iter)
            # or:
            # dict_data = {key: value for key, value in iter}
            data.append(dict_data)
        return data

if __name__ == "__main__":
    path = "./data.csv"
    data = read_csv(path)
    print(data[0: 2])