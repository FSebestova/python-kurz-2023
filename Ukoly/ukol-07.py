import re

data = """2.2.2022
13. 8. 1999
4/5/2001"""

"""5.123.458.91
21.4
8./9"""
regularni_vyraz = re.compile(r"(\d{1,2}[.\/]\s?\d\s?[.\/]\s?\d{4})")

vysledek = regularni_vyraz.findall(data)

print(vysledek)