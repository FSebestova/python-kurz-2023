books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},  #0
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},  #1
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},  #2
]

print(books[2])
print(books[0])
print(books[1]["title"])

hodnoceni = ["Kniha 1", 4, "Kniha 2", 5, "Kniha 3", 3.3]
hodnoceni1 = [
    ["Kniha1", 4], 
    ["Kniha2", 5], 
    ["Kniha3", 3.3]
]

print(hodnoceni1[0][1])
print(hodnoceni1[0][0][0])

for polozka in hodnoceni1:
    print(polozka[0] + " " + str(polozka[1]))