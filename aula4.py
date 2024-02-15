#Tipos int e float
#int -> Número inteiro - sem ponto e sem virgula(virgula em programacao separa argumentos)
#tipo int representa qualquer numero -> positivo e negativo. Int sem sinal é considerado positivo
print(11)
print(-11)
print(0)

#Float -> Numero com ponto flutuante - #####
#float representa qualquer numero -> positivo ou negativo com ponto flutuante(virgula ou ponto - no python ponto)
#float sem sinal é considetado positivo
print(1.1)
print(1.0,1.1,1.2) #a virgula separou os numeros 1.0 1.1 e 1.2
print(0.0,-1.5)

#A funcao type mostra o tipo que o Python inferiu ao valor
#type - uma classe que pode ser executada como funcao
print( type('Isabella') ) # resposta do console -><class 'str'>
#print( type(1,1,'Isabella') ) # resposta do console ->error  = jeito errado de ver multiplos tipos de dados
print( type(1.1), type(-1.2),type('isabella')) # resposta console-> jeito certo de ver multipos dados ->  <class 'float'> <class 'float'> <class 'str'>
