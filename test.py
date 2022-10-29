from datetime import datetime

date = datetime.strptime('02/04/1990', '%d/%m/%Y')
print(date)
print(date.strftime('%d')[1])

