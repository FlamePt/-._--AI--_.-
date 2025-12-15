

for i in range(4):
    num = float(input(f"Insira o número {i+1}: "))
    

for num in range(1, 5, 1):
    resto = num % 2
    if resto == 0 and num > 10:
        print(f"O número {num} é par e de valor superior a 10")
    elif resto == 0 and num < 10:
        print(f"O número {num} é par e de valor inferior a 10")
    elif resto != 0 and num > 10:
        print(f"O número {num} é ímpar e de valor superior a 10")
    elif resto != 0 and num < 10:
        print(f"O número {num} é ímpar e de valor inferior a 10")
