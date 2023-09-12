import csv

path = 'resources/budget_data.csv'

with open(path, 'r', newline='') as file:

    csv_reader = csv.reader(file)

    csvArray = list(csv_reader)

    row_count = len(csvArray)

    totalValue = 0

    totalChange = 0

    monthlyChange = 0

    checkForRepetitive = []

    greatestIncrease = {"month":"", "value":0}

    greatestDecrease = {"month":"", "value":0}

    for i in range(1, row_count):

        if i == 1:
            if not i in checkForRepetitive:  
            
                checkForRepetitive.append(csvArray[i][0])
                totalValue += int(csvArray[i][1])
       
        else:
          if not i in checkForRepetitive:  
            
                checkForRepetitive.append(csvArray[i][0])
                totalValue += int(csvArray[i][1])
                monthlyChange = int(csvArray[i][1]) - int(csvArray[i - 1][1])
                totalChange += int(csvArray[i][1]) - int(csvArray[i - 1][1])
                if greatestIncrease["value"] < monthlyChange:
                   greatestIncrease["value"] = monthlyChange
                   greatestIncrease["month"] = csvArray[i][0]

                if greatestDecrease["value"] > monthlyChange:
                   greatestDecrease["value"] = monthlyChange
                   greatestDecrease["month"] = csvArray[i][0]


    content = f"Financial Analysis\n\n----------------------------\n\nTotal Months: {len(checkForRepetitive)}\n\nTotal: ${totalValue}\n\nAverage Change: ${round(totalChange / (len(checkForRepetitive)-1), 2)}\n\nGreatest Increase in Profits: {greatestIncrease['month']} (${greatestIncrease['value']})\n\nGreatest Decrease in Profits: {greatestDecrease['month']} (${greatestDecrease['value']})"

    txt_path = "PyBank.txt"

    with open(txt_path, "w") as file:
        file.write(content)
