# Quyidagi dictga `email` kalitini qo‘sh: `"email": "ali@example.com"`

# ```python
# person = {"name": "Ali", "age": 25}
# ```

person = {
    "name": "Ali", 
    "age": 25,
}

per = person["email"] = "ali@example.com"

print(person)
