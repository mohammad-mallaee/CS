def recover(d):
    a = d.copy()
    for i in range(1, len(d)):
        if a[i - 1] > d[i] & d[i] != 0:
            return "-1"

        a[i] = d[i] + a[i - 1]
    res = ""
    for j in range(0, len(d)):
        res += str(a[j]) + (" " if j < len(d) - 1 else "")
    return res


n = int(input())
answers = []
for i in range(n):
    count = int(input())
    ds = [int(num_str) for num_str in input().split(" ")]
    answers.append(recover(ds))

for answer in answers:
    print(answer)
