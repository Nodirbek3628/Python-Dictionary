# Qiymatlar bo‘yicha indekslarni guruhlash

# **Funksiya yarat**:

# ```python
# def group_indices(numbers: list[int]) -> dict[int, list[int]]:
# ```

# **Shart**: Har bir noyob son uchun u ro‘yxatda qayerda turganini ko‘rsatuvchi dict qaytar.
# ✅ Natija: `{1: [0, 2, 5], 2: [1, 4], ...}`



def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    """
    Har bir noyob son uchun u ro'yxatda qayerda turganini (indekslarini) ko'rsatuvchi lug'atni qaytaradi.

    Args:
        numbers (list[int]): Raqamlar ro'yxati

    Returns:
        dict[int, list[int]]: Har bir noyob raqam uchun indekslar ro'yxati
    """
    result = {}

    for index, number in enumerate(numbers):
        if number not in result:
            result[number] = []
        result[number].append(index)

    return result

nums = [1, 2, 1, 3, 2, 1]

print(group_indices(nums))