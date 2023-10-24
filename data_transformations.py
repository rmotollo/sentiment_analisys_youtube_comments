import csv

def write_to_csv(headers, data, filename):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow([str(item) for item in row])

def transform_data(comments, sentiments):
    transformed_data = []
    for i in range(len(comments)):
        transformed_data.append([comments[i], sentiments[i][0], sentiments[i][1]])
    return transformed_data