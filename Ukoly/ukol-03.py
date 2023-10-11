import json

with open("Ukoly/body.json", mode="r", encoding="utf-8") as file:
    body = json.load(file)
    prospech = {}
    for klic, hodnota in body.items():
        if hodnota >= 60:
            prospech[klic] = "pass"
        else:
            prospech[klic] = "faild"

            
with open("Ukoly/prospech.json", mode= "w", encoding="utf-8") as file:
                json.dump(prospech, file, ensure_ascii=False)


