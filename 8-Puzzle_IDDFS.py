def dfs(src, target, limit, visited_states):
    if src == target:
        return True
    
    if limit <= 0:
        return False
    
    visited_states.append(src)
    moves = possible_moves(src, visited_states)
    for move in moves:
        if dfs(move, target, limit-1, visited_states):
            print_grid(move)
            return True
    return False



def print_grid(src):
    # print the grid state
    state = src.copy()
    state[state.index(-1)] = '_'
    print(f"""
     {state[0]} {state[1]} {state[2]}
     {state[3]} {state[4]} {state[5]}
     {state[6]} {state[7]} {state[8]}
    """)





def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    if b not in [0, 1, 2]:
        d += 'u'
    if b not in [6, 7, 8]:
        d += 'd'
    if b not in [2, 5, 8]:
        d += 'r'
    if b not in [0, 3, 6]:
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state, move, b))
    return [move for move in pos_moves if move not in visited_states]


def gen(state, move, blank):
    temp = state.copy()
    if move == 'u':
        temp[blank-3], temp[blank] = temp[blank], temp[blank-3]
    if move == 'd':
        temp[blank+3], temp[blank] = temp[blank], temp[blank+3]
    if move == 'r':
        temp[blank+1], temp[blank] = temp[blank], temp[blank+1]
    if move == 'l':
        temp[blank-1], temp[blank] = temp[blank], temp[blank-1]
    return temp


def iddfs(src, target, depth):
    for i in range(depth):
        visited_states = []
        if dfs(src, target, i+1, visited_states):
            print(True)
            return
    print(False)


src = [1,2,3,4,-1,6,7,5,8]
target = [1, 2, 3, 4, 5, 6, 7, 8, -1]

depth = 100
iddfs(src, target, depth)