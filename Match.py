


def add(a1,a2):
    return a1 + a2

def mult(m1, m2):
    return m1 * m2 

n1 = float(input("Qual é o primeiro numero:"))
n2 = float(input("Qual é o segundo numero:"))
op = input("Digite a operação desejada (A/M): ")
if op == "A":
        resultado = add(n1, n2)
        print(f"O resultado da adição é: {resultado}")
elif op == "M":
        resultado = mult(n1, n2)
        print(f"O resultado da multiplicação é: {resultado}")
else:
        print("Opção Inválida")
