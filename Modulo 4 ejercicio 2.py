from datetime import datetime
date = datetime(2022, 11, 7, 19, 5)
print(date.strftime("%A/%B/%Y %H:%M:%S "))
print(date.strftime("%d/%m/%Y %H:%M:%S %p "))
print(date.strftime("%a/%b/%g "))
print(date.strftime("%d, %Y %B "))
print(date.strftime("%d: %d "))
print(date.strftime("Dia : %j "))
print(date.strftime("Semana num: %U "))