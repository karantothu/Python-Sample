# A Simple Python 3 program to count triplets with sum smaller
def countTriplets(arr, n, sum):
    # Initialize result
    ans = 0
    # Fix the first element as A[i]
    for i in range(0, n - 2):
        # Fix the second element as A[j]
        for j in range(i + 1, n - 1):
            # Now look for the third number
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] < sum):
                    ans += 1
    return ans

arr=list();
n= int(input('enter n value:'))
for i in range(0, n):
    e =input()
    arr.append(e)
sum = input('Enter Sum value:')

print(countTriplets(arr, n, sum))
