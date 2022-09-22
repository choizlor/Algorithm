T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    company = [arr[0], arr[1]]
    home = [arr[2], arr[3]]
    client = []
    for i in range(4, len(arr), 2):
        client.append([arr[i], arr[i+1]])

