import sys

def input_data():
    readl = sys.stdin.readline
    loop = readl().strip()
    return loop


# 입력 받는 부분
loop = input_data()


# 코드를 작성하세요

# 처음에는 <> 를 해석한다.
def interpreter(text):
    textOrg = text[1:-1]
    print('interpreter - ', textOrg)
    loopNum = int(textOrg[0])
    loopCmdIndex = textOrg.find('<')
    print('loopCmdIndex', loopCmdIndex)
    
    if loopCmdIndex != -1:
        loopCmdEndIndex = textOrg.rindex('>')
        print('loopCmdEndIndex', loopCmdEndIndex)

        textBeforeLoop = textOrg[1:loopCmdIndex]
        print('textBeforeLoop', textBeforeLoop)
        textAfterLoop = textOrg[loopCmdEndIndex+1:]
        print('textAfterLoop', textAfterLoop)
        textLoop = interpreter(textOrg[loopCmdIndex:loopCmdEndIndex+1])
        print('textLoop', textLoop)
        return loopNum * (textBeforeLoop + textLoop + textAfterLoop)
    else:
        return loopNum * textOrg[1:]
        
    

print(interpreter(loop))
