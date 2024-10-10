import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
file_path = 'C:/Users/User/Desktop/python_kaggle_dataScience/pythonApplication_2303110265/물놀이형수경시설수질검사결과현황.csv'

# 파일 인코딩 확인 및 읽기
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

# 데이터프레임의 열 이름 확인
print(df.columns)

# 필요한 열만 선택
df = df[['시설명', '소재지도로명주소', '채수및검사일자', 'PH(5.8~8.6)', '탁도(4NTU이하)', '대장균(200개체수/100MmL미만)', '유리잔류염소(0.4~4.0mg/L)']]

# 새 열 이름 지정
df.columns = ['facility_name', 'location', 'inspection_date', 'ph', 'turbidity', 'e_coli', 'residual_chlorine']

# '-' 값을 NaN으로 변환 후 NaN 값 제거
df.replace('-', pd.NA, inplace=True)
df.dropna(inplace=True)

# 열의 값을 숫자로 변환
df['ph'] = pd.to_numeric(df['ph'], errors='coerce')
df['turbidity'] = pd.to_numeric(df['turbidity'], errors='coerce')
df['e_coli'] = pd.to_numeric(df['e_coli'], errors='coerce')
df['residual_chlorine'] = pd.to_numeric(df['residual_chlorine'], errors='coerce')

# NaN 값 제거
df.dropna(inplace=True)

# 데이터 확인
print(df.head())

# pH 분석
ph_mean = df['ph'].mean()
ph_out_of_range = df[(df['ph'] < 5.8) | (df['ph'] > 8.6)]

# 탁도 분석
turbidity_mean = df['turbidity'].mean()
turbidity_out_of_range = df[df['turbidity'] > 5]

# 대장균 분석
e_coli_positive = df[df['e_coli'] > 0.5]

# 유리잔류염소 분석
residual_chlorine_mean = df['residual_chlorine'].mean()
residual_chlorine_out_of_range = df[(df['residual_chlorine'] < 0.2) | (df['residual_chlorine'] > 4.0)]

# pH 시각화
plt.figure(figsize=(10, 6))
plt.hist(df['ph'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of pH Levels')
plt.xlabel('pH')
plt.ylabel('Frequency')
plt.axvline(x=6.5, color='red', linestyle='--')
plt.axvline(x=8.5, color='red', linestyle='--')
plt.show()

# 탁도 시각화
plt.figure(figsize=(10, 6))
plt.hist(df['turbidity'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Turbidity Levels')
plt.xlabel('Turbidity')
plt.ylabel('Frequency')
plt.axvline(x=5, color='red', linestyle='--')
plt.show()

# 대장균 검출 시각화
plt.figure(figsize=(10, 6))
df['e_coli'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
plt.title('E. coli Presence')
plt.xlabel('E. coli Count')
plt.ylabel('Frequency')
plt.show()

# 유리잔류염소 시각화
plt.figure(figsize=(10, 6))
plt.hist(df['residual_chlorine'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Residual Chlorine Levels')
plt.xlabel('Residual Chlorine (mg/L)')
plt.ylabel('Frequency')
plt.axvline(x=0.2, color='red', linestyle='--')
plt.axvline(x=4.0, color='red', linestyle='--')
plt.show()

# pH 범위를 벗어난 시설 식별 및 시각화
print("===================================================================================")
print("pH 범위를 벗어난 시설 목록:")
print(ph_out_of_range[['facility_name', 'location', 'ph']])
print("===================================================================================")
# 대장균이 검출된 시설 목록
print("대장균이 검출된 시설 목록:")
print(e_coli_positive[['facility_name', 'location', 'e_coli']])
