# 1568 새

birds = int(input())
result = 0
song = 1
# 새의 수가 0이 될 때까지 규칙을 반복
while birds != 0:
    if song > birds:
        song = 1

    result += 1
    birds -= song
    song += 1

print(result)
