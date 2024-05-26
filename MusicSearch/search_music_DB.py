import json

def search_lyrics(lyrics_part, filename="song_data.json"):
    # 파일에서 데이터를 불러옵니다.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."

    # 가사 부분이 포함된 노래를 찾습니다.
    results = []
    for song in data["songs"]:
        if lyrics_part.lower() in song["lyrics"]:
            results.append((song["title"], song["artist"]))

    return results if results else "검색된 노래가 없습니다."

# 사용자로부터 검색할 가사 부분을 입력받습니다.
lyrics_part = "More than the air"

# 함수를 호출하여 결과를 출력합니다.
result = search_lyrics(lyrics_part)
print(result)
