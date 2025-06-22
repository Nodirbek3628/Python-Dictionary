# Funksiya yarat**:

# ```python
# def count_names(names: list[str]) -> dict[str, int]:

def count_names(names: list[str]) -> dict[str, int]:
    """Ismlarni sanash 
    Args:
        (names: list[str]: ismlar ro'yxati
    Returns:
        dict[str, int]:  natija
    """
    result = {}
    for name in names:
        result[name] = names.count(name) 
    return result





name_list = {"ali","vali","jon","bob","ali","vali","jon","bob","ali"}

result = count_names(name_list)
print(result)