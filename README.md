# coding-test
코딩 테스트 준비 기록용 레포지토리

### 디렉토리 구조
문제 출처(플랫폼, 교재)별로 상위 폴더를 구성하고, 그 아래는 유형별 하위 폴더로 나눈다.

```
coding-test/
├── Baekjoon/       # 백준 (서비스 종료, 기존 기록 보관)
├── Programmers/    # 프로그래머스
├── solvesql/       # solvesql
├── Codetree/       # 코드트리
├── 이코테/         # <이것이 취업을 위한 코딩 테스트다> 예제·기출
│   ├── 05_DFS&BFS/
│   └── 13_DFS&BFS 기출/
└── example/        # 개념 정리용 예제 코드 (문제 풀이 아님)
```

### 규칙
- 파일명: 출처 + (선택적으로 필요한 내용: level, tier) + 문제 번호 + 제목 (ex. poj_lv1_1111_제목.py)

    | 출처 | 접두사 | 예시 |
    |---|---|---|
    | 프로그래머스 | `poj` | `poj_lv2_42746_가장 큰 수.py` |
    | 백준 | `boj` | `boj_gold4_14502_연구소.py` |
    | solvesql | `solvesql` | `solvesql_day1_lv1_사랑에 대한 영화 찾기.sql` |
    | 코드트리 | `ct` | `ct_L11_2021상반기오후1_나무 타이쿤.py` (문제 번호 대신 출제 회차) |
    | 이코테 | `ecote` | `ecote_4-1_상하좌우.py`, `ecote_Q11_뱀.py` (책의 예제 번호 / 기출 번호) |

    - 파일명만 보고 출처를 알 수 있게 접두사를 꼭 붙인다.
- 문제 기록: 문제 지문은 그대로 옮기지 않고, 문제 링크와 직접 쓴 요약만 주석으로 남긴다.
- 커밋 메시지 형식: [상태] 날짜 / 언어 / 시간 / 메모리 ([Add] 251201 / Python 3 / 52ms / 13425KB) 혹은 [상태] 와 날짜, 언어만 기재
    - [WIP] : Work in Progress
    - [Try] : 시도했지만 아직 풀지 못함
    - [Review] : 다른 사람 풀이를 참고해 정리
    - [Refactor] : 통과했지만 코드 개선
    - [Add] : 직접 문제 풀이 성공
    - `example` 등 문제 풀이가 아닌 커밋은 상태 없이 `날짜 / 언어 / 내용`으로 적는다 (ex. `261005 / Python 삼성 SW 템플릿 예제`).

### 개념 예제 (`example`)
문제 풀이와 별개로, 알고리즘·자료구조 개념을 직접 구현해 보며 정리한 코드. 파일명은 영어 소문자 + 하이픈(`bubble-sort.py`)으로 쓴다.

| 폴더 | 내용 |
|---|---|
| `algorithm/dfs&bfs` | BFS, DFS(재귀·스택), 최단 거리 BFS, flood fill |
| `algorithm/backtracking` | 조합, 순열, 중복순열, 가지치기 |
| `algorithm/simulation` | 격자 기본, 배열 회전, 중력·2048 합치기, 나선형, 동시 업데이트 |
| `algorithm/sort` | 정렬 알고리즘 구현, 다중 기준 우선순위 |
| `data structure` | 배열, 리스트, 스택, 큐, 그래프, 트리, 힙 (Python, C, Java) |
| `library` | 파이썬 표준 라이브러리 사용법 (`math`, `itertools` 등) |
| `pointer` | C 포인터 |

> 예제 파일 이름을 표준 라이브러리 모듈과 같게 지으면(ex. `heapq.py`) import가 꼬이므로 `heapq_example.py`처럼 접미사를 붙인다.

### 풀이 플랫폼
- Programmers (poj)
- 백준 (boj) - 서비스 종료로 기존 기록만 보관
- solvesql (solvesql)
- 코드트리 (ct)
- 이것이 취업을 위한 코딩 테스트다 (ecote)
- 추가 예정
