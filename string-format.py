# como formatar string para que elas capturem variaveis

nome = 'luiz'
altura = 1.80
peso = 95

calculo_imc = peso / (altura ** altura) 
#print(nome, 'tem','' ,altura,'de altura','pesa',peso,'kg', 'e seu imc é : ',calculo_imc)

################################################################
#usando format string

#print('nome tem altura de altura') #-> nome tem altura de altura -> nao captura as variaveis - é uma string

#criando uma variavel que captura variaveis dentro de uma string

#linha_1 = f'{nome} tem {altura} de altura'

#print(linha_1)

#formatando casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura' #2f-> quantidade de casas decimais depois do ponto = 1.80

#print(linha_1)

#exemplo 2
linha_2 = f'pesa {peso} kg e seu imc é:  '

print(linha_2)

linha_3 = f'{calculo_imc:.2f}'#
print(linha_3)