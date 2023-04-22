print("------------------------------------------------")
print("-----------------Multiplos 7 y 9----------------")
print("------------------------------------------------")



multiplos_7 = 0
multiplos_9 = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        multiplos_7 += 1
    if i % 9 == 0:
        multiplos_9 += 1

print("Entre 1000 y 5000 hay: "+ str (multiplos_7) + " múltiplos de 7 y "+ str(multiplos_9) + " múltiplos de 9.")
