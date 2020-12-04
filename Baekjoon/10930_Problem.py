# 10930 SHA- 256

import hashlib

s = input()
# 해쉬 함수 이용
print(hashlib.sha256(s.encode()).hexdigest())
