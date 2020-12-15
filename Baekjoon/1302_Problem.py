# 1302 베스트셀러

n = int(input())

books = dict()

# 책을 입력받으면 dict에 해당 책 수를 1 올려줌
for _ in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

# books를 정렬해주는데 수를 우선으로 정렬하고 그 이후에 이름으로 정렬
# 수를 우선으로 정렬할 때 -를 붙여줌으로써 가장 큰 수가 앞으로 오면서 사전 상 빠른 것이 앞으로 오게함
books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(books[0][0])
