n = int(input())
count = 0

for _ in range(n):
    word = input()
    group = True
    seen = set()
    prev_w = ''
    
    for w in word:
        if w != prev_w:
            if w in seen:
                group = False
                break
            seen.add(w)
        prev_w = w
    
    if group:
        count +=1
        
print(count)
    