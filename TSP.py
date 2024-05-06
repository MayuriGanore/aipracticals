import sys

def all_visited(visited):
    return all(visited)

def TSP(cost,current,visited,path):
    global min_cost,ans
    if(all_visited(visited)):
        if(min_cost>cost+graph[current][0]):
            min_cost=cost+graph[current][0]
            ans=path+[0]
        return 
    for i in range (n):
        if not visited[i] and current!=i:
            visited[i]=True
            TSP(cost+graph[current][i],i,visited,path+[i])
            visited[i]=False

if __name__=="__main__":
    print("Enter the Total No. Of Vertices:")
    n=int(input())
    graph=[]

    for i in range (n):
        row=[]
        for j in range (n):
            if(i!=j):
                print(f"Enter the Value Of Distance Between {i} to {j}:")
                dist=int(input())
                row.append(dist)
            else:
                row.append(0)
        graph.append(row)

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end="\t")
        print()

    path=[]
    visited=n*[False]
    visited[0]=True
    min_cost=sys.maxsize

    TSP(0,0,visited,[0])
    print("Shortest Path:",ans)
    print("Cost:",min_cost)

# Enter the Total No. Of Vertices:
# 4
# Enter the Value Of Distance Between 0 to 1:
# 10
# Enter the Value Of Distance Between 0 to 2:
# 15
# Enter the Value Of Distance Between 0 to 3:
# 20
# Enter the Value Of Distance Between 1 to 0:
# 10
# Enter the Value Of Distance Between 1 to 2:
# 35
# Enter the Value Of Distance Between 1 to 3:
# 25
# Enter the Value Of Distance Between 2 to 0:
# 15
# Enter the Value Of Distance Between 2 to 1:
# 35
# Enter the Value Of Distance Between 2 to 3:
# 30
# Enter the Value Of Distance Between 3 to 0:
# 20
# Enter the Value Of Distance Between 3 to 1:
# 25
# Enter the Value Of Distance Between 3 to 2:
# 30
# 0       10      15      20
# 10      0       35      25
# 15      35      0       30
# 20      25      30      0
# Shortest Path: [0, 1, 3, 2, 0]
# Cost: 80
