n = int(input())

moves = []
for _ in range(n):
    a, b, g = map(int, input().split())
    moves.append((a, b, g))

best = 0

# Try every possible starting position
for start in [1, 2, 3]:
    pebble = start
    score = 0

    for a, b, g in moves:
        # Perform the swap
        if pebble == a:
            pebble = b
        elif pebble == b:
            pebble = a

        # Check Elsie's guess
        if pebble == g:
            score += 1

    best = max(best, score)

print(best)