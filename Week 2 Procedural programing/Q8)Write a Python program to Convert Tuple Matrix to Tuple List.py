test_list = [[(9, 51), (7, 9)], [(11, 1), (22, 19)]]
print("The original list is : " + str(test_list))
temp = [ele for sub in test_list for ele in sub]
res = list(zip(*temp)) 
print("The converted tuple list : " + str(res))