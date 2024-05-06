def TowerOfHanoi(n,A,B,C):
    if n==1:
        print(f"Move Disk {n} from {A} to {C}")
        return
    TowerOfHanoi(n-1,A,C,B)
    print(f"Move Disk {n} from {A} to {C}")
    TowerOfHanoi(n-1,B,A,C)

if __name__=="__main__":
    print("Enter Total No. of Disks:")
    n=int(input())
    A=1
    B=2
    C=3
    TowerOfHanoi(n,A,B,C)

# Enter Total No. of Disks:
# 3 
# Move Disk 1 from 1 to 3
# Move Disk 2 from 1 to 2
# Move Disk 1 from 3 to 2
# Move Disk 3 from 1 to 3
# Move Disk 1 from 2 to 1
# Move Disk 2 from 2 to 3
# Move Disk 1 from 1 to 3