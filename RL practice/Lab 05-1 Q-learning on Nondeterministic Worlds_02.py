# Deterministic : 방향키를 누른데로 움직이는 상태 
# Stochastic : 방향키를 눌러도 움직이지 않는 상태

import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0') # 미끄러움이 있음

Q = np.zeros([env.observation_space.n,env.action_space.n])

learning_rate = .85
dis = .99
num_episodes = 2000

rList = []

for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    e = 1. / ((i // 100) + 1)

    while not done:
        action = np.argmax(Q[state, :] + np.random.randn(1,env.action_space.n) / (i+1))


        new_state, reward, done, _ = env.step(action)

        Q[state,action] = (1-learning_rate) * Q[state,action] + learning_rate*(reward + dis * np.max(Q[new_state, :]))

        rAll += reward
        state = new_state

    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)
plt.bar(range(len(rList)),rList,color="blue")
plt.show()