##fruts=['яблоко', "банан", "арбуз"]
##print(fruts)
##fruts.append('персики')
##print(fruts)
##ansure='марковка' in fruts
##print(ansure)
##results='марковка' not in fruts
##print(results)

name=input('Как тебя зовут? ')
print('Привет '+name+' Время поиграть в поле чудес')
word='арбуз'
letters=[]
ittems=3
while ittems>0:
    victory=True
    later=input('введите букву ')
    letters.append(later)
##    print(letters)
    for i in word:
        if i in letters:
            print(i, end=' ')
        else:
            print('*', end=' ')
            victory=False
    print()
    if later not in word:
        ittems -= 1
        if ittems == 0:
            print("ты проиграл")
            print("Секретное слово " + word)
    if victory == True:
        print("ты победил")
        break
