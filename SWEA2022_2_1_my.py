from queue import PriorityQueue

class player:
    def __init__(self, idx, x, y, d, s):
        self.idx = idx
        self.c = x
        self.r = y
        self.d = d
        self.s = s
        self.gun = None
        self.score = 0
      
    def move(self, loser = False):
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        if not loser:
            nr = self.r + dr[self.d]
            nc = self.c + dc[self.d]
            if 0 <= nr < n and 0 <= nc < n:
                self.r = nr 
                self.c = nc
            else:
                self.d = (self.d + 2) % 4
                nr = self.r + dr[self.d]
                nc = self.c + dc[self.d]
                self.r = nr
                self.c = nc
        else:
            for i in range(4):
                r, c = self.r, self.c
                nd = (self.d+i) % 4
                nr = r + dr[nd]
                nc = c + dc[nd]
                if 0 <= nr < n and 0 <= nc < n and check(nr, nc, self.idx) is None:
                    self.r = nr 
                    self.c = nc
                    self.d = nd

    def drop_gun(self):
        global grid
        if self.gun is None:
            return
        else:
            grid[self.r][self.c].put(self.gun)
            self.gun = None
            return
    
    def pick_gun(self):
        global grid
        if grid[self.r][self.c].qsize() != 0:
            self.gun = grid[self.r][self.c].get()
        return

    def print_ability(self):
        print(f"player id:{self.idx}, position:({self.r},{self.c}), ability: {self.s}, gun: {self.gun}, score: {self.score}.")

# check there is someone else.
def check(r, c, j):
    for i in range(m):
        if i != j:
            if players[i].r == r and players[i].c == c:
                return i
    return None

# fight player a and player b
def fight(a, b):
    global players
    winner = None
    loser = None
    if players[a].gun is not None:
        ability_a = players[a].s - players[a].gun
    else:
        ability_a = players[a].s
    
    if players[b].gun is not None:
        ability_b = players[b].s - players[b].gun
    else:
        ability_b = players[b].s
    
    # player a is powerful than b
    if ability_a > ability_b:
        players[a].score += ability_a - ability_b
        winner = a
        loser = b
    # player b is powerful than a
    elif ability_a < ability_b:
        players[b].score += ability_b - ability_a
        winner = b
        loser = a
    # player a and b has same power
    else:
        if players[a].s > players[b].s:
            winner = a
            loser = b
        else:
            winner = b
            loser = a
    return winner, loser



if __name__ == '__main__':
    # get input
    n, m, k = map(int, input().split())
    
    # get grid
    grid = []
    for _ in range(n):
        tmp = []
        for g in list(map(int, input().split())):
            que = PriorityQueue()
            if g > 0:
                que.put(g*(-1))
            tmp.append(que)
        grid.append(tmp)
    
    # get player
    players = []
    for idx in range(m):
        x, y, d, s = map(int, input().split())
        players.append(player(idx, y-1, x-1, d, s))

    # round
    for _ in range(k):
        for j in range(m):
            # print(f"--START PLAYER {j}--")
            # players[j].print_ability()
            # j 번째 player 게임 시작.
            # 1-1 move
            # print(f"{j} move", end="\n")
            players[j].move()
            # players[j].print_ability()

            # 2-1-1 Fight or Chill
            j2 = check(players[j].r, players[j].c, j)
            if j2 is None:
                # print(f"{j} chill", end="\n")
                # 2-1-2 Chill: drop gun / pick gun
                if grid[players[j].r][players[j].c].qsize() == 0:
                    continue
                else:
                    players[j].drop_gun()
                    players[j].pick_gun()
                # players[j].print_ability()
            else:
                # 2-2-1 Fight
                # print(f"{j} fight with {j2}")
                winner, loser = fight(j, j2) 

                # 2-2-2 loser moves
                players[loser].drop_gun()
                players[loser].move(loser=True)
                players[loser].pick_gun()
                # print(f"{loser} loses", end = "\n")
                # players[loser].print_ability()

                # 2-2-3 winer pick up guns
                players[winner].drop_gun()
                players[winner].pick_gun()
                # print(f"{winner} wins", end = "\n")
                # players[winner].print_ability()
    for idx in range(m): print(players[idx].score, end=" ")
