import array

# 'i'는 부호 있는 정수(integer) 타입을 의미
numbers = array.array('i', [10, 20, 30, 40, 50])

# 배열 요소에 접근
print(f"첫 번째 요소: {numbers[0]}")
print(f"세 번째 요소: {numbers[2]}")

# 배열 요소 변경
numbers[1] = 25
print(f"변경된 두 번째 요소: {numbers[1]}")

# 배열 순회
print("전체 배열 요소:", end=" ")
for num in numbers:
    print(num, end=" ")
print()