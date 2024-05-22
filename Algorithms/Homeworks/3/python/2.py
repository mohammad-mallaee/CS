def min_trash_bins(points: list):
    points.sort()
    n = len(points)
    i = 0
    bins = []
    while i < n:
        p = points[i]
        j = 1
        while i + j < n and abs(p - points[i + j]) <= 2:
            j += 1
        bins.append((p + points[i + j - 1]) / 2)
        i = i + j
    return bins


print(min_trash_bins([1, 1.2, 1.3, 2, 2.1, 3, 3.01, 5, 4.5, 3, 8]))
print(min_trash_bins([2.01, 8, 6, 0.7, 4, 9, 0.3]))