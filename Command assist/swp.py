import time,pyhk,keybd,threading
def main():
    global flage
    if flage == 0:
        flage = 1
        t1 = threading.Thread(target=s1,args=())
        t1.start()
    else:
        flage = 0

def s1():
    while flage == 1:
        time.sleep(0.08)
        if flage == 0:
            break
        keybd.key_press('0')

if __name__ == '__main__':
    flage = 0
    hot = pyhk.pyhk()
    hot.addHotkey(['Ctrl','Z'], main)
    hot.start()
