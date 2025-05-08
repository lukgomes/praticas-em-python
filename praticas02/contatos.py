""""
nome
telefone
email
"""
import os

contatos = [
    {"nome": "lucas", "telefone": "123456789", "email": "lucas@mail.com"},
    {"nome": "bruna", "telefone": "753951258", "email": "bruna@mail.com"},
    {"nome": "jao", "telefone": "258456789", "email": "jao@mail.com"}
]

while True:
    print("1 - listar\n2 - adicionar\n3 - editar\n4 - apagar\n0 - sair")
    op = input("o que deseja fazer: ")
    match op:
        case '1':
            os.system('clear')
            print("="* 70)
            print(f'NOME\t\tTELEFONE\t\tEMAIL\n{"-" * 70}')
            for contato in contatos:
                print(f'{contato['nome']}\t\t{contato['telefone']}\t\t{contato['email']}')
            print("="* 70)

        case '2':
            os.system('clear')
            nome = input('informe o nome: ')
            telefone = input('informe o telefone: ')
            email = input('informe o email: ')

            contatos.append({"nome": nome, "telefone": telefone, "email": email})

        case '3':
            os.system('clear')
            nome = input("qual o contato deseja editar: ")
            for index in range(len(contatos)):
                if nome == contatos[index]['nome']:
                    nome = contatos[index]['nome']
                    telefone = contatos[index]['telefone']
                    email = contatos[index]['email']
                    while True:
                        print(f'{contatos[index]}')
                        continuar = input("se os informações estiverem corretas, pressione 'q' para sair, se deseja continuar pressione 'c': ")
                        if continuar.lower() == 'q':
                            break
                        base = input("qual informação deseja alterar: ")
                        if base == "nome":
                            nome = input('Digite o nome novo: ')
                        elif base == "telefone":
                            telefone = input("Digite o telefone novo: ")
                        elif base == "email":
                            email = input("Digite o email novo: ")
                        else:
                            print('informação não condiz com o campo')
                        
                    contatos[index] = {"nome": nome, "telefone": telefone, "email": email}
                    found = 'yes'
                    break
                else:
                    found = 'not'

            if found == 'not':
                print('Nome não encontrado.')

        case '4':
            os.system('clear')
            nome = input("qual o contato deseja editar: ")
            for index in range(len(contatos)):
                if nome == contatos[index]['nome']:
                    contatos.pop(index)
                    found = 'yes'
                    break
                else:
                    found = 'not'
                
            if found == 'not':
                print('Nome não encontrado.')

        case '0':
            os.system('clear')
            print('ByeBye')
            break