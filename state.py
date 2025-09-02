import copy

class state:
    def __init__(self,state=[[0,0,0],[0,0,0],[0,0,0]],player=1):
        self.state = state
        self.player = player
        self.actions = self.get_child()
        self.terminal = self.is_terminal()

    def get_child(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    children.append([i,j])
        return children

    def new_state(self, action):
        new_state = state()
        new_state.state = copy.deepcopy(self.state)
        new_state.state[action[0]][action[1]] = self.player
        new_state.player = -self.player
        new_state.actions = new_state.get_child()
        new_state.terminal = new_state.is_terminal()

        return new_state

    def is_terminal(self):
        for row in self.state:
            if abs(sum(row)) == 3:
                return True
        for i in range(3):
            if abs(sum([self.state[j][i] for j in range(3)])) == 3:
                return True
        if abs(sum([self.state[i][i] for i in range(3)])) == 3:
            return True
        if abs(sum([self.state[i][2-i] for i in range(3)])) == 3:
            return True
        for row in self.state:
            if 0 in row:
                return False
        return True


    def get_reward(self):
        for row in self.state:
            if abs(sum(row)) == 3:
                return sum(row)/3
        for i in range(3):
            if abs(sum([self.state[j][i] for j in range(3)])) == 3:
                return sum([self.state[j][i] for j in range(3)])/3
        if abs(sum([self.state[i][i] for i in range(3)])) == 3:
            return sum([self.state[i][i] for i in range(3)])/3
        if abs(sum([self.state[i][2-i] for i in range(3)])) == 3:
            return sum([self.state[i][2-i] for i in range(3)])/3
        if 0 not in self.state:
            return 0

    def get_player(self):
        return self.player






