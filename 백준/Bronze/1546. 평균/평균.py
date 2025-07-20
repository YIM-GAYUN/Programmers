n = int(input())
scores = list(map(int, input().split()))
M = max(scores)
new_scores = [(x/M)*100 for x in scores]
average = sum(new_scores) / n
print(average)