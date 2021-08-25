#                                                   WHILE
# While loops are very flexible, we can do a lot because we have a conditional statement. 
# "For" loops are simpler. When your´not sure how many times you will loop

# EXAMPLE 1
# In the need of send a message based on a dta base, we can use "While" to keep sending messages until it´s
# over.

# 
lista_del_super = [1,2,3]


for item in lista_del_super:
    print(item)

i = 0
while i < len(lista_del_super):
    print(lista_del_super[i])
    i += 1
lista_del_super = 0
while True:
    print(lista_del_super[i])
    break
# "While True" always will be True, so break will get the loop only execute 1 time.

while True:
    print(lista_del_super[i])
    break

while True:
    response = input("Say tomething: ")
    if (response == "bye"):
        break

