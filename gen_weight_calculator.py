# 身長及び性別をinput
user_gender = input('性別を入力してください')
user_height = int(input('身長を数字のみで入力してください(cm)'))

# 様々な性別入力バリエーションに合わせて入力値を自動修正
m_list = ['男性', 'Man', 'man', 'Men', 'men' 'Male', 'male', '男子', '男']
f_list = ['女性', 'Woman', 'woman' 'Women', 'women', 'Female', 'female', '女子', '女']

if user_gender in m_list:
    user_gender = 'M'
elif user_gender in f_list:
    user_gender = 'F'
else:
    print('性別の入力を確かめてください。')
    print()

# 標準体重計算
if user_gender == 'M':
    g_weight = (user_height / 100) * (user_height / 100) * 22
    print('身長{0}cm男性の標準体重は{1}kgです。'.format(user_height, round(g_weight, 2)))
    print('プログラムを終了致します。\nご利用いただきありがとうございました。')
if user_gender == 'F':
    g_weight = (user_height / 100) * (user_height / 100) * 21
    print('身長{0}cm女性の標準体重は{1}kgです。'.format(user_height, round(g_weight, 2)))
    print('プログラムを終了致します。\nご利用いただきありがとうございました。')