#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Seleccionaste", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 3:
        funcoes.excluir()
elif opcao == 4:
	funcoes.buscar_nome()
elif opcao == 9:
        exit()
else:
	funcoes.falha()


