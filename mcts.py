import math
import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.rewards = 0
        self.is_expanded = False


class mcts:
    def __init__(self, uct_constant=1/math.sqrt(2)):

        self.uct_constant = uct_constant
        self.rollout = self.rollout_random


    def search(self,init_state,iterations=1000):
        self.root=Node(init_state)

        for i in range(iterations):
            node = self.select(self.root)
            reward = self.rollout(node)
            self.backpropagate(node, reward)
        
        best_action,best_child=self.best_child(self.root)
        return best_action,best_child

    def rollout_random(self, node):
        while not node.state.terminal:
            children=node.state.get_child()
            action=random.choice(children)
            node=Node(node.state.new_state(action),node)

        return node.state.get_reward()

    def select(self, node):
        while not node.state.terminal:
            if not node.is_expanded:
                node = self.expand(node)
                return node
            else:
                action,node = self.best_child(node)
        return node


    def expand(self, node):
        actions = node.state.get_child()
        for action in actions:
            # Convert action (list) to a tuple to make it hashable
            action_tuple = tuple(action)
            if action_tuple not in node.children:
                child_node = Node(node.state.new_state(action), node)
                node.children[action_tuple]=child_node
                if len(node.children) == len(actions):
                    node.is_expanded = True
                return child_node

    def best_child(self,node):
        best_action=None
        best_value=-float('inf')
        for action,child_node in node.children.items():
            value=child_node.rewards/child_node.visits+self.uct_constant*math.sqrt(math.log(node.visits)/child_node.visits)
            if value>best_value:
                best_value=value
                best_action=action
            elif value==best_value:
                if random.random()<0.5:
                    best_action=action
        return best_action,node.children[best_action]
                    
    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.rewards += reward
            node = node.parent

