def int_function(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False

words = input('введите строку из слов разделенных пробелами - ').split()
for w in words:
    result = int_function(w)
    if result:
        print(int_function(w), ' ')
