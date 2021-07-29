def zh(text):
    datas = text.replace('0','zero').replace('1','one').replace('zero',zero).replace('one',one)
    return datas



if __name__ == '__main__':
    #l = 4400,4400
    #S = 540,5220
    #根据美的的编码规则，L A A' B B' C C' S L A A' B B' C C' O
    # 为最普通的开机码，其中L为引导码，A、B、C为决定温度，风速，模
    # 式的码，A'，B'，C'分别为A，B，C按位
    # 取反后的码，S为分隔码，O为终止码


    one = '550,1660,'
    zero = '550,550,'
    back = {
        'l':'4400,4400,',

        'A': zh('10110010'),
        'A2': zh('01001101'),

        'B': zh('00011111'),
        'B2': zh('11100000'),

        'C': zh('00000000'),
        'C2': zh('11111111'),

        'S':'550,5220,',
        'O' : '550,8000'
    }

    data = back['l']+\
           back['A']+back['A2']+\
           back['B']+back['B2']+\
           back['C']+back['C2']+\
           back['S']+back['l']+\
           back['A']+back['A2']+\
           back['B']+back['B2']+\
           back['C']+back['C2']+\
           back['O']



    print(data)
