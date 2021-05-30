import csv
with open('departments.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("ID Department Name")
    print("---------------------------------")
    
    # Example: Show all the date
    #for row in data:
    #    print(row['department_id'], row['department_name'])

    # Example: Show just top 5 
    #count = 0
    #for row in data:
    #    if count <= 5:
    #        print(row['department_id'], row['department_name'])
    #    else:
    #        break
    #    count += 1

    
    # Example: Priting just ONE column
    count = 0
    for row in data:
        if count <= 5:
            print(row['department_id'])
        else:
            break
        count += 1