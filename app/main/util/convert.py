from datetime import datetime

# Convert string to date
def StrToDate(str):
    date = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    return date.date()
