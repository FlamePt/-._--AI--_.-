import matplotlib.pyplot as plt


marcas = ['Lexus', 'Mercedes', 'Toyota', 'Opel', 'BMW']


vendas = []


for marca in marcas:
    venda = int(input(f"Insira o número de vendas para {marca}: "))
    vendas.append(venda)


plt.stem(marcas, vendas)


plt.grid(True)


plt.title('Vendas Anuais de Automóveis')
plt.xlabel('Marcas de Automóveis')
plt.ylabel('Vendas Anuais')


plt.show()
