# Yosh bo‘yicha guruhlash

# **Funksiya yarat**:

# ```python
# def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
# ```

# **Shart**: Har bir odamni `age` bo‘yicha guruhlab, ismlarini list ko‘rinishida qaytar.

# ---

def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    """
    Odamlarni yosh (age) bo‘yicha guruhlab, ismlarini ro‘yxat shaklida qaytaradi.

    Args:
        people (list[dict[str, int | str]]): Har bir elementda 'name' va 'age' mavjud

    Returns:
        dict[int, list[str]]: Har bir yoshga tegishli ismlar ro‘yxati
    """
    result = {}

    for person in people:
        age = person["age"]
        name = person["name"]
        
        if age not in result:
            result[age] = []
        result[age].append(name)

    return result

people = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 21},
    {"name": "Laylo", "age": 20},
    {"name": "Sami", "age": 22},
    {"name": "Lola", "age": 21}
]

print(group_by_age(people))
