# n以下の自然数のうち、3の倍数もしくは3がつく数を小さいものから順に出力しなさい
n = int(input())
for i in range (1,n+1):
    if i%3 == 0 or "3" in str(i):
        print(" {}".format(i),end ="")
print()
