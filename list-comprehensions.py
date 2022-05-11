'''
question - https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ## way 1 - using traditional for loop 
    list_to_print =[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != int(n):
                    list_to_print.append([i,j,k])
    # print(list_to_print) # comment as it is not expacted from program output using for loop 
    
    ## way 2 - use the list comprehension, having multiple for loop with if condition 
    list_to_print1 =[]
    list_to_print1 = [[i,j,k] for i in range(x+1)  for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != int(n)]
    print(list_to_print1)
    
"""
Input (stdin)
1
1
1
2

Your Output (stdout)
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Expected Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
