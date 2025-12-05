a = 0
b = 0

# Solicitar entrada dos números
a = int(input('Indique o primeiro número:\n'))

b = int(input('Indique o segundo número:\n'))


# Solicitar operação
op = str(input('Qual a operação desejada (adição, subtração, multiplicação, divisão, divisão inteira, módulo, exponenciação)?\n'))

# Operações
op_adicao = a + b
op_subtracao = a - b
op_multiplicacao = a * b
op_divisao = a / b 
op_divisao_int = a // b
op_modulo_div = a % b 
op_exponenciacao = a ** b


if op == "adição":
    print("Adição ->", a, "+", b, "=", op_adicao)
elif op == "subtração":
    print("Subtração ->", a, "-", b, "=", op_subtracao)
elif op == "multiplicação":
    print("Multiplicação ->", a, "X", b, "=", op_multiplicacao)
elif op == "divisão":
    print("Divisão ->", a, "/", b, "=", op_divisao)
elif op == "divisão inteira":
    print("Divisão inteira ->", a, "//", b, "=", op_divisao_int)
elif op == "módulo":
    print("Módulo ->", a, "%", b, "=", op_modulo_div)
elif op == "exponenciação":
    print("Exponenciação ->", a, "**", b, "=", op_exponenciacao)
else:
    print("Operação inválida! Tente novamente.")
