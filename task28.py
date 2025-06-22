#  Satr uzunligi bo'yicha guruhlash

# **Funksiya yarat**:

# ```python
# def group_by_length(words: list[str]) -> dict[int, list[str]]:
# ```

# **Shart**: Har bir so'zni uzunligiga qarab dict ichiga guruhlab joylashtir.

# ---

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """
    So'zlarni uzunligiga qarab guruhlaydi.

    Args:
        words (list[str]): So'zlar ro'yxati

    Returns:
        dict[int, list[str]]: Har bir uzunlik uchun tegishli so'zlar ro'yxati
    """
    result = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)

    return result

words = ["kitob", "salom", "men", "sen", "dastur", "AI"]

print(group_by_length(words))

