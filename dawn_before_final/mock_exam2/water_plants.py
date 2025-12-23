n, a, b = map(int, input().split())
plants = list(map(int, input().split()))
alice_pointer = 0
bob_pointer = n - 1
alice_water = a
bob_water = b
alice_count = 0
bob_count = 0
while alice_pointer < bob_pointer:
    if alice_water >= plants[alice_pointer]:
        alice_water -= plants[alice_pointer]
        alice_pointer += 1
    else:
        alice_count += 1
        alice_water = a - plants[alice_pointer]
        alice_pointer += 1
    if bob_water >= plants[bob_pointer]:
        bob_water -= plants[bob_pointer]
        bob_pointer -= 1
    else:
        bob_count += 1
        bob_water = b - plants[bob_pointer]
        bob_pointer -= 1
if alice_pointer == bob_pointer:
    if max(alice_water, bob_water) < plants[alice_pointer]:
        alice_count += 1

print(alice_count + bob_count)