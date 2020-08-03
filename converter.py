import csv, json

csvFilePath = "books.csv"
jsonFilePath = "books.json"

# reading csv and adding to dict
data = {}
with open(csvFilePath) as csv_file:
    csvReader = csv.DictReader(csv_file)
    for csvRow in csvReader:
        book_id = csvRow['bookID']
        data[book_id] = csvRow

# write to json file
with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))