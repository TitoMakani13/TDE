# partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
#classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
#obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
#para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo).

#Entrada
idade=int(input("Digite sua idade: "))

#Desenvolvimento
if idade <16:
    print('Não votante')
if idade >=18 and idade <=65:
    print('Eleitor obrigatório')
if idade >=16 and idade <18:
    print('Voto opcional')
if idade >65:
    print('Eleitor facultativo')