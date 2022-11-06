# problem url - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    nested_list = []
    score_ = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
        score_.append(score)
    nested_list.sort() # to sort the names when we have mutiple name with second lowest
    # print("Full list: ", nested_list)
    
    score_=sorted(set(score_)) # use index 1 to get the second lowest score from the list
    # print("Score: ",score_)
    
    for i in nested_list:
        # print("==> ", i[1],score_[1])
        if i[1] == score_[1]:
            print(i[0])
            
    # dic = {}
    # count = 1
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     if name in dic.items:
    #     # if dic["std_name"] == name:
    #         dic["occurance"]+=count
    #     else:
    #         dic = {"std_name": name, "std_score" : score,
    #         "occurance" : count}
    # print("output: ",dic)
    # print("output2: ",dic["occurance"]+count)
    
