from openai import OpenAI
client = OpenAI()


text = "부처핸썸"
def text_to_ipa(text):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "너는 IPA 변환기야. 예시) 안녕 hi: anɲjʌŋ haɪ"},
        {"role": "user", "content": text},
    ],
    temperature= 0 
    )

    return response.choices[0].message.content