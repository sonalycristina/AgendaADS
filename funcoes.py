#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv
import sys

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print('4 Buscar contato pelo nome')
	print('9 Para sair do programa')

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:").lower()
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	
	
	
def listar():
	data = open('agendatelefonica.csv')
	numero = 0
	for linhas in data:
		numero = numero + 1
		print (numero, linhas)

	print ('Listado corretamente')
	data.close()	


def falha():
	print("Opcao Incorreta")

def buscar_nome():
	import csv #importa biblioteca csv
	lista = [] #cria 1 lista
	with open('agendatelefonica.csv') as csvfile: #abre arquivo csv
		leitor = csv.reader(csvfile, delimiter=',') #le arquivo csv
		for linha in leitor: #poem na variavel linha cada linha do arquivo
        		lista.append(linha) #adiciona para lista
	
	x = 0
	nome = input('Escreva o nome que procura na agenda:\n').lower()
	while x < len(lista): #enquanto x for menor que numero de contatos faca
		a = lista[x] # a recebe lista posicao x
		if nome in a: # se nome estiver na variavel a
			print('Nome: {} - Telefone: {}'.format(a[0],a[1])) #escreva 
		x+=1
    
	if x == len(lista): #se mesmo apos procurar nome em a e nao encontrar apos loop while terminar entrara nesta condicao
		print('Contato inexistente!! Favor cadastrar o contato')
