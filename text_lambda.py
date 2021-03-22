# Вычисление вхождений символов в текст с помощью лямбды
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
count = sum(map(lambda x : 1 if '' in x else 0, text_string)) 
print(f'Количество вхождений равно = {count}')
