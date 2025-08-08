end = int(input())
now = 1
room = 1
while (now < end):
    now += 6 * room
    room += 1
print(room)