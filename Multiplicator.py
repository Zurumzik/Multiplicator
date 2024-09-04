#Программа конвертации больших чисел
import math

variable = float(input("Введите число: "))
dict = {1:'тыс', 2:'млн', 3:'млрд', 4:'трлн'}

x = math.floor(variable)
if len(str(x)) > 3:
    n=(len(str(x))-1)//3
    i = n*3
    variable = str(round(variable/(10**i),2))+' '+dict[n]
    print(variable)

