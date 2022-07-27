# n, k = map(int, input().split())
# test_lst = [] # 최종 검사할 list
# data = [] # 기본 list 값
# data_2 = [[0] * n for _ in range(n)] # 2차원 리스트 값
# sumV = 0

# # 리스트 만들어주기
# for i in range(n):
#     data.append(list(map(str, input().split())))
#     for j in range(n):
#         data_2[j][i] = data[i][j]

# # test_lst에 '111' 값 만들어주기
# for i in range(n):
#     test_lst.append(''.join(data[i]).split('0'))
#     test_lst.append(''.join(data_2[i]).split('0'))

# # 연속 '111' 값 찾아서 출력
# for i in range(n * 2):    
#     if '1' * k in test_lst[i]:
#         sumV += 1
# print(sumV)

print(type('str'))