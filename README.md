# MCTS

This repository provides a simple implementation of MCTS in the game of tic-tac-toe of 3*3.

## Installation

With git: `git clone https://github.com/mzhhhh666/MCTS-3-3.git`

Without git: Download the zip/tar.gz file of the [latest release]([mzhhhh666/MCTS-3-3](https://github.com/mzhhhh666/MCTS-3-3))

## Quick Usage

This release has implemented

This release has implemented an example of using MCTS in tic-tac-toe, and to run the example, you can directly run `main.py`.

If you want to test mcts in other states, you can modify the following parameters:

- `current`:This parameter indicates the current game status on the board.
- `ust_constant`:It is a custom parameter in the ust algorithm
- `iterations`:It is the iteration round of mcts

```
if __name__ == '__main__':
    current=[[1,-1,0],[1,0,-1],[0,0,0]]
    init_state=state(current)
    mcts=mcts(uct_constant=1/math.sqrt(2))
    best_action,best_child=mcts.search(init_state,iterations=1000)
    print(best_action)
    print(best_child.state.state)
```

If you want to implement a custom game using MCTS,, you must implement a `State` class which can fully describe the state of the world.  It must also implement four methods:

- `get_player()`: Returns 1 if it is the maximizer player's turn to choose an action, or -1 for the minimiser player
- `get_child()`: Returns an iterable of all `actions` which can be taken from this state
- `new_state(action)`: Returns the state which results from taking action `action`
- `is_terminal()`: Returns `True` if this state is a terminal state
- `get_reward()`: Returns the reward for this state.  Only needed for terminal states.

You must also choose a hashable representation for an action as used in `get_child` and `new_state`.  

## Collaborating

Feel free to raise a new issue for any new feature or bug you've spotted. Pull requests are also welcomed if you're interested in directly improving the project.
