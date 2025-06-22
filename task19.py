# Quyidagi dictdagi barcha `qiymat`lar soni bo‘lsa, ularni yig‘indisini hisobla:

# ```python
# scores = {"math": 90, "english": 85, "science": 92}
# ```

scores = {"math": 90, "english": 85, "science": 92}


count = 0

for key, value in scores.items():
   if type(value) == int or type(value) == float:
      count += value
      print(count)

