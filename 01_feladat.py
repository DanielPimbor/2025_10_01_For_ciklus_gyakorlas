"""Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét."""

szam = int(input('Adj meg egy egész számot. '))

eredmény = 0

for i in range (0, szam + 1):
    eredmény += i

print(f'Az 1-től a megadott számig terjedő egész számok összege: {eredmény}')
