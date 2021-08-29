import re,random,os

map = ['机会渺茫','泯灭快车','虚空降临','克哈裂痕','虚空撕裂','升格之链','聚铁成兵','净网行动','黑暗杀星','熔火危机','营救矿工','王者之夜','天界封锁','死亡摇篮','往日神庙']

regex = r"(?<=\d\.\s).*?(?=\：)"



while True:

    print('因子数量：')

    num = input('')



    path = os.getcwd() + '\因子.txt'

    print(path)

    yinzi = open(path,encoding='utf-8')

    yinzi_list = re.findall(regex, yinzi.read())

    print(random.sample(yinzi_list, int(num)))

    na = input('')
