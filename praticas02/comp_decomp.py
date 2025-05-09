
def compact_string(word):
    comp_word = ''
    cont = 1
    index = 0
    tamanho = len(word)
    while index <= tamanho:
        try:
            if word[index] == word[index + 1]:
                cont += 1        
                index += 1
            else:
                valor = word[index] + str(cont)
                comp_word += valor
                cont = 1
                index += 1
        except IndexError:
            valor = word[index] + str(cont)
            comp_word += valor
            cont = 1
            index += 1
            break
    return comp_word

    
def decompile_word(word):
    num = ''
    letter = ''
    decompiler = ''

    for i in range(len(word)):
        if not word[i].isdigit():
            letter = word[i]
        elif word[i].isdigit():
            num = word[i]
        
        if letter and num:
            cipher = letter * int(num)
            decompiler += cipher
            letter = ''
            num = ''

    return decompiler



word = 'aaabbc'

print(compact_string(word))