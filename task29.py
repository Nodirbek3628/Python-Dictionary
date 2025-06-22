# Active foydalanuvchilarni chiqarish

# **Funksiya yarat**:

# ```python
# def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
# ```

# **Shart**: Faqat `"active": True` bo‘lgan foydalanuvchilarning ismini ro‘yxat qilib qaytar.

# ---

def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    """
    Foydalanuvchilar dictidan faqat "active": True bo‘lgan foydalanuvchilar ismlarini ro‘yxat qilib qaytaradi.

    Args:
        users (dict[str, dict[str, bool | str]]): Har bir foydalanuvchi uchun ichki dictda "active" mavjud.

    Returns:
        list[str]: Faqat faol foydalanuvchilarning ismlar ro‘yxati
    """
    active_users = []

    for name, info in users.items():
        if info.get("active") == True:
            active_users.append(name)

    return active_users

users = {
    "Ali": {"active": True, "email": "ali@example.com"},
    "Vali": {"active": False, "email": "vali@example.com"},
    "Soli": {"active": True, "email": "soli@example.com"}
}

print(get_active_users(users))
