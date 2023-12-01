massiv = [1, 2, 3]
a = 0
for num in massiv:
    a += num
print(f"Sonlar yeg'indisi {a}")


target = int(input("son kirit:"))
massiv = [5, 3, 3, 5, 7, 4, 4, 4]

def find_occurrences(massiv, target):
    occurrence_count = 0

    for num in massiv:
        if num == target:
            occurrence_count += 1

    return occurrence_count


print(find_occurrences(massiv, target))


num1 = int(input("enter number: "))
num2 = int(input("enter number again: "))
if num1 == num2:
    num3 = num2 ** 2
    print("True")
    print(f"{num2}-ning kvadrati {num3}")
else:
    print("False")