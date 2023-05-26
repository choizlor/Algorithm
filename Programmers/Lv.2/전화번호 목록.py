def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        num = len(phone_book[i])
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:num] == phone_book[i]:
                return False
    return True

# # 해시 방법(시간복잡도 O(1))
# # 해시를 리스트로 한다면 시간복잡도 O(n)
# def solution1(phone_book):
#     hash_map = {}
#     for number in phone_book:
#         hash_map[number] = 1
    
#     for number in phone_book:
#         jubdoo = ""
#         for num in number:
#             jubdoo += num
#             if jubdoo in hash_map and jubdoo != number:
#                 return False
#     return True