import matplotlib.pyplot 
#Listas de valores a ser apresentados no grãfico 
matplotlib.pyplot.plot([ "Jan" , "Fev " , "Mar" , "Abr" , "Maio" , "Jun" , "Jul" , "Ago" , "Set", "Out" , "Nov" , "Dez" J,[9.03, 9.78, 12.37, 13.99, 16.78, 20.39, 22.54, 22.92, 20.48, 16.84, 12.28, 9.75], '-o' , color="purple " , 
linewidth=3) 
#Apresenta o titulo do grãfico 
matplotlib.pyplot.title( 'Temperatura Média 1991-2019(Portugal Continental-Font e IPMA) ' ) 
#Aprese nte o rótulo do eixo do y 
matplotlib.pyplot.ylabel( 'Temperatura (ºC)' ) 
#Aprese nta o rótulo do ei xo do x 
matplotlib.pyplot. xlabel ( 'Mês' ) 
#Apresenta a grelha do grãfico 
matplotlib.pyplot.grid () 
#Apresenta o grãfico numa janela 
matplotlib.pyplot.show ()