import csv 

def main(file_path):
    with open(file_path,"r") as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            print(row)

main("data/records.csv")
main("data/users.csv")
