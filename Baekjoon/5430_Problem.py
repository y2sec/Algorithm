# 5430 AC

import collections
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    lst = collections.deque(list(map(int, sys.stdin.readline().replace('[', '').replace(']', '').replace(',', ' ').split())))
    direction = True
    isAvailable = True
    for oper in p:
        if oper == 'R':
            direction = not direction
        elif oper == 'D' and lst:
            if direction:
                lst.popleft()
            else:
                lst.pop()
        elif oper == 'D' and not lst:
            isAvailable = False
            break

    if isAvailable:
        print('[', end='')
        if direction:
            if lst:
                print(lst.popleft(), end='')
            while lst:
                print(',', end='')
                print(lst.popleft(), end='')
        else:
            if lst:
                print(lst.pop(), end='')
            while lst:
                print(',', end='')
                print(lst.pop(), end='')
        print(']')
    else:
        print('error')
