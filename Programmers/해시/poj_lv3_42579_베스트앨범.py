'''
장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 출시
노래는 고유 번호로 구분
1. 속한 노래가 많이 재생된 장르를 먼저 수록한다 (장르 총합으로 먼저 장르 순서를 결정)
2. 장르 내에서 많이 재생된 노래를 먼저 수록한다 (그 장르 안에서 재생수 기준으로 수록)
3. 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록한다 (같으면 고유번호)

베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
장르별 두 개씩!

장르의 종류를 모르므로 장르별 변수를 만들 수는 없다.

이게 정렬을 해야할까..?
장르 종류는 100개 미만...  장르에 속한 곡이 하나면 하나의 곡만 선택한다 
0. genre:{id:plays,}
1. 리스트 안에 장르별로 딕셔너리를 만들기 [{id:plays}, ..]
2. 총 재생수로 정렬
3. 각 장르내에서 재생수로 정렬

["classic", "classic", "classic"]
[500, 600, 150]

'''

def solution(genres, plays):
    songs_d = { genre:{} for genre in set(genres) }
    for i in range(len(genres)):
        songs_d[genres[i]][i] = plays[i]
    
    songs = list(songs_d.values())
    # 총 재생수로 장르 정렬
    songs.sort(key=lambda x: sum(x.values()), reverse=True)
    
    answer = []
    # 장르 내에서 재생수로 정렬 + 결과 기록
    for i in range(len(songs)):
        songs[i] = sorted(songs[i].items(), key=lambda x: x[1], reverse=True)
        answer.append(songs[i][0][0])
        if len(songs[i]) > 1: # 장르별 음원이 1개인 경우
            answer.append(songs[i][1][0])
    
    return answer

'''
# 260731
문제를 잘못 읽고 장르를 두 개 꼽고 그 장르 내에서 최대 두 곡을 뽑는 건 줄 알고 풀다가.
이전 코드를 보며 공부하다가 뒤늦게 문제를 잘못 이해했다는 걸 깨달았다
문제를 잘 읽어야 하는 이유..

개선:
    (1) 장르 내 정렬 시 동점 규칙이 있고 각각 오름차순, 내림차순이어서 정렬을 두 번 했다. 이걸 한 줄로 줄일 수 있다고 함
        => lambda x: (-x[1], x[0]) 마이너스 기호를 사용할 수 있는 건 처음 알았다'
    (2) 마지막 반복문 순회 자료형 변경 및 딕셔너리 변수명 개선
        장르별 노래를 모아둔 songs를 genre_songs로 바꾸고, 
        매 반복 시 인덱스를 사용하는 게 아니라 genre_songs의 각 원소(songs)로 직접 받아서 쓴다
        반복문 내에서 장르 내 정렬 후 변수명도 ranked로 수정해서 가독성을 높인다
    (3) answer 업데이트 로직 개선
        하나 넣고 조건 검사 후 하나를 더 넣는 방식이 아니라 for문으로 answer 업데이트
'''

def solution(genres, plays):
    genre_dict = {genre:{} for genre in set(genres)}
    for i in range(len(plays)):
        genre_dict[genres[i]][i] = plays[i]
    
    # 장르 정렬
    songs = sorted(genre_dict.values(), key=lambda x: sum(x.values()), reverse=True)
    
    answer = []
    for i in range(len(songs)):
        # 장르 내 정렬
        songs[i] = sorted(songs[i].items(), key=lambda x: x[0])
        songs[i] = sorted(songs[i], key=lambda x: x[1], reverse=True)
        answer.append(songs[i][0][0])
        if len(songs[i]) > 1:
            answer.append(songs[i][1][0])

    return answer

# 개선 후 

def solution(genres, plays):
    genre_dict = {genre:{} for genre in set(genres)}
    for i in range(len(plays)):
        genre_dict[genres[i]][i] = plays[i]
    
    # 장르 정렬
    genre_songs = sorted(genre_dict.values(), key=lambda x: sum(x.values()), reverse=True)
    
    answer = []
    for songs in range(len(genre_songs)):
        # 장르 내 정렬
        ranked = sorted(songs.items(), key=lambda x: (-x[1], x[0]))
        for id, _ in ranked[:2]:
            answer.append(id)

    return answer


'''
# 260810
지난 번에 착각한 걸 이번에는 다시 제대로 풀 수 있었다
초반에는 딕셔너리 안에 리스트로 풀었다가... 인덱싱할 때 문제가 생겨서 다행히 딕셔너리 안에 딕셔너리로 풀 수 있었다
'''

def solution(genres, plays):
    songs = {genre:{} for genre in set(genres)}
    for i, play in enumerate(plays):
        songs[genres[i]][i] = play

    # 장르 내 곡 정렬
    top_genres = sorted(songs.values(), key=lambda x: sum(x.values()), reverse=True)
    
    # 장르 내 곡 선정
    answer = []
    for genre_songs in top_genres:
        top_songs = sorted(genre_songs.items(), key=lambda x: (-x[1], x[0]))
        for i, _ in top_songs[:2]:
            answer.append(i)

    return answer