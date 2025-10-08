"""Számold ki egy adott szám faktoriálisát! A számot a felhasználótól kérd be!"""

szam = int(input("Adj meg egy pozitív egész számot: "))

faktorialis = 1

for i in range(1, szam + 1):
        faktorialis *= i

print(f"A(z) {szam} faktoriálisa: {faktorialis}")
