# 24: Eng ko‘p uchragan harfni topish

# **Funksiya yarat**:

# ```python
# def most_common_char(text: str) -> str:
# ```

# **Shart**: Berilgan matndagi eng ko‘p uchraydigan bitta harfni qaytar

def most_common_char(text: str) -> str:
    """
    Matndagi eng ko‘p uchraydigan bitta harfni qaytaradi.

    Args:
        text (str): Kiruvchi matn

    Returns:
        str: Eng ko‘p uchragan bitta harf
    """
    frequency = {}

    for char in text:
        if char.isalpha():  # faqat harflarni hisoblaymiz
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    # Eng ko‘p takrorlangan harfni topish
    most_common = max(frequency, key=frequency.get)
    return most_common
    
print(most_common_char("salom hammaga")) 