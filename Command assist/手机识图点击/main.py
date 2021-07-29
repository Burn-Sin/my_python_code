import os,cv2,time,queue,threading

def find_button(target, template):
    theight, twidth = target.shape[:2]
    # 寻找target图片在template中的位置，返回应该点击的坐标。
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 如果匹配度小于99%，就认为没有找到。
    if min_val > 0.01:
        return None
    strmin_val = str(min_val)

    # 绘制矩形边框，将匹配区域标注出来
    # cv2.rectangle(template, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val, template)
    # cv2.imwrite('1.png', template, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    x = min_loc[0] + twidth//2
    y = min_loc[1] + theight//2
    return (x, y)




def click(str):
    # 截图
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 保存
    os.system('adb pull /sdcard/screen.png')
    template = cv2.imread("screen.png")
    tgt = cv2.imread(str)
    find = find_button(target=tgt, template=template)
    x2,y2=find
    os.system('adb shell input tap {} {}'.format(x2, y2))
    if find==None:
        return False
    else:
        return True


if __name__ == '__main__':

    Q = queue.Queue()

    zb = [
        (441,1135),
        (431,901),
        (546,719),
        (698,1140),
        (213,1088),
        (260,620)
    ]

    target_list = {
        'open': 'res/s.png',
        'tz':'res/s2.png',
        'skip':'res/s3.png',
        'skip2':'res/s4.png',
        'back':'res/s5.png',
        'skip3':'res/s6.png'
    }


    for x,y in zb:
        os.system('adb shell input tap {} {}'.format(x,y))
        try:
            click(target_list['open'])
            click(target_list['tz'])
        except:
            try:
                click(target_list['back'])
            except:
                while True:
                    try:
                        click(target_list['open'])
                        click(target_list['tz'])
                    except:
                        try:
                            click(target_list['skip3'])
                        except:
                            try:
                                click(target_list['skip2'])
                            except:
                                try:
                                    if click(target_list['skip']) ==True:
                                        break
                                except:
                                    pass