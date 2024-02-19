#Funcao input - como coletar dados do usuario com funcao input

#input('Qual o seu nome? ') #Só exibe no terminal, não faz nada no codigo

#Coletando dados com a funcao input e variavel nome  -> o que o usuário digitar vai ficar gravado na variavel nome,  que tem tipo string
#nome = input('Qual o seu nome? ')

#print(f'O seu nome é {nome=}') #mostra qual o valor recebido, digitado pelo usuário


#numnero_1 = input('Digite um numero: ')
#numero_2 = input('Digite outro numero: ')

#print(f'A soma dos numeros é: {numnero_1 + numero_2}') #1 +5  -> o resultado mostrado pelo temrinal sera 15 - por conta da concatenação das variaveis do tipo string (numero_1 e numero_2) python. Para evitar o erro devemos fazer uma correção de tipo de str para int 

#O problema de corrigir utilizando int na raiz da variável é que se o usuário digitar alguma letra o programa quebra


#coerção de tipo str para int
numnero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite um numero: '))

print(f'A soma dos numeros é: {numnero_1 + numero_2}')


