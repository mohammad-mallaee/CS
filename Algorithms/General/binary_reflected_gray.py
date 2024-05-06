def brgc(n):
    if n == 1:
        return ["0", "1"]
    else:
        l1 = brgc(n-1)
        l2 = [""] * len(l1)
        length = len(l1)
        for i in range(length):
            l2[length - i - 1] = l1[i] + "1"
            l1[i] = l1[i] + "0"
        return l1 + l2
    

def sdv(n):
    if n == 1:
        return ["0", "1"]
    else:
        l1 = sdv(n-1)
        l2 = list(reversed(l1))
        for i in range(len(l1)):
            l1[i] = l1[i] + "0"
            l2[i] = l2[i] + "1"
        return l1 + l2
