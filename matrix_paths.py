# Find all possible paths of a matrix from (0,0) to (m,n).
# Find the path that has max value of values of the path.

all_path = []
t_path =  []

def printAllPathsUtil(mat, i, j, m, n, path, pi):
    global all_path
    global t_path
    if (i == m - 1): 
        for k in range(j, n): 
            path[pi + k - j] = mat[i][k] 
  
        for l in range(pi + n - j):
            t_path.append(path[l])  
        
        all_path.append(t_path)
        t_path = []
        return

    if (j == n - 1): 
  
        for k in range(i, m): 
            path[pi + k - i] = mat[k][j] 
  
        for l in range(pi + m - i):
            t_path.append(path[l]) 
        
        all_path.append(t_path)
        t_path = [] 
        return
  
    
    path[pi] = mat[i][j]  
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1) 
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1) 
  
def printAllPaths(mat, m, n):  
    path = [0 for i in range(m + n)] 
    printAllPathsUtil(mat, 0, 0, m, n, path, 0) 
  
# Driver Code 
mat = [[1, 2, 3],  
       [4, 5, 6]] 
  
printAllPaths(mat, 2, 3)

t_sum = [sum(i) for i in all_path]
index = t_sum.index(max(t_sum))
listToStr = ''.join(map(str, all_path[index]))
print(listToStr)
