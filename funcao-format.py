#Formatacao de nucleos dentro da funcao format
a = 'A'
b = 'B'
c = 1.1

#formato = ' ' #-> string vazia

#Método format  ->Ele é utilizado para agrupar um 
#conjunto de instruções relacionadas em um único bloco de código, 
#permitindo sua reutilização em diferentes partes do programa

################################################################
# Método Format
#pegando valor das variaveis a,b e c
    #formato = ''.format(a,b,c) #->o que esta dentro do parenteses é chamo de argumentos. a,b,c se tornam argumentos dentor de format

#Exibindo valor de a - utilizando indices - comecando por 0

#formato = 'a ={0} b={1}'.format(a,b,c)

#outra forma de acessar os argumentos de formato - criando uma variavel string e acessando os objetos de string pela variavel formato

#formatoando a string c -> duas casas decimais
#string = 'a ={0} b={1} c ={:.2f}'#->error cannot switch from manual field 
#specification to automatic field numbering - todos os campos tem que ter numeros e nao pode misturar numero com letra

#string = 'a ={0} b={1} c ={2:.2f} ' #formatoando a string c -> duas casas decimais -> campos sem nada e so o campo e formatacao com numero e letra



#Forma correta, criando quarto argumento na funcao format. 
#string = 'a ={} b={} c ={:.2f} {}'
#formato = string.format(a,b,c,'123456')
#print (formato)

#Acessando o mesmo valor diversas vezes - pelo index

#string = 'a ={0} a ={0} a ={0} a ={0} b={1} c ={:.2f} '
#formato = string.format(a,b,c,)
#print (formato)

#Parâmetro nomeado ->dar nome para chamada das funcoes
#A partir do primerio paramentro nomeado, tudo o que vier depois de um paramentro nomeado tambem precisa ser nomeado
#Ao cirar o paramentro nome1, a,b,c se tornam argumentos
string = 'a ={0} a ={0} a ={0} a ={0} b={1} c ={:.2f} '
formato = string.format(
    nome1=a,nome2=b, nome3=c,
)
print (formato)