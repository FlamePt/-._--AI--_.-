import matplotlib.pyplot as plt


nacoes = ['Portugal', 'Brasil', 'Alemanha', 'França', 'Bélgica']
pontuacoes = [10, 5, 7, 4, 9]

plt.bar(nacoes, pontuacoes, color='blue')  
plt.title('Campeonato do Mundo de Futebol')
plt.xlabel('Nações')
plt.ylabel('Pontuação')
plt.grid(axis='y') 
plt.show()
