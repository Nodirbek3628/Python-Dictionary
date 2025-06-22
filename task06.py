# Foydalanuvchidan `kalit` nomini input orqali so‘ra. Agar dictda shu kalit bo‘lsa, qiymatini chiqarsin, aks holda `"Topilmadi"` chiqarsin.

car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"
}

keys = input()         #kiritilgan so'z dicta bulsa qiymat  chiqadi keys: value

key = car.get(keys,"topilmadi")

print(key)