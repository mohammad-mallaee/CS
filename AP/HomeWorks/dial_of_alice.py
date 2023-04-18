n = input()
words = input().split()
words = [w for w in words if len(w) > 4 and w[0].lower() == w[-1].lower()]
print(" ".join(sorted(words)))
