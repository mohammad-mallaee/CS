from time import time

def power_set(S: list):
    p = [[]]
    for element in S:
        for i in range(len(p)):
            p.append(p[i] + [element])
    return p

power_set_length = 20
my_set = [i for i in range(1, power_set_length + 1)]
start = time()
my_set_power_set = power_set(my_set)
print(len(my_set_power_set), time() - start)
