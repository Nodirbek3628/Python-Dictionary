# `inventory` dict bor. Agar mahsulot yo‘q bo‘lsa, uni `quantity = 0` bilan qo‘sh.

inventory = {
    "Olma": 10 ,
    "gilos": 11,
    "pomidor":12,
    "nok" : 0
 }
product = input("Maxsulot nomini kiriting: ")


for product in not inventory:
    inventory[product]= 0

print(inventory)

# T.U.Sh