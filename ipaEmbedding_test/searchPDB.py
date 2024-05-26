from openai import OpenAI
import csv
from scipy.spatial.distance import cosine
import numpy as np
from convertPcode import text_to_ipa


def find_closest_texts(input_text, filename='Ideaton/ipaEmbedding_test/embeddings.csv', top_n=2):
    client = OpenAI()
    
    # 입력 텍스트의 IPA 변환 및 임베딩을 생성합니다.
    ipa_text = text_to_ipa(input_text)  # 이 함수는 실제 IPA 변환을 위해 구현해야 합니다.
    response = client.embeddings.create(
        input=ipa_text,
        model="text-embedding-3-small"
    )
    input_embedding = np.array(response.data[0].embedding)

    # CSV 파일에서 원본 텍스트와 임베딩을 읽어 들입니다.
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            original_text = row[0]
            embedding = np.array(row[2].split(','), dtype=float)  # 임베딩 데이터를 배열로 변환
            data.append((original_text, embedding))

    # 각 임베딩과 입력 임베딩 간의 코사인 유사도를 계산합니다.
    similarities = [(original_text, 1 - cosine(input_embedding, emb)) for original_text, emb in data]

    # 유사도가 높은 순서대로 정렬합니다.
    similarities.sort(key=lambda x: x[1], reverse=True)

    # 가장 유사한 top_n 개의 원본 텍스트를 반환합니다.
    closest_texts = [text for text, _ in similarities[:top_n]]

    return closest_texts

# 예시 사용
closest_texts = find_closest_texts("but yo han sup")
print("가장 유사한 텍스트들:", closest_texts)
