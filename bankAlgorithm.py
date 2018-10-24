max = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
need = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]
available = [3,3,2]
safety_list = []
safety_list_list = []

safety_bool_list = [False,False,False,False,False]

def safety_Test(i):
    if len(safety_list) == 5:
        print(safety_list)
        return True
    if need[i][0]<=available[0] and need[i][1]<=available[1] and need[i][2]<=available[2]:
        safety_list.append(i)
        safety_bool_list[i] = True
        if len(safety_list)==5:
            print(safety_list)
            print(safety_bool_list)
            safety_list_list.append(str(safety_list));
        available[0] = available[0] + allocation[i][0]
        available[1] = available[1] + allocation[i][1]
        available[2] = available[2] + allocation[i][2]
        for j in range(len(need)):
            if j in safety_list:
                continue
            else:
                safety_Test(j)
        t = safety_list.pop()
        safety_bool_list[t] = False
        available[0] = available[0] - allocation[t][0]
        available[1] = available[1] - allocation[t][1]
        available[2] = available[2] - allocation[t][2]
    else:
        return None


def commit():
    pn = int(input('请求的编号'))
    Xa = int(input('需要a资源的数目'))
    Xb = int(input('需要b资源的数目'))
    Xc = int(input('需要c资源的数目'))
    if (Xa > (available[0])) or (Xb > available[1]) or (Xc > available[2]):
        print('超出已有资源，请求失败')
    elif Xa + allocation[pn][0] > max[pn][0] or Xb + allocation[pn][1] > max[pn][1] or Xc + allocation[pn][2] > max[pn][2] :
        print('超出资源需求，请求失败')
    else:
        need[pn][0] = need[pn][0] - Xa
        need[pn][1] = need[pn][1] - Xb
        need[pn][2] = need[pn][2] - Xc
        allocation[pn][0] = allocation[pn][0]+Xa
        allocation[pn][1] = allocation[pn][1]+Xb
        allocation[pn][2] = allocation[pn][2]+Xc
        available[0] = available[0] - Xa
        available[1] = available[1] - Xb
        available[2] = available[2] - Xc
        available2 = available[:]
        for i in range(len(need)):
            safety_Test(i)
        available[:] = available2[:]

        if len(safety_list_list):
            print(safety_list_list)
            print('请求已完成')
        else:
            need[pn][0] = need[pn][0] + Xa
            need[pn][1] = need[pn][1] + Xb
            need[pn][2] = need[pn][2] + Xc
            allocation[pn][0] = allocation[pn][0] - Xa
            allocation[pn][1] = allocation[pn][1] - Xb
            allocation[pn][2] = allocation[pn][2] - Xc
            available[0] = available[0] + Xa
            available[1] = available[1] + Xb
            available[2] = available[2] + Xc
            print('请求失败')

commit()