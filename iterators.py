arr = iter(range(1, 11))

for _ in range(5):
    print(next(arr))

print("stop")

for _ in range(5):
    print(next(arr))
