# Foydalanuvchidan kalit nomi so‘raladi. Agar dictda mavjud bo‘lsa, o‘chiriladi. Aks holda `"Bunday kalit yo‘q"` chiqariladi.
cars = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"
}

keys = input("key nomini kiriting: ")          

key = cars.get(keys,"Bunday kalit yuq ")
del cars[keys]    # kiritilgan suzimz dictda borligi uchun uchirib tashaldi

print(cars)



