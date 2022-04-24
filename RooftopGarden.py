N = int(input())

H = []
for _ in range(N):
    H.append(int(input()))

C = [0] * N

'''way1 - timeout
sum = 0
for i in range(N):   
    for j in range(i+1,N):        
        if H[i] > H[j]:
            sum += 1
        else:
            break
'''

#way2 - stack
# 현재 건물 위치 뒤로 낮은 건물 수를 세는게 아니라 
# 현재 건물을 바라볼 수 있는 건물 수를 뽑는게 목적
s = []
#sum = 0
s.append(H[0])
'''
for i in range(0,N):
    while s:        
        if H[i] < s[-1]:
            break
        s.pop()
    #sum += s.__len__()
    C[i] = s.__len__()
    s.append(H[i])
'''     

for i, value in enumerate(H):
    while s:
        if value < s[-1]:
            break
        s.pop()
    C[i] = s.__len__()
    s.append(value)
print(sum(C))