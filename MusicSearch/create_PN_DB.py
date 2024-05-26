from openai import OpenAI
import csv
from convertPcode import text_to_ipa

# OpenAI 클라이언트 초기화
client = OpenAI()


def create_embeddings(text):
    # OpenAI로부터 텍스트 임베딩 생성
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

def save_to_csv(original_text, ipa_text, embedding):
    # CSV 파일 이름 지정
    filename = 'PN_DB.csv'
    
    # CSV 파일을 append 모드로 열기
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # 리스트 형태의 임베딩을 하나의 문자열로 변환하여 저장
        embedding_str = ','.join(map(str, embedding))
        # CSV 파일에 데이터 쓰기
        writer.writerow([original_text, ipa_text, embedding_str])

def process_text(text):
    ipa_text = text_to_ipa(text)
    embedding = create_embeddings(ipa_text)
    save_to_csv(text, ipa_text, embedding)
    print(f"Data saved for {text}")

# 예제 사용
process_text("let it go let it go can hold it back anymore")