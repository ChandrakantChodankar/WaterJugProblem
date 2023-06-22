# jug problem
jugA = int(input("Enter the capacity of jug A "))
jugB = int(input("Enter the capacity of jug B "))
jugAi = int(input("Enter the initial capacity of A "))
jugBi = int(input("Enter the initial capacity of B "))
jugAf = int(input("Enter the final state "))


print("Operations")
print("1: Fill the Jug A completely")
print("2: Fill the Jug b completely")
print("3: Empty the Jug A completely on ground")
print("4: Empty the Jug B competely on ground")
print("5: Pour the water from Jug A to B completely")
print("6: Pour the water from Jug B to A or until Jub B becomes completely empty")
print("7: Pour the water from Jug B to Jug A")
print("8: Pour the water from Jug A to jug B")


while (jugAi != jugAf):
    op = int(input("Enter the operation: "))
    if (op == 1):
        jugAi = jugA

    elif (op == 2):
        jugBi = jugB

    elif (op == 3):
        jugAi = 0

    elif (op == 4):
        jugBi = 0

    elif (op == 5):
        if (jugB-jugBi > jugAi):
            jugBi = jugBi+jugAi
            jugAi = 0
        else:
            jugAi = jugAi-(jugB-jugBi)
            jugBi = jugB

    elif (op == 6):
        if (jugA-jugAi > jugBi):
            jugAi = jugAi+jugBi
            jugBi = 0
        else:
            jugBi = jugBi-(jugA-jugAi)
            jugAi = jugA

    elif (op == 7):
        jugAi = jugAi+jugBi
        jugBi = 0

    elif (op == 8):
        jugBi = jugBi+jugAi
        jugAi = 0

    print(jugAi, jugBi)
