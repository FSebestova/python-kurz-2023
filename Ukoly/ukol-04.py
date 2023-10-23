import math  

# definuje funkci pro práci s telefoním číslem, nahradí mezery v čísle, spočítá počet číslic v čísle a vezme v potaz předvolbu
def phone_number(number:str):
    number = number.replace(" ", "")
    if len(number) == 9 or len(number) == 13 and number[0:3] == "+420":
     return True
    else:
     return False

# nastaví cenu SMS a spočítá počet znaků a zaokrouhlí nahoru aby byl výpočet ceny přesný a vrátí konečnou cenu
def SMS(message:str):
    sazba = 3
    cena = (math.ceil(len(message) / 180)) * sazba
    return cena

#zeptá se na telefoní číslo a zprávu a nastaví cenu SMS, validacční hláška na telefoní číslo
number = input("Zadej telefoní číslo: ")
if phone_number(number):
   message = input("Zadej zprávu pro příjemce: ")
   cena = SMS(message)
   print(f"Cena Vaší SMS zprávy je {cena}")
else:
   print("Telefoní číslo není platné")
