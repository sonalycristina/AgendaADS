#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Excluir contatos da agenda")
	print('4 Buscar contato pelo nome')


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


def excluir():
	import csv
	lista = []
	agenda = open('agendatelefonica.csv')
	ler = csv.reader(agenda)
	for lin in ler:
		lista.append(lin)

	nome = input('Escreva o nome para excluir da agenda\n').lower()
	x=0
	while x<len(lista):
		contato = lista[x]
		if nome in contato:
			print('Deseja excluir este contato?\n')
			print('Nome {} - Telefone {}\n'.format(contato[0],contato[1]))
			resp=int(input('[1]Sim   [2]Nao'))
			if resp==1:
				del(lista[x])
				print('contato excluido')
				break
		x += 1
		if x==len(lista):
			print('contato nao encontrado')
	with open('agendatelefonica.csv', "wt") as arquivo:
		escritor = csv.writer(arquivo, delimiter=",")
		for linha in lista:
			escritor.writerow(linha)
			

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
    
