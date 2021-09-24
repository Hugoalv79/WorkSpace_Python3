def palabra():
    word = "AAAAA"
    test7 = "F"
    while test7 != True:
        word = input("Introduce una palabra: ")
        test7 = word.islower()
        if test7 == False:
             print("Todas las letras deben de ser minúsculas")
    length_ = len(word)
    for letter in word:
        if letter in "aeiou":
            word = word.replace(letter,letter.upper())
    # print(f"{word} tiene {length_} letras")
    return word,length_

x = palabra()
# print(x)
print(f"{x[0]} tiene {x[1]} letras")