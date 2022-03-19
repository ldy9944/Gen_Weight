print('표준 체중 계산을 시작합니다.')
user_gender = input('성별을 입력해 주세요(M or F)')
try:
    user_height = int(input('신장을 입력해 주세요(cm)'))

except ValueError:
    print('올바른 값을 입력하세요')

else:
    if user_gender == 'M':
        g_weight = (user_height / 100) * (user_height / 100) * 22
        print('키 {0}cm 남성의 평균 체중은 {1}kg입니다.'.format(user_height, round(g_weight, 2)))
    elif user_gender == 'F':
        g_weight = (user_height / 100) * (user_height / 100) * 21
        print('키 {0}cm 여성의 평균 체중은 {1}kg입니다.'.format(user_height, round(g_weight, 2)))
    else:
        print('올바른 값을 입력하세요')