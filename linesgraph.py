import matplotlib.pyplot as plt


disciplinas = ['Português', 'Matemática', 'Tecnologias', 'Inglês']
notas = [15.4, 17.3, 18.1, 13.3]


plt.plot(disciplinas, notas, marker='o')


plt.grid(True)


plt.title('Notas Médias por Disciplina')
plt.xlabel('Disciplinas')
plt.ylabel('Notas')

plt.show()
