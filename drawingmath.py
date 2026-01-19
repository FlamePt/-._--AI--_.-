import math
from turtle import *

a = float(input("Qual o valor do lado a: "))
b = float(input("Qual o valor do lado b: "))
c = float(input("Qual o valor do lado c: "))


A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = 180 - A - B


speed(1)  


forward(a)  
left(A)  
forward(b) 
left(B) 
forward(c)  


done()

   



