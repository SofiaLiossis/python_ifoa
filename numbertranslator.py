# -*- coding: iso-8859-15 -*-

# Scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'� altra strada che quella
# di prevedere una traduzione semplice attraverso una tabella:
# 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilit� di prevedere
# una "traduzione" della decina e demandare la "traduzione"
# dell'unit� alla funzione che traduce fino a 20
# 25 -> decina = 2, unit� = 5


def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unit� di n
    return DECADES[decade-2] + translate_to_20(unit)



def translate_to_1000(n):
    if n < 100:
        return translate_to_100(n)
    if n > 999:
        return "Out of range"
    cent = n // 100
    decine = n % 100
    if cent > 1: #se le centinaia sono più di 1 traduci pure le centinaia
        return translate_to_20(cent) + "cento" + translate_to_100(decine) #altrimenti scrivi solo cento
    return "cento" + translate_to_100(decine)

def translate_to_1000000(n):
    if n < 1000:
        return translate_to_1000(n)
    if n > 999999:
        return "Out of range"
    migliaia = n // 1000
    cent = n % 1000
    if migliaia > 1 :
        return translate_to_1000(migliaia) + "mila" + translate_to_1000(cent)
    return "mille" + translate_to_1000(cent)


def translate_number(n):
    if (n == 0):
        return "zero"
    if (n < 0):
        return "meno " + translate_number(-n)
    result = translate_to_1000000(n).replace('iu', 'u').replace(
        'io', 'o').replace('au', 'u').replace('ao', 'o')
    return result


for x in range(1, 1000001):
    print(translate_number(x))



    

 