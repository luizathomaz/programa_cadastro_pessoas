from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mErro\033[m')
    sleep(1)
