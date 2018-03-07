#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
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
