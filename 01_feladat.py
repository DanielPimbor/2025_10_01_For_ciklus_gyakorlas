"""Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét."""

szam = int(input('Adj meg egy egész számot. '))

eredmény = 0

for i in range (0, szam):
    eredmény += i

print(f'Az 1-től a megadott számig terjedő egész számok összege HA az adott számot nem kell hozzáadni (pl. az adott szám 3 -> 0 + 1 + 2 = 3): {eredmény}')
