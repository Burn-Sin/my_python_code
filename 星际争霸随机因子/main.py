import re,random

map = ['机会渺茫','泯灭快车','虚空降临','克哈裂痕','虚空撕裂','升格之链','聚铁成兵','净网行动','黑暗杀星','熔火危机','营救矿工','王者之夜','天界封锁','死亡摇篮','往日神庙']

regex = r"(?<=\d\.\s).*?(?=\：)"

yinzi = open('F:\my_python_code\星际争霸随机因子\因子.txt',encoding='utf-8')

while True:

    print('因子数量：')

    num = input('')

    yinzi_list = re.findall(regex, yinzi.read())

    print(random.sample(yinzi_list, int(num)))

    num = input('')
