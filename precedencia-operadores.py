

conta_1 = 1 + 1 **5 + 5 # -> resultado = 7

#precedencia - ordem de execução 
#1- (n + n)- primeira coisa a ser executada é o que esta dendro dos parenteses(sao executados de dentro para fora - parenteses mais internos sao executados primeiro e depos segue para os exeternos)

#2 - ** - segunda coisa que é executada é a exponencição

#3 - *multiplicacao, divisao /, divisao de inteiros //, modulo % -> todos tem o mesmo peso, porem a ordem de execucao é da esquerda para direita

# 4 - adição +, subtração- -<> todos tem o mesmo peso, porem a ordem de execucao é da esquerda para direita

conta_1_certa = (1 + 1) ** (5 + 5)
print (conta_1_certa) #-->1024

#Precedencia - interpretador
#O interpretador Python le da esquerda para direita, de cima para baixo

var_1 = (1 + 10) ** (15 + 5)

var1 = "Qualquer coisa"

#-> a resposta do console sera "Qualquer coisa" -> pois, a ultima atualizacao da variavel foi "Qualquer coisa"

