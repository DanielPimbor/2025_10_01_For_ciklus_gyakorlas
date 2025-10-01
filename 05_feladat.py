"""Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:"""

szam = int(input('Adj meg egy számot, és megadom a szorzótábláját. '))

for i in range(0, 11):
    print(f'{szam} X {i} = {szam * i}')