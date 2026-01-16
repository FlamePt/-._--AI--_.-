from math import pi

r = float(input("Qual é o raio do círculo: "))

P = 2*pi*r
A = pi*r*r

if r > 0:
    print("O perimetro do circulo é", P)
    print("A area do circulo é", A)
else:
    print("Erro: A operação não pode ser concluida")