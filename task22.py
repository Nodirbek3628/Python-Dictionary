#  Talabalarni guruhlash

# **Funksiya yarat**:

# ```python
# def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
# ```

# **Shart**: Har bir talaba ismini u tegishli bo'lgan `group` bo'yicha dict shaklida qaytar.
# ✅ Natija: `{"A": ["Ali", "Soli"], "B": ["Vali", "Karim"]}`

def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    """
    Har bir talaba ismini u tegishli bo'lgan 'group' bo'yicha guruhlab, dict shaklida qaytaradi.

    Args:
        students (list[dict[str, str]]): Har bir elementida 'name' va 'group' mavjud bo'lgan talabalar ro'yxati.

    Returns:
        dict[str, list[str]]: Guruh nomi kalit, unga tegishli talabalar ismlari ro'yxati qiymat.
    """
    result = {}

    for student in students:
        group = student["group"]
        name = student["name"]

        if group not in result:
            result[group] = []
        result[group].append(name)

    return result

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Soli", "group": "A"},
    {"name": "Karim", "group": "B"}
]

natija = group_students(students)
print(natija)




