print(f"Números de l'1 al 10 amb for:")
for num in range(1, 11):
    print(f"{num}")

print(f"Números de l'1 al 10 amb while:")
num = 1
while num <= 10:
    print(f"{num}")
    num += 1

suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma dels primers 10 números és {suma}\n")


fruits = ["poma", "pera", "raïm", "plàtan"]
print(f"Elements de la llista:")
for fruit in fruits:
        print(f"{fruits}")
print()

num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
parells = []
imparells = []
for n in num:
    if n % 2 == 0:
        parells.append(n)
    else:
        imparells.append(n)

print(f"Números parells: {parells}")
print(f"Números imparells: {imparells}\n")

suma = 0
n = 0
while suma < 100:
    suma += n
    n += 1
print(f"La suma dels números fins a arribar a 100 és {suma}\n")


num = 250
while True:
    if 100 <= num <= 400:
        print(f"El número {num} està entre 100 i 400.")
        break
    else:
        print(f"El número {num} no està entre 100 i 400.")
        break

