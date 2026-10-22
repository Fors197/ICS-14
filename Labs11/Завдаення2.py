
import json

with open("enterprises.txt", "r", encoding="utf-8") as file:
    enterprises = json.load(file)

best_name = ""
best_enterprise = {}
best_effect = 0

for name, data in enterprises.items():
    area = data["площа"]
    profit = data["прибуток"]
    effect = profit / area

    if effect > best_effect:
        best_effect = effect
        best_name = name
        best_enterprise = data

result = {
    "підприємство": best_name,
    "площа": best_enterprise["площа"],
    "прибуток": best_enterprise["прибуток"],
    "ефективність": round(best_effect, 2)
}

# Запис у файл effect.txt у форматі JSON
with open("effect.txt", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Дані про найефективніше підприємство записано у effect.txt")