#Dolgozhatsze
a=int(input("Add meg hány éves vagy: "))
if a<15:
        print("Te még nem dolgozhatsz!")
elif 15<a<18:
    print("Korlátozottan dolgozhatsz!")

else:
    print("Teljes mértékben munkaképes vagy!")

b=int(input("Mennyi pénzt akarsz keresni: "))

if b>200000:
    print("Ehhez aztán nem kell sokat dolgoznod!")
elif 200000<b<500000:
    print("Napi 8 óra")
else:
    print("Ehhez napi 10-12 órát kell dolgoznod,de sokat fogsz keresni!")

