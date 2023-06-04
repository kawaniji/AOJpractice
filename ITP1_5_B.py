while True:
    H,W = map(int,input().split())
    # HまたはWが0なら処理を終了
    if H == 0 and W == 0:
        break
    # 1行目を出力
    print("#"*W)
    # 2～(H-1)行目までは# + .*(W-2) +#を出力
    for i in range(H-2):
        print("#"+"."*(W-2)+"#")
    # H行目を出力
    print("#"*W)

    print()
