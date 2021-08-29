map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

x = 2
y = 1

endx = 7
endy = 9



# 用字符串重新给地图赋值
def print_map():
    for nums in map_data:
        for num in nums:
            if num == 1:
                print(" #",end=" ")
            elif(num == 0):
                print("  ",end=" ")
            else:
                print(" $",end=" ")
        print("")

def move(juece):
    if juece == 'up':
        y = y-1
        print_map()

print_map()
move('up')