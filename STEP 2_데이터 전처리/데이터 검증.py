import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 파일 불러오기
service_data = pd.read_csv('./서울시 개인서비스 요금 정보.csv', encoding = 'cp949')

# 데이터 확인
print(service_data.head())

#가설 1: 도봉구와 광진구의 경양식 업종의 개인서비스 가격은 차이가 있을 것이다.
service_data_theory1 = service_data[service_data['업종']=='경양식']

t_statistic, p_value = stats.ttest_ind(service_data_theory1[service_data_theory1['구명']=='도봉구']['가격(원)'],
                                       service_data_theory1[service_data_theory1['구명']=='광진구']['가격(원)'])

print("가설1: ", "도봉구와 광진구의 경양식 업종의 개인서비스 가격은 차이가 있을 것이다. p value: ", p_value)

#가설 2 : 동교동과 합정동의 미용업 업종의 개인서비스 가격은 차이가 있을 것이다.
service_data_theory2 = service_data[service_data['업종']=='미용업']

t_statistic, p_value = stats.ttest_ind(service_data_theory2[service_data_theory2['동명']=='동교동']['가격(원)'],
                                       service_data_theory2[service_data_theory2['동명']=='합정동']['가격(원)'])

print("가설2: ", "동교동과 합정동의 미용업 업종의 개인서비스 가격은 차이가 있을 것이다. p value: ", p_value)

#가설 3 : 창동에서 미용업과 숙박업 업종의 개인서비스 가격은 차이가 있을 것이다.
service_data_theory3 = service_data[service_data['동명']=='창동']

t_statistic, p_value = stats.ttest_ind(service_data_theory3[service_data_theory3['업종']=='미용업']['가격(원)'],
                                       service_data_theory3[service_data_theory3['업종']=='숙박업']['가격(원)'])

print("가설3: ", "창동에서 미용업과 숙박업 업종의 개인서비스 가격은 차이가 있을 것이다. p value: ", p_value)