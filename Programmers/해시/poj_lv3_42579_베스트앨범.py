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