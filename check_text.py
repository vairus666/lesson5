# #Check text


def sum_text(string):
    return len(string)    

def sum_words(string): 
    return string.count(' ') + 1

def sum_sentence(string):
    if string == '':
        return 0
    else:
        a = string.count('.')
        b = string.count('?')
        c = string.count('!')
        if a | b | c == 0:
            return 1 
        return a + b + c

frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()

print(f'Количество вхождений равно = {sum_text(text_string)}')
print(f'Количество слов равно = {sum_words(text_string)}')
print(f'Количество предложений равно = {sum_sentence(text_string)}')
