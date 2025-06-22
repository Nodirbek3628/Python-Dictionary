# Quyidagi dictdan `city` kalitini o‘chir:

# ```python
# person = {"name": "Ali", "age": 25, "city": "Tashkent"}
# ```

person = {
    "name": "Ali", 
    "age": 25, 
    "city":"Tashkent"
}

del person["city"]    # del bilan city key qiymati o'chirib tawlandi

print(person)