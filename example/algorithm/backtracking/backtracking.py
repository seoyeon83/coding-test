# 백트래킹 (핵심: 고르기 -> 재귀 -> 되돌리기)

# 조합 직접 구현하기
def my_comb(items, k):
    result, picked = [], []

    # 지금까지 picked에 고른 것에 이어서 start 이후의 원소들로 나머지를 채운 모든 경로를 result에 저장한다
    def go(start):
        # 다 고른 경우 (재귀 종료)
        if len(picked) == k:
            result.append(picked[:])    # 복사해서 저장
            return
        for i in range(start, len(items)):
            picked.append(items[i])     # 고르기
            go(i + 1)                   # 나머지는 다음 단계에
            picked.pop()                # 되돌리기 (원상복구)
            # 다음 반복할 때 이전 반복의 잔여물이 남지 않도록 비워주는 것

    go(0)   # 처음부터 시작
    return result

# 순열 직접 구현하기
# 이때 조합과 달리 go에 원소가 없고 used를 쓰는 이유는 뭘까?
# 조합은 원소 순서 상관없이 원소만 있으면 되는 반면 순열은 순서가 중요하다
# 따라서 원소를 고를 때 나를 제외한 모든 원소를 고려해야 한다
def my_perm(items, k):
    result, picked = [], []
    used = [False] * len(items)
    def go():
        if len(picked) == k:
            result.append(picked[:])
            return
        for i in range(len(items)):
            # 이미 사용한 거면 넘기기
            if used[i]:
                continue
            used[i] = True
            picked.append(items[i])
            go()
            picked.pop()
            used[i] = False
    go()
    return result

# 가지치기 예: 최솟값 찾기에서 이미 현재 최선보다 나쁘면 중단
# 예시를 3일 동안 매일 점심 메뉴를 고르는데 총 점심값의 최솟값을 구하는 것으로 구체화해보자

prices = [
  [5, 3, 8],   # 1일차 메뉴 가격
  [4, 6, 2],   # 2일차
  [7, 1, 9],   # 3일차
]
DAYS = 3
best = float("inf")
def search(day, spent):
    global best
    if spent >= best:   # 이미 최저가 이상 썼으면 그만
        return
    if day == DAYS:     # 3일치를 다 정했으면 끝
        best = spent    # 위에서 걸러졌으니 spent < best 보장
        return
    for price in prices[day]:
        search(day + 1, spent + price)

search(0, 0)
print(best)