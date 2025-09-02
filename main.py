from mcts import mcts
from state import state

if __name__ == '__main__':
    current=[[1,-1,0],[1,0,-1],[0,0,0]]
    init_state=state(current)

    mcts=mcts()
    best_action,best_child=mcts.search(init_state)
    print(best_action)
    print(best_child.state.state)

