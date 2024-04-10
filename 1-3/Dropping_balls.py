import sys

#nballs 為第幾顆球
#dep為數的深度
#pos為根節點

def Dropping_balls(dep, nballs):             
    pos = 1  

    for j in range(dep - 1):
        if nballs % 2 == 0:                  # 如果球的編號是偶數，則球向右移動；如果是奇數，則向左移動。
            pos = pos * 2 + 1                # 當球向右移動時，我們更新球的位置，如果當前節點的位置是 pos，則其右子節點的位置是 2 * pos + 1
            nballs = nballs // 2             # 當球向右移動後，我們需要更新球的編號
        else:                                # 如果球的編號是偶數，則球向右移動；如果是奇數，則向左移動。
            pos = pos * 2  # Go left
            nballs = (nballs + 1) // 2 

    return pos 

while True:
# 讀取直到EOF的輸入
    input_line = (input().strip())

    if input_line == '-1':  # 如果讀取到-1，跳出循環。
        break

    else:
        cases = int(input_line)
        results = []
        for case in range(cases):
            line = input()
            param1, param2 = map(int, line.split())   #line.split將輸入進來的文字按照空格分割成list，再由 map 函式讀取列表逐個轉換為 int
            pos = Dropping_balls(param1, param2)
            results.append(pos)
        for result in results:
            print(result)
        
