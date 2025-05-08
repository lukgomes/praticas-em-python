""""
nome
telefone
email
"""

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
            print("="* 50)
            print(f'NOME\t\tTELEFONE\t\tEMAIL\n{"-" * 50}')
            for contato in contatos:
                print(f'{contato['nome']}\t\t{contato['telefone']}\t\t{contato['email']}')
            print("="* 50)
        case '2':
            nome = input('informe o nome: ')
            telefone = input('informe o telefone: ')
            email = input('informe o email: ')

            contatos.append({"nome": "lucas", "telefone": "123456789", "email": "lucas@mail.com"})

            contatos['nome'] = nome
            contatos['telefone'] = telefone
            contatos['email'] = email
        case '3':
            pass
        case '4':
            pass
        case '0':
            pass