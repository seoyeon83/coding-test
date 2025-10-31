'''
K번째 교환되는 수
배열 크기.. N이 매우 커서 시간 초과를 고민하고 있다...............

아니근데 애초에 선택정렬은 O(n^2)이잖아.. 
최적화를 해야하네.. 어떻게?

교환 횟수는 K.. N은 5 ~ 500,000인데
길이가 N인 배열에서 모든 교혼이 이루어진다고 하면 교환은 N-1만큼 이루어진다고 생각할 수 있다
근데 이때 교환 횟수가 K보다 작으면 -1을 리턴. 계산 전에 N-1과 K를 비교해본다면?
N-1은 모두 교환을 하게되는 최악의 경우.

하지만 그렇지 않은 경우에는 숫자도 크고 N도 큰데 선택 정렬 과정 자체를 최적화해야 하잖아.. 
그걸 어떻게 할 수 있는데? ㅠㅠ

아예 선택정렬을 쓰지말라고? 아나..
다른 효율높은 정렬 알고리즘으로 정렬하고 정렬된 거랑 비교해서 그 값을 찾는 방식으로?
어떤 값을 뒤로 보내야하는지를 이미 정렬해둔 걸로 확인할 수 있다 
이미 정렬한 배열을 알고 있으므로,,, 근데 그 큰 값을 딕셔너리로 알아낼 수 있다는 게
그 값의 인덱스를 저장한다고?
근데 중복값? 이 없네 그럼 ㄱㅊ겟다
'''

import sys 

def selection_sort(arr, sorted_arr, N, K):
    # 값별 인덱스 위치
    location = {arr[i]:i for i in range(N)}
    cnt = 0
    for last in range(N-1, 0, -1):
        # 범위 내 최댓값 위치 구하기
        m = location[sorted_arr[last]]

        # 다르면 바꾸기
        if m != last:
            arr[m], arr[last] = arr[last], arr[m]
            location[arr[last]] = last
            location[arr[m]] = m

            cnt += 1
            if cnt == K:
                return print(arr[m], arr[last])
                
    if cnt < K:
        return print(-1)
        

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

selection_sort(arr, sorted_arr, N, K)