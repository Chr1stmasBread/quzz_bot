def choice_weapon():
    choice_gun = input()
    if choice_gun == "1":
        print("gun_1")
    elif choice_gun == "2":
        print("gun_2")
    elif choice_gun == "3":
        print("gun_3")
    else:
        print("invalid choice")

def choice_door():
    choice_doors = input()
    if choice_doors == "1":
        choice_door_1()
    elif choice_doors == "2":
        choice_door_2()
    elif choice_doors == "3":
        choice_door_3()
    else:
        print("invalid choice")

def block_door():
	print("Вы погибли")

def choice_way():
    choice = input()
    if choice == "1":
        block_door()
    elif choice == "2":
        choice_door()
    elif choice == "3":
        window_open()


def window_open():
    window_open = input()
    if window_open and choice_weapon(1):
        print("Вы смогли сломать окно с помощью топора")
    elif window_open and choice_weapon(2):
        print("Вы смогли сломать окно с помощью приклада оружия")
    elif window_open and "ломик":
        print("Вы смогли сломать окно с помощью ломика")

def choice_door_1():
    print("Вы решили пройти через дверь №1")
    print("Вы погибли")
def choice_door_2():
    print("Пройти через одну из дверей")
    choice_door = input()
    if choice_door == "2" and choice_weapon(1):
        print("Открыть дверь №2")
        print("Вы погибли")
    elif choice_door == "2" and choice_weapon(2):
        print("Открыть дверь №2")
        print("Вы погибли")
    elif choice_door == "2" and choice_weapon(3):
        choice_door_2_3()
    else:
        print("Ответ должен быть числом(1, 2, 3)")

def choice_door_2_3():
    way = input()
    if way == "1" and choice_door_2(3):
        choice_door_2(3)
        print("Вы сошли с ума")
    elif way == "2" and choice_door_2(3):
        choice_door_2(3)
        print("Вы умерли красиво")
def choice_door_3():
    print("Вы решили пройти через дверь №3")
    print("Вы смогли выйти из дома")
def choice_out_home_with_window():
    choice_out_home = input()
    if choice_out_home == "1":
        print("Остаться в комнате")
    elif choice_out_home == "2":
        print("Вы решаетесь открыть дверь №1")
    elif choice_out_home == "3":
        print("Вы решаетесь открыть дверь №2")
    else:
        print("Ответ должен быть числом(1, 2, 3)")

print("сцена 1")
# Переход на сцену 2
print("сцена 2")
print()
