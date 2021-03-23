# 1904 01타일

n = int(input())
data_list = [0] * 1000001
data_list[1] = 1
data_list[2] = 2

for idx in range(3, n + 1):
    data_list[idx] = (data_list[idx - 2] + data_list[idx - 1]) % 15746

print(data_list[n])