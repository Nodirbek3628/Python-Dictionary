# Bo‘sh `config` dict yarat. Foydalanuvchidan 3 ta `setting` nomi va qiymati so‘raladi. Ularni dictga joyla.

config = {}


for i in range(3):
    key = input(f"{i + 1}-Nomini kiriting: ")
    value = input(f"{i + 1}-qiymatni kiriting: ")
    config[key] = value
    

    

print(config)