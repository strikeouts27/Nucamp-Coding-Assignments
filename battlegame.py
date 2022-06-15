wizard = "Wizard"
elf = "Elf"
human = "Human"
Wizard_HP = 70
Elf_HP = 100
Wizard_HP = 70
Wizard_Damage = 150
Elf_Damage = 100
Human_HP = 150
Human_Damage = 20
Dragon_HP = 300
Dragon_Damage = 50
while True:
    print("1    Wizard")
    print("2    Elf")
    print("3    Human")
    character = input(
        "Choose your character by pressing the corresponding number:")
    if character == "1":
        character = wizard
        my_hp = Wizard_HP
        my_damage = Wizard_Damage
        break
    if character == "2":
        character = elf
        my_hp = Elf_HP
        my_damage = Elf_Damage
        break
    if character == "3":
        character = human
        my_hp = Human_HP
        my_damage = Human_Damage
        break
    else:
        print("Unknown Character")
print(
    f"Your character is {character}, Your health point is {my_hp}, My attack power is {my_damage}")
# the f stands for format. This line is helpful 
while True:
    Dragon_HP = Dragon_HP - my_damage
    print("The", character, "damaged the Dragon! Its current health is", Dragon_HP)
    if Dragon_HP <= 0:  # this is one of the two exits.
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - Dragon_Damage
    print("The", character, "takes damage Your current health meter is at", my_hp)
    if my_hp <= 0:  # this is the second exit.
        print("The dragon devours you. At least you tried to stand up to evil!")
        break
