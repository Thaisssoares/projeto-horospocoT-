#Apresentação
print('\n\n\t-- Projeto Horoscopo \n\n')

#Entrada
dia=int(input('digite o dia:'))
mes=int(input('digite o mes:'))

#Processamento e Saída
if mes == 12 and dia <= 22 or mes == 1 and dia >= 19 :
        print('Capricornio')
elif mes == 1 and dia <= 20 or mes == 2 and dia >= 18 :
        print('Aquario')
elif mes == 2 and dia <= 19 or mes == 3 and dia >=20 :
        print('Peixes')
elif mes == 3 and dia <= 21  or mes == 4 and dia >=19 :
        print('Aries')
elif mes == 4 and dia <= 20 or mes == 5 and dia >= 20:
        print('Touro')
elif mes == 5 and dia <= 21  or mes == 6 and dia >= 20:
        print('Gemeos')
elif mes == 6 and dia <= 22  or mes == 7 and dia >= 22:
        print('Cancer')
elif mes == 7 and dia <= 23  or mes == 8 and dia >=22:
        print('Leao')
elif mes == 8 and dia <= 23 or mes == 9 and dia >=22:
        print('Virgem')
elif mes == 9 and dia <= 23 or mes == 10 and  dia >= 21:
        print('Libra')
elif mes == 10 and  dia <= 23 or mes == 11 and dia >= 21:
        print('Escorpiao')
elif mes == 11 and dia <= 22 or mes == 12 and dia >=21:
        print('Sargitario')

else:
        print('mes invalido')

