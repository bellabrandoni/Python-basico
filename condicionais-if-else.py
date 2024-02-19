#Mudanca de fluxo em blocos de código python
#if / elif / else
#if - pode ficar sozinho, ter uma unica condicao e se essa condicao nao for sanada nao precisa do else
#elif depende do if- dependem um do outro
#elif - pode repetir várias vezes

#else depende só do if depende - pode haver if e else
#se/ se não se/ se 

#Somente um desses blocos sera executado dependendo da condicao

entrada = input('Voce que entrar ou sair? ')

if entrada == 'entrar':
    print('Voce entrou no sistema   ') ##condicao verdadeira
elif entrada == 'sair':
    print('Voce saiu do sistema')
else: 
        print('Voce nao digitou nem entrar e nem sair')
#######################################


##entendo o fluxo do interpretador em condicionais
#if sozinho
condicao = True

if condicao:
    print('Este é o código do if')

print('fora do if')

########## if e else
# nao executa tudo ao mesmo tempo,só uma condicao nesse bloco sera executada -
condicao = False

if condicao:
    print('Este é o código do if')
else:
    print('')
print('fora do if')


if 10==10:
    print('Outro if')

print('Fora do if')


################################################################
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Código para a Condicao 1 ')
    print('Código 2 para a Condicao 1 ')
elif condicao2:
    print('Código para a Condicao 2  ')
elif condicao3:
    print('Código para a Condicao 3')
elif condicao4:
    print('Código para a Condicao 4')
else:
    print('Nenhuma condicao foi satisfeita')##a condicao a ser executada é essa

