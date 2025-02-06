# 1. NumPy 배열 생성 및 연산
# NumPy를 사용해 3x3 정수 배열(1부터 9까지)과 2x5 실수 배열(0~1 사이 난수)을 생성하세요. 
# 생성한 배열의 합계와 평균을 각각 계산하고, 두 배열을 곱한 결과를 출력하세요.
# 배열의 형태를 유지하지 않아도 괜찮습니다.
import random
import numpy as np

array_int = np.arange(1,10).reshape(3,3)
array_float = np.random.rand(2,5)

mean_int = array_int.mean()
mean_float = array_float.mean()

sum_int = array_int.sum()
sum_float = array_float.sum()

print("3x3 정수 배열의 평균: ",mean_int)
print("3x3 정수 배열의 합계: ",sum_int,"\n")

print("2x5 실수 배열의 평균: ",mean_float)
print("2x5 실수 배열의 합계: ",sum_float,"\n")



print("두 배열을 곱한 결과: ")
print( np.outer(array_int.flatten(),array_float.flatten()) )

# ================================================
# 2. Pandas를 활용한 데이터 처리
# 아래 데이터를 DataFrame으로 생성하세요.
#   Name: [Alice, Bob, None, Charlie] Age: [25, None, 28, 35] City: [New York, None, Chicago, None]
# 누락된 이름은 "Unknown"으로, 나이는 평균 나이로 채우고 수정된 DataFrame을 출력하세요.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', None, 'Charlie']
    ,'Age': [25, None, 28, 35]
    ,'City': ['New York', None, 'Chicago', None]
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)

# ================================================
# 3. HTTP 통신을 활용한 데이터 읽기 및 저장
# https://jsonplaceholder.typicode.com/todos 에서 JSON 데이터를 가져오세요. 
# 데이터를 파일로 저장한 뒤, "title" 키의 값을 출력하세요.

import requests
import pandas as pd
import json

# HTTP GET 요청 보내기
response = requests.get('https://jsonplaceholder.typicode.com/todos')

#데이터를 파일로 저장하기
with open('todos.json', 'w') as f:
    f.write(response.text)

with open('todos.json', 'r') as f:
    data = json.load(f)

for todo in data:
    print(todo["title"])