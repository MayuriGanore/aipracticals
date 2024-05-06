import sys
def all_visited(visited):
    return all(visited)
def TSP(visited,cost,path,current):
    global min_cost,ans
    if(all_visited(visited)):
        if min_cost>cost+graph[current][0]:
            min_cost=cost+graph[current][0]
            ans=path+[0]
        return
    for i in range (n):
        if not visited[i] and current!=i:
            visited[i]=True
            TSP(visited,cost+graph[current][i],path+[i],i)
            visited[i]=False
if __name__=="__main__":
    print("Enter Total No. of Vertices:")
    n=int(input())
    graph=[]

    for i in range(n):
        row=[]
        for j in range(n):
            if i!=j:
                print(f"Enter distance from node {i} to node {j}:")
                dist=int(input())
                row.append(dist)
            else:
                row.append(0)
        graph.append(row)

    min_cost=sys.maxsize
    path=[]
    visited=[False]*n
    visited[0]=True
    TSP(visited,0,[0],0)
    print("Minimum Cost:",min_cost)
    print("Path:",ans)

# Enter Total No. of Vertices:
# 4
# Enter distance from node 0 to node 1:
# 10
# Enter distance from node 0 to node 2:
# 15
# Enter distance from node 0 to node 3:
# 20
# Enter distance from node 1 to node 0:
# 10
# Enter distance from node 1 to node 2:
# 35
# Enter distance from node 1 to node 3:
# 25
# Enter distance from node 2 to node 0:
# 15
# Enter distance from node 2 to node 1:
# 35
# Enter distance from node 2 to node 3:
# 30
# Enter distance from node 3 to node 0:
# 20
# Enter distance from node 3 to node 1:
# 25
# Enter distance from node 3 to node 2:
# 30
# Minimum Cost: 80
# Path: [0, 1, 3, 2, 0]