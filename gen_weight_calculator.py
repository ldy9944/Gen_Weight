while True:
    # 身長及び性別をinput, 入力が間違えると再起動
    user_gender = input('性別を入力してください')

    try:
        user_height = int(input('身長を数字のみで入力してください(cm)'))

    except ValueError:
        print('身長は数字のみ入力してください。\nプログラムを再起動します。')
        print()
        continue

    # 様々な性別入力バリエーションに合わせて入力値を自動修正、入力が間違えると再起動
    m_list = ['男性', 'Man', 'man', 'Men', 'men' 'Male', 'male', '男子', '男', 'M', 'm']
    f_list = ['女性', 'Woman', 'woman' 'Women', 'women', 'Female', 'female', '女子', '女', 'F', 'f']

    if user_gender in m_list:
        user_gender = 'M'
        break
    elif user_gender in f_list:
        user_gender = 'F'
        break
    else:
        print('性別の入力を確かめてください。\nプログラムを再起動します。')
        print()
        continue

# 標準体重計算
if user_gender == 'M':
    g_weight = (user_height / 100) * (user_height / 100) * 22
    print('身長{0}cm男性の標準体重は{1}kgです。'.format(user_height, round(g_weight, 2)))
    print('プログラムを終了致します。\nご利用いただきありがとうございました。')
if user_gender == 'F':
    g_weight = (user_height / 100) * (user_height / 100) * 21
    print('身長{0}cm女性の標準体重は{1}kgです。'.format(user_height, round(g_weight, 2)))
    print('プログラムを終了致します。\nご利用いただきありがとうございました。')
