import tkinter as tk
import pyhk
import win32api
import win32con
import win32gui
import win32process
import win32clipboard

class Bcmd():
    def __init__(self):
        self.lines = []

    def bintext(self):
        var = self.e.get()
        self.listb .insert(0,var)
        print(var)
        with open('./data/{}.txt'.format(self.res[-1].split('.')[0]),'a')as f:
            f.write('\n' + var)


    def getl(self):
        value = self.listb.get(self.listb.curselection())
        self.set_text(value)
        print(value)

    def set_text(self,string):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, string)
        win32clipboard.CloseClipboard()
        print("Set text to clipboard successfully!")

    #快捷键呼出
    def fun(self):
        point = win32api.GetCursorPos()
        hwnd = win32gui.WindowFromPoint(point)
        pid = win32process.GetWindowThreadProcessId(hwnd)
        handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid[1])
        proc_name = win32process.GetModuleFileNameEx(handle, 0)
        self.res = proc_name.split('\\')
        try:
            f = open('./data/{}.txt'.format(self.res[-1].split('.')[0]), 'r')
            self.lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
            f.close()
        except IOError:
            f = open('./data/{}.txt'.format(self.res[-1].split('.')[0]), 'w')


        self.root = tk.Tk()
        self.root.title(self.res[-1])
        self.root.geometry('300x600')

        self.e = tk.Entry(self.root)
        self.b = tk.Button(self.root, text='添加', command=self.bintext)
        self.b2 = tk.Button(self.root, text='复制', command=self.getl)
        self.listb = tk.Listbox(self.root)



        self.e.pack()
        self.b.pack()
        self.b2.pack()


        for i in self.lines:
            self.listb.insert(0, i)
        self.listb.pack()
        self.root.mainloop()


if __name__ == '__main__':
    hot = pyhk.pyhk()
    hot.addHotkey(['Ctrl', 'B'], Bcmd().fun)
    hot.start()
