# Primeiro projeto desenvolvido por Emerson da Silva Vianna com a ajuda da Solyd iniciado 25/01/2022 #

print("AGENDA")

AGENDA = {}

#############################
def mostrar_contatos():
    for contato in AGENDA:
        buscar_contatos(contato)
        print('----------------')
#############################
def buscar_contatos(contato):
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]['telefone'])
    print("Email:", AGENDA[contato]['email'])
    print("Endereco:", AGENDA[contato]['endereco'])
#############################
def ler_detalhes_contato():
    telefone = input("Digite o telefone:")
    email = input("Digite o email:")
    endereco = input("Digite o endereco:")
    return telefone, email, endereco
#############################
def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email' : email,
        'endereco' : endereco,
    }
    salvar()
    print("!!!Contato {} adicionado/editado!!!".format(contato))
    print("----------------")
#############################
def excluir_contato(contato):
    AGENDA.pop(contato)
    print("!!!Contato {} excluido!!!".format(contato))
    salvar()
#############################
def salvar():
    exportar_agenda("database.csv")
#############################
def load():
    importar_agenda("database.csv")
#############################
def exportar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{};{};{};{}\n".format(contato, telefone, email, endereco))
            print("Contatos exportados com sucesso!")
            print("----------------------------")
    except:
        print("Algum erro ocorreu ao exportar a contatos")
#############################
def importar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contatos(nome, telefone, email, endereco)
    except FileNotFoundError:
        print("Arquivo nao encontrado!")
    except Exception as error:
        print("Algum erro ocorreu")
        print(error)
#############################
def imprimir_menu():
    print("1 - Mostrar contatos da agenda")
    print("2 - Buscar contato da agenda")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos")
    print("7 - Importar contatos")
    print("0 - Fechar Agenda")
#############################
load()
#############################
while True:

    imprimir_menu()

    print("----------------------------")
    opcao = input('Digite a opção desejada:')
    print("----------------------------")

    ########################
    if opcao == "1":
        mostrar_contatos()
    #########################
    elif opcao == "2":
        contato = input("Digite o nome do contato:")
        buscar_contatos(contato)
    ##########################
    elif opcao == "3":
        contato = input("Digite o nome do contato:")

        try:
            AGENDA[contato]
            print("Contato ja existente")
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
    ############################
    elif opcao == "4":
        contato = input("Digite o nome do contato:")

        try:
            AGENDA[contato]
            print("Editando contato: ", contato)
            incluir_editar_contatos(contato, telefone, email, endereco)
        except KeyError:
            print("Contato Inexistente")
    ############################
    elif opcao == "5":
        contato = input("Digite o nome do contato para ser excluido:")
        print("----------------------------")
        excluir_contato(contato)
        mostrar_contatos()
    #############################
    elif opcao == "6":
          exportar_agenda()
    #############################
    elif opcao == "7":
      nome_do_arquivo = input("Digite o nome do arquivo:")
      importar_agenda(nome_do_arquivo)
    #############################
    elif opcao == "0":
        print("Saindo do programa")
        print("----------------------------")
        break
    #############################
    else:
        print("OPCAO INCORRETA, SAINDO DO PROGRAMA")
        print("----------------------------")
    #############################
