A = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

B = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

C = [["1","2",".",".",".",".","6",".","7"],
    [".",".",".",".",".",".",".",".","5"],
    [".",".","9",".","6",".","4",".","."],
    [".","6",".",".",".",".",".",".","."],
    [".",".",".",".","4",".",".","7","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","2"],
    [".","9",".",".",".",".",".",".","7"]]
board = C
def check(M):
    while '.' in M:
        M.remove('.')
    if len(M) != len(set(M)):
        return False
    else:
        return True

for ln in board:
    temp  = ln[:]
    res = check(temp)
    if res == False:
        print('haha')
        # return False

for i in range(9):
    temp = [ln[i] for ln in board]
    print(temp)
    res = check(temp)
    if res == False:
        print('heihei')
        # return False

for i_start in [0,3,6]:
    for j_start in [0,3,6]:
        temp = []
        for i in range(3):
            for j in range(3):
                # print(i_start+i)
                # print(j_start+j)
                temp.append(board[i_start+i][j_start+j])
        res = check(temp)
        if res == False:
            print('wawa')
            # return False




