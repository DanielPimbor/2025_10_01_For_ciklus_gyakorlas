"""Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

jelszo = input('Add meg a jelszavat. ')

while True: 

    if jelszo == 'alma1234':
        print('Belépés engedélyezve ✓ ')
        break

    else:
        print('Belépés megtagadva ✖ ')
        jelszo = input('Próbáld újra: ')