limite = 100001
i = 3
cuenta = 1
primo = 2
while cuenta < limite:
    for x in range(3, int(i ** 0.5) + 1, 2):
        if i % x == 0:
            break
    else:
        primo = i
        cuenta += 1
    i += 2
print(primo)