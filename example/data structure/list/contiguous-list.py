# Python의 list는 동적 배열
names = []

# 요소 추가 (append)
names.append("Alice")
names.append("Bob")
names.append("Charlie")
print(f"초기 리스트: {names}")

# 요소 접근 (get)
print(f"인덱스 1의 이름: {names[1]}")

# 요소 변경 (set)
names[0] = "Anna"
print(f"변경 후 리스트: {names}")

# 요소 삭제 (remove, pop)
names.pop(2) # 인덱스 2의 'Charlie' 삭제
print(f"삭제 후 리스트: {names}")

# 현재 크기 확인 (len)
print(f"리스트 크기: {len(names)}")