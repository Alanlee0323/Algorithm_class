def Merge(A:list, p:int, q:int, r:int) -> None:   #p為合併數組段的起始, q為劃分的中心點 r為合併數組段的結束  
    n1 = q - p + 1 #兩個子數組的長度  
    n2 = r - q   
    L = [0] * (n1)  #每個List中的元素都為0  
    R = [0] * (n2)  
      
    for i in range(n1):  
        L[i] = A[p + i]  
    for j in range(n2):  
        R[j] = A[q + j +1]  
  
    L.append(float('inf'))  # 添加哨兵值  
    R.append(float('inf'))  
  
    i = j = 0  
    for k in range(p, r + 1):  
        if L[i] <= R[j]:  
            A[k] = L[i]  
            i += 1   
        else:  
            A[k] = R[j]  
            j += 1  
  
def merge_sort(A, p, r):  
    if p < r:  
        q = (p + r) // 2  
        merge_sort(A, p, q)  
        merge_sort(A, q + 1, r)  
        Merge(A, p, q, r)  
  
A = [4,8,0,3,6,2]  
merge_sort(A, 0,len(A) - 1)  
print(A)  