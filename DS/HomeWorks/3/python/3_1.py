def simple_find_major(A: list) -> int:
    for i in A:
        count = 0
        for j in A:
            if i == j:
                count += 1
        if count > len(A) // 2:
            return i
        
    return -1
