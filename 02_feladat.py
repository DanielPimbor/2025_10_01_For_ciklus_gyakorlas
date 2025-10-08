"""Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket."""

b = int(input('Add meg az első számod (ez lesz a "b" szám): '))
a = int(input('Add meg a második számod (ez lesz az "a"" szám): '))

if a > b and b + 1 != a:
    for i in range(b + 1, a):
        print(f'Ezek a számok vannak közöttük: {i}')

elif a < b and a + 1 != b:
    for i in range(b - 1, a , -1):
        print(f'Ezek a számok vannak közöttük: {i}')

elif a + 1 == b or b + 1 == a:
    print('Nincsenek közöttük egész számok.')

else:
    print('Ugyanazokat a számokat adtad meg.')