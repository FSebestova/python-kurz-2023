jmeno = str(input("Zadej jméno:"))
domena = "@czechitas.cz"
email = str(jmeno + domena)
print(f"Váš email je: {email}")

#BONUS

jmeno_a_prijmeni = str(input("Zadej jméno a přijmení: "))
print(jmeno_a_prijmeni.upper()) #velká
print(jmeno_a_prijmeni.lower()) #malá
l=jmeno_a_prijmeni.find(" ")
print(jmeno_a_prijmeni[:l].capitalize() + " " + jmeno_a_prijmeni[l+1:].capitalize()) 
print(jmeno_a_prijmeni[0:1].capitalize() + "."+" " + jmeno_a_prijmeni[l+1:l+2].capitalize()+".") 
