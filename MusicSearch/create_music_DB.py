import json

def load_existing_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"songs": []}  # 파일이 없을 경우 빈 리스트를 가진 구조를 반환

def lyrics_to_list(lyrics):
    # 줄바꿈을 기준으로 문자열을 분할하고 빈 문자열을 제거하여 리스트로 반환합니다.
    return [line for line in lyrics.split('\n') if line.strip() != '']

def save_song_to_json(title, artist, lyrics, url, filename="song_data.json"):
    # 기존 데이터를 불러옵니다.
    data = load_existing_data(filename)
    
    # 가사를 리스트로 변환합니다.
    lyrics_list = lyrics_to_list(lyrics)
    
    # 새 노래 정보를 추가합니다.
    new_song = {
        "title": title,
        "artist": artist,
        "lyrics": lyrics_list,  # 가사를 리스트 형태로 저장
        "url": url             # 노래의 URL 추가
    }
    data["songs"].append(new_song)
    
    # 변경된 데이터를 파일에 다시 씁니다.
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 사용자로부터 노래 정보와 URL을 입력받습니다.
title = "우주를 줄게"
artist = "볼빨간사춘기"
url = "https://www.youtube.com/watch?v=9U8uA702xrE"
lyrics = '''
커피를 너무 많이 마셨나 봐요
심장이 막 두근대고 잠은 잘 수가 없어요
한참 뒤에 별빛이 내리면 난
다시 잠들 순 없겠죠

지나간 새벽을 다 새면
다시 네 곁에 잠들겠죠
너의 품에 잠든 난 마치
천사가 된 것만 같아요
난 그대 품에 별빛을 쏟아 내리고
은하수를 만들어 어디든 날아가게 할거야

Cause I’m a pilot anywhere
Cause I’m a pilot anywhere
lighting star shooting star 줄게 내 Galaxy
Cause I’m a pilot anywhere
Cause I’m your pilot 네 곁에
저 별을 따 네게만 줄게 my Galaxy

Like a star 내리는 비처럼
반짝이는 널 가지고 싶어
Get ma mind
엄지와 검지만 해도 내 마음을 너무 잘 표현해
붙어 안달 나니까
마냥 떨리기만 한 게 아냐
준비가 되면 쏘아 올린 인공위성처럼
네 주윌 마구 맴돌려 해
더 가까워진다면 네가 가져줄래
이 떨림을

어제는 내가 기분이 참 좋아서
지나간 행성에다가
그대 이름 새겨 놓았죠
한참 뒤에 별빛이 내리면
그 별이 가장 밝게 빛나요

지나간 새벽을 다 새면
다시 네 곁에 잠들겠죠
별빛 아래 잠든 난 마치
온 우주를 가진 것만 같아
난 그대 품에 별빛을 쏟아 내리고
은하수를 만들어 어디든 날아가게 할거야

Cause I’m a pilot anywhere
Cause I’m a pilot anywhere
Lighting star Shooting star 줄게 내 Galaxy
Cause I’m a pilot anywhere
Cause I’m your pilot 네 곁에
저 별을 따 네게만 줄게 my Galaxy

Cause I’m a pilot anywhere
Cause I’m a pilot anywhere
Lighting star Shooting star 줄게 내 Galaxy
Cause I’m a pilot I’m your pilot
Lighting star Shooting star 줄게 my Galaxy

라라라라라 라라라라라
'''


# 입력받은 정보를 JSON 파일로 저장합니다.
save_song_to_json(title, artist, lyrics, url)
