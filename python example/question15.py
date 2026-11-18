import datetime

lineage = []

def track_data(source, operation, destination):
    record = {
        "source": source,
        "operation": operation,
        "destination": destination,
        "time": str(datetime.datetime.now())
    }

    lineage.append(record)

track_data("students.csv", "Remove duplicates", "cleaned.csv")

track_data("cleaned.csv", "Calculate marks", "results.csv")

for record in lineage:
    print(record)