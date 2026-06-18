# coding-test
코딩 테스트 준비 기록용 레포지토리

### 규칙
- 파일명: 플랫폼 + (선택적으로 필요한 내용: level, tier) + 문제 번호 + 제목 (ex. poj_lv1_1111_제목.py)
- 디렉토리 구조: 문제 출처, 즉 플랫폼 별로 상위 폴더 구성
- 커밋 메시지 형식: [상태] 날짜 / 언어 / 시간 / 메모리 ([Add] 251201 / Python 3 / 52ms / 13425KB) 혹은 [상태] 와 날짜, 언어만 기재
    - [WIP] : Work in Progress
    - [Try] : 시도했지만 아직 풀지 못함
    - [Review] : 다른 사람 풀이를 참고해 정리
    - [Refactor] : 통과했지만 코드 개선
    - [Add] : 직접 문제 풀이 성공

### 복습 스케줄 (`review.py`)

커밋 기록을 기반으로 오늘 복습할 문제를 출력하는 스크립트.

```bash
python review.py
```

`[Add]` / `[Refactor]` / `[Review]` 커밋 날짜를 기준으로 복습 주기를 자동 계산한다.

| 커밋 상태 | 1차 | 2차 | 3차 |
|---|---|---|---|
| `[Add]` | 7일 | 30일 | 90일 |
| `[Refactor]` / `[Review]` | 1일 | 7일 | 21일 |

### 풀이 플랫폼
- Programmers (poj)
- 백준 (boj)
- solvesql (solvesql)
- 추가 예정
