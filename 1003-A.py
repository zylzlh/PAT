#求图上两点间的最短路径，并求最短路径上的最大权值和，如果仅一条最短路径，即为该条路径的权值和
INT_MAX=100000
mind =INT_MAX
maxw=0 #最短路径权值和的最大值
cnt=1 #最短路径条数
N,M,c1,c2=[int(x) for x in input().split(' ')]
wei=[int(x) for x in input().split(' ')]
visit=[-1]*N
#road 为列表的列表，不能用road=[tem[:]]*N，这样各行实际指向同一列表。要避免这种浅复制
#road[i][j]=INT_MAX，代表图上不存在i和j间的边
tem=[INT_MAX]*N
road=[]
for i in range(N):
    road.append(tem[:])
#读入各边的长度
for r in range(M):
    i,j,dist=[int(x) for x in input().split(' ')]
    road[i][j]=dist
    road[j][i] = dist

def dfs( p, end, dist, weit):
    global mind,cnt,maxw,N,wei,visit
    if(p==end):
        if(dist<mind):
            cnt = 1
            mind=dist
            maxw = weit
        elif(dist==mind):
            cnt+=1
            if(maxw<weit):
                maxw = weit
        return 0
    if (dist > mind): #如果该路径的长度已经超过已知的最短路径了的话，就没必要继续迭代了
        return 1
    for i in range(N):
        if(visit[i] == -1 and road[p][i] != INT_MAX):
            visit[i] = 1
            dfs(i, end, dist + road[p][i], weit + wei[i])
            visit[i] = -1
visit[c1] = 1
dfs(c1, c2, 0, wei[c1])
print (cnt, maxw)
    
