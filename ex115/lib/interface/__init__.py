def leiaInt(mensagem):
    while True:
        try: 
            a = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            break
        else:
            return a


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc