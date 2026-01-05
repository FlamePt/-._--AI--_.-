'''Exemplo da utilização das funções internas abs(x), ord(c), chr(i), bin(x), divmod(a,b), len(s), round(n, n_digits)'''
# Atribui à variável numeros uma lista de números inteiros
numeros = [1,3,5,7,8,6,10,56,23,4,14]

# Atribui à variável absoluto o resultado da função abs()
absoluto = abs(-4)

# Atribui à variável n_ordem o resultado da função ord()
n_ordem = ord('A')

# Atribui à variável caracter o resultado da função chr()
caracter = chr(64)

# Atribui à variável binario o resultado da função bin()
binario = bin(8)

# Atribui à variável quo_resto o resultado da função divmod(a,b) em que a corresponde ao dividendo e b ao divisor
quo_resto = divmod(23,5)

# Atribui à variável n_itens o resultado da função len()
n_itens = len(numeros)

# Atribui à variável num_arred o resultado da função round(n, n_digits)
num_arred = round(245.5690,1)

# Apresentação dos resultados atribuídos às variáveis
print("abs(-4) =", absoluto)
print("ord('A') =", n_ordem)
print("chr(64) =", caracter)
print("bin(8) =", binario)
print("divmod(23,5) =", quo_resto)
print("len(numeros) =", n_itens)
print("round(245.5690,1) =", num_arred)
