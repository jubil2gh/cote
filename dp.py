# ver1) Pure Recursion
# def fibo(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)
# num = int(input())
# print(fibo(num))

# ver2) Memoization
# def fibo_dp(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     if memo[num] != -1:
#         return memo[num]
#     memo[num] = fibo_dp(num - 1) + fibo_dp(num - 2)
#     return memo[num]
# num = int(input())
# memo = [-1] * (num + 1)
# print(fibo_dp(num))

# ver3) Pure DP, No Recursive (Tabulation)
num = int(input())
dp = [0] * (num + 1)
dp[1] = 1
for i in range(2, num + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[num])