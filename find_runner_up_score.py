# if-else statement ==========================
# n = int(input("Enter Value: ").strip())
# if (n % 2 != 0):
#     print("Weird")

# if n in range(2, 6) and n % 2 == 0:
#     print("Not Weird")

# if n in range(6, 21) and n % 2 == 0:
#     print("Weird")

# if n > 20 and n % 2 == 0:
#     print("Not Weird")









n = int(input())
    arr = map(int, input().split())
    
    sorted_arr = sorted(set(arr))
    print(sorted_arr[-2])
