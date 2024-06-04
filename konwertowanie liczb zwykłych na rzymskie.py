def konwertuj_na_rzymskie(liczba):
    rzymskie = ''
    rzymskie_cyfry = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    cyfry = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for cyfra in cyfry:
        while liczba >= cyfra:
            rzymskie += rzymskie_cyfry[cyfra]
            liczba -= cyfra        
    return rzymskie
 
try:
    liczba = int(input("Podaj liczbę dziesiętną do skonwertowania na rzymską: "))
    if liczba <= 0:
        print("Podaj liczbę większą od zera.")
    else:
        print("Liczba rzymska:", konwertuj_na_rzymskie(liczba))
except ValueError:
    print("To nie jest poprawna liczba całkowita.")