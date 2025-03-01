from collections import Counter #리스트 속 요소들의 등장 횟수를 빠르게 세기 위해 활용
import re #정규 표현식을 이용해 특정 패턴의 단어를 찾기 위해 활용

# 파일 읽기
file_path = "C://Users//kanga//Downloads//example.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 1. 'Rebecca' 단어 개수 세기 (대소문자 구분 O)
rebecca_count = text.count("Rebecca")
print(f"'Rebecca' 단어 개수: {rebecca_count}")

# 2. 4글자 이상의 단어 중 가장 많이 나온 단어 Top 5 (대소문자 구분 X)
words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())  # 4글자 이상 단어 찾기 (원본 텍스트를 소문자로 변환하여 대소문자 구분 없이 단어의 빈도를 세기 위한 코드)
word_counts = Counter(words)  # 단어 개수 세기

# 가장 많이 나온 단어 상위 5개 출력
top_5_words = word_counts.most_common(5)
print("가장 많이 나온 4글자 이상 단어 Top 5:")
for word, count in top_5_words:
    print(f"{word}: {count}")