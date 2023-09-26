print('  martin   '.strip()) #strip() : Odstraní všechny bílé znaky na začátku a konci řetězce

print("martin".upper()) #převádí na velká písmena
print("martin".lower()) #převádí na malá písmena

print('po ut st čt pá'.split(' ')) #rozdělí pomocí zadaneého znaku například mezery
print('+'.join(['1', '2', '3', '4'])) #spojí pomocí zadaneého znaku například mezery



text = "Kurz vede lektor Marek"
novy_text = text.replace("Marek", "Martin")  #nahradí tex  za text nový
print(novy_text)
