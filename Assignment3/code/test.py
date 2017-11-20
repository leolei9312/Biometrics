import csv
test = [123,3,4,5,6,7]

with open('ConfidenceResult.csv', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    wr.writerow(test)
    test.append(1)
    wr.writerow(test)
