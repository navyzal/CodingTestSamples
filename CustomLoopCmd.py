import sys

def input_data():
    readl = sys.stdin.readline
    loop = readl().strip()
    return loop


# 입력 받는 부분
loop = input_data()


# 코드를 작성하세요

# 처음에는 <> 를 해석한다.
# <1 후 아것도 없는 에러 처리 필요
# interpreter -  1><1 에러.. 다시 풀자.

#def interpreter(text):
def interpreter(textOrg):
    #textOrg = text[1:-1]
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
        #textLoop = interpreter(textOrg[loopCmdIndex:loopCmdEndIndex+1])
        textLoop = interpreter(textOrg[loopCmdIndex+1:loopCmdEndIndex])
        print('textLoop', textLoop)
        return loopNum * (textBeforeLoop + textLoop + textAfterLoop)
    else:
        return loopNum * textOrg[1:]
        
    

print(interpreter(loop[1:-1]))
#test = '<1A<1>>'
#print(test[1:-1])

