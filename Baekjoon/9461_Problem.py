# 9461 파도반 수열

T = int(input())
tri_angle = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    tri_angle.append(tri_angle[i-1] + tri_angle[i-5])
for _ in range(T):
    N = int(input())
    print(tri_angle[N])
