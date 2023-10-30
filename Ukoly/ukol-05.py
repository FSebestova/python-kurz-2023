import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne_teploty = [statistics.mean(den) for den in teploty]
ranni_teploty = [b[0] for b in teploty]
nocni_teploty =[c[3] for c in teploty]
poledne_noc = [[a[1], a[3]] for a in teploty]

print(prumerne_teploty)
print(ranni_teploty)
print(nocni_teploty)
print(poledne_noc)

teploty2 = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

den_teplota ={den[0]:statistics.mean(den[1:]) for den in teploty2}
print(den_teplota)