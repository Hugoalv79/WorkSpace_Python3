from time import sleep
print("0:0:0")
sleep(.2)
for i in range(0,24):
    sleep(1)
    for j in range (0,60):
        for n in range (0,59):
            n += 1
            print(i,":",j,":",n)
