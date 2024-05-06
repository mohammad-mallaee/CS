import math
import random


class HashedTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [None] * size
        self.filled_cells = 0
        self.insertion_counter = 0
        self.search_counter = 0

    def add(self, value: int):
        if self.filled_cells >= self.size:
            raise Exception("HashTable is full")
        self.table[self.get_insertion_index(value)] = value
        self.filled_cells += 1

    def get_insertion_index(self, value: int):
        hash_index = self.hash(value)
        start_index = -(len(self.table) - hash_index)
        for i in range(start_index, hash_index):
            if self.table[i] is None or self.table[i] is False:
                self.insertion_counter += 2 * abs(start_index - i)
                return i

    def hash(self, value: int):
        return value % self.size

    def search(self, value: int):
        hash_index = self.hash(value)
        start_index = -(len(self.table) - hash_index)
        for i in range(start_index, hash_index):
            if self.table[i] is None:
                self.search_counter += abs(start_index - i) + 1
                return False
            elif self.table[i] == value:
                if i >= 0:
                    return i
                else:
                    return len(self.table) + i
        self.search_counter += len(self.table)
        return False

    def delete(self, value: str):
        index = self.search(value)
        if index:
            self.table[index] = False
            self.filled_cells -= 1


def test_search():
    for i in range(1, 7):
        n = 10**i
        m = n // 2
        hash_table = HashedTable(n)
        alpha = m / n

        for _ in range(m):
            hash_table.add(random.randint(1, n**2))
            m += 1
        for _ in range(n):
            hash_table.search(random.randint(1, n**2))

        print(f">> n is 10^{i} and alpha is {alpha}:")
        print(
            "average uncessufull search comparisons is:", hash_table.search_counter / n
        )
        print(
            "in theory the average for search should be:",
            1 / 2 * (1 + (1 / ((1 - alpha) ** 2))),
        )


def test_add():
    for i in range(1, 7):
        n = 10**i
        m = n
        hash_table = HashedTable(m)

        for _ in range(m):
            hash_table.add(random.randint(1, n**2))

        print(f">> n is 10^{i}:")
        print("uncessufull add comparisons are", hash_table.insertion_counter)
        print(
            "in theory it should be:",
            math.sqrt(math.pi / 2) * (m**1.5),
        )


if __name__ == "__main__":
    print("\nTesting unseccussfull search comparisons ...\n")
    test_search()
    print("\n")
    print("Testing unseccussfull add comparisons ...\n")
    test_add()
