def elso():
    a: float = float(input("Kérek egy számot, ami nagyobb, mint 2: "))
    if a < 3 or a % 1 != 0:
        while a < 3 or a % 1 != 0:
            print("2-nél nagyobb egész számot kell megadni!")
            a: float = float(input("Kérek egy 2-nél nagyobb számot: "))
    
    i: int = 1
    while i <= a:
        maradek = i % 3
        if maradek == 0:
            if i == a or i == a - 1 or i == a - 2:
                print(i, end=" ")
            else:
                print(i, end=", ")
        i += 1

def masodik():
    a: float = float(input("Kérek egy pozitív egész számot: "))
    if a <= 0 or a % 1 != 0:
        while a <= 0 or a % 1 != 0:
            print("Pozitív egész számot kell megadni!")
            a: float = float(input("Kérek egy pozitív egész számot: "))
    
    i: int = 0
    while i < a:
        if i == a - 1:
            print(int(a - i), end=" ")
        else:
            print(int(a - i), end=", ")
        i += 1

def harmadik():
    a: int = int(input("Kérek egy 5-tel osztható számot: "))

    if a % 5 != 0:
        while a % 5 != 0:
            print("5-tel osztható számot kell megadni")
            a: int = int(input("Kérek egy 5-tel osztható számot: "))
    
    print(f"A(z) {a} egy öttel osztható szám")

def negyedik(a):
    a: float = float(input("Kérek egy számot: "))
    if a % 1 != 0 or a == 0:
        while a % 1 != 0 or a == 0:
            print("Törtet vagy 0-át nem adhatsz meg!")
            a: float = float(input("Kérek egy számot: "))

    if a > 0:
        i = 1
        while i <= a:
            logikai(i,a)
            i+=1
    elif a < 0:
        b = -1
        while b >= a:
            logikai(b,a)
            b-=1

def logikai(i,a):
    if i % 3 == 0 and i % 2 == 0:
        if i == a:
            print("BUMMBAM", end=" ")
        else:
            print("BUMMBAM", end=", ")
    elif i % 3 == 0:
        if i == a:
            print("BUMM", end=" ")
        else:
            print("BUMM", end=", ")
    elif i % 2 == 0:
        if i == a:
            print("BAM", end=" ")
        else:
            print("BAM", end=", ")
    else:
        if i == a:
            print(i, end=" ")
        else:
            print(i, end=", ")


def negyedikteszt(a):
    if a % 1 != 0 or a == 0:
        while a % 1 != 0 or a == 0:
            print("Törtet vagy 0-át nem adhatsz meg!")
            a: float = float(input("Kérek egy számot: "))

    if a > 0:
        i = 1
        while i <= a:
            logikai(i,a)
            i+=1
    elif a < 0:
        b = -1
        while b >= a:
            logikai(b,a)
            b-=1
