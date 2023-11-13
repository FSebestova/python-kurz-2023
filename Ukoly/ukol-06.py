class Auto:
    def __init__(self,registracni_znacka,typ_vozidla,najete_km,dostupne=True) -> None:
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla"
        else: 
            return f"Vozidlo není k dispozici"
        
    def vrat_auto(self,stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        self.dostupne = True
        if pocet_dni < 7:
            cena_den = 400
        else:
            cena_den = 300
            celkova_cena = cena_den * pocet_dni
        return f"Cena za půjčení vozu je {celkova_cena} Kč."
    
    def get_info(self):
        return f"Typ vozidla {self.typ_vozidla} jeho registrační značka {self.registracni_znacka}"
    
Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)


vyber_vozidla = input(("Máme k dispozici vozidlo Peguot nebo Škoda. Jaké vozidlo chcete? "))

if vyber_vozidla == "Škoda":
    print(Skoda.get_info())
    print(Skoda.pujc_auto())
elif vyber_vozidla == "Peugeot":
    print(Peugeot.get_info())
    print(Peugeot.pujc_auto())
else:
    print(f"Tato značka není k dispozici") 

pocet_dni = int(input("Zadej počet dní: "))
stav_tachometr = int(input("zadej stav tachometru: "))
print(Peugeot.vrat_auto(stav_tachometr, pocet_dni))
print(Skoda.vrat_auto(stav_tachometr, pocet_dni))
