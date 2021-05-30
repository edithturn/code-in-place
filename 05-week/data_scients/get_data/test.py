import csv
with open('departments.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("ID Department Name")
    print("---------------------------------")
    #for row in data:
    #    print(row['department_id'], row['department_name'])

    count = 0
    for row in data:
        if count <= 5:
            print(row['department_id'], row['department_name'])
        else:
            break
        count += 1