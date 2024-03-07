def minesweeper(N, M, l):
    for i in range(N):
        for j in range(M):
            row, col = i + 1, j + 1
            mine_near = 0
            for mine_pos in l:
                cur_pos = (row, col)
                if mine_pos == cur_pos:
                    print("*",end=" ")
                    mine_near = 0
                    break
                elif abs(mine_pos[1] - cur_pos[1]) < 2 and abs(mine_pos[0] - cur_pos[0]) < 2:
                    mine_near += 1
            else:
                print(mine_near,end=" ")
                mine_near = 0
            
        print()
N, M, K = list(map(int, input().split()))
l = [tuple(map(int,input().split())) for i in range(K)]
minesweeper(N, M, l)

                