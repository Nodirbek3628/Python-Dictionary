# Quyidagi dictda faqat qiymati `True` bo‘lgan kalitlarni chiqar:

# ```python
# permissions = {"read": True, "write": False, "delete": True}
# # chiqishi: read, delete 


permissions = {
    "read": True, 
    "write": False, 
    "delete": True
    
}

for key, values in permissions.items():
    if values == True:
        print(key)