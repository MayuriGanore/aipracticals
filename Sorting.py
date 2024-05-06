def bubble_sort(A,n):
    for i in range (n):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

def selection_sort(A,n):
    for i in range(n):
        min_index=i
        for j in range (i+1,n):
            if A[min_index]>A[j]:
                min_index=j
        A[i],A[min_index]=A[min_index],A[i]

def insertion_sort(A,n):
    for i in range(1,n):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
if __name__=="__main__":
    print("Enter No Of Elements:")
    n=int(input())
    A=[]
    for i in range (n):
        print(f"Enter the {i+1} Element:")
        A.append(int(input()))
    print("Choose the Sorting Algorithm:\n1)Bubble Sort\n2)Selection Sort\n3)Insertion Sort\n")
    choice=int(input())
    if(choice==1):
        bubble_sort(A,n)
    elif(choice==2):
        selection_sort(A,n)
    elif(choice==3):
        insertion_sort(A,n)
    else:
        print("Please Choose Valid Choice!!")

    for i in range(n):
        print(A[i],end="\t")
