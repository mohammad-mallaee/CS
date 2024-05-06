import random
import importlib

hash_table_module = importlib.import_module("4")

a_access = 0
b_access = 0
assigns = 0
helper_access = 0
comparisons = 0


def are_equal(A: list[int], B: list[int]):
    global a_access, b_access, assigns, helper_access, comparisons
    n = len(A)
    helper_list = [0] * (2 * n + 1)
    for number in A:
        a_access += 1
        assigns += 1
        helper_list[number] = 1
    for number in B:
        comparisons += 1
        helper_access += 1
        b_access += 1
        if helper_list[number] == 0:
            return False
    return True


def find_a_b(x: int, A: list[int], B: list[int]):
    n = len(A)
    hash_table = hash_table_module.HashedTable(4 * n)
    for number in A:
        hash_table.add(number)
    for number in B:
        if hash_table.search(x - number):
            return True
    return False


def test_find():
    for i in range(1, 7):
        n = 10**i
        A = [random.randint(1, n**4) for _ in range(n)]
        B = [random.randint(1, n**4) for _ in range(n)]
        x = random.randint(1, n**4)
        print(f"length of A and B is 10^{i}")
        print(
            f"x was {x} and",
            "found" if find_a_b(x, A, B) else "couldn't find",
            "two numbers that equal x",
        )
        print()


def test_equal():
    global a_access, b_access, assigns, helper_access, comparisons
    for i in range(1, 7):
        n = 10**i
        A = [random.randint(1, 2 * n) for _ in range(n)]
        B = [random.randint(1, 2 * n) for _ in range(n)]
        print(f"length of A and B is 10^{i}")
        print("A and B are", "equal" if are_equal(A, B) else "not equal")
        print(f"a_access: {a_access}, b_access: {b_access}, assigns: {assigns}")
        print(f"helper_access: {helper_access}, comparisons: {comparisons}")
        print()
        a_access = b_access = assigns = helper_access = comparisons = 0


test_find()
