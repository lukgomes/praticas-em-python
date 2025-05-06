import re

CPF_MASK = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
CNPJ_MASK = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'

doc = input('Digite o cpf ou cnpj para validação:\n')

if re.match(CPF_MASK, doc):
    print("O numero é um cpf válido")
elif re.match(CNPJ_MASK, doc):
    print("O numero é um cnpj valido")
else:
    print("O numero não é um documento valido.")