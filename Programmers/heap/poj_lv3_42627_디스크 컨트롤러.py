'''
1초씩 세면서.. heap에 넣어야 하나?

종료 시각 - 요청 시각
'''

import heapq

def solution(jobs):
    N = len(jobs)
    jobs.sort()
    
    idx, cur_time = 0, 0
    queue, answer = list(), list()
    while idx < N or queue:
        # 도착한 job 대기 큐에 추가 
        while idx < N and jobs[idx][0] <= cur_time:
            heapq.heappush(queue, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1

        # queue에 작업이 있으면 job 수행
        if queue:
            job = heapq.heappop(queue)
            # 수행 완료 시간(종료 시각 - 요청 시각) = cur_time + 수행 시간job[0] - 요청 시각job[1]
            cur_time += job[0]
            answer.append(cur_time - job[1])
        else:
            cur_time += 1
    
    s = 0
    for ans in answer:
        s += ans

    return s//N


print(solution([[2, 2], [0, 10]]))
# 3 + 5 = 4