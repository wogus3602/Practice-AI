# Deterministic : 방향키를 누른데로 움직이는 상태 
# Stochastic : 방향키를 눌러도 움직이지 않는 상태

import gym
from gym.envs.registration import register
import readchar

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

arrow_keys = {
    'w' : UP,
    's' : DOWN,
    'd' : RIGHT,
    'a' : LEFT
}

# register(
#     id='FrozenLake-v3',
#     entry_point='gym.envs.toy_text:FrozenLakeEnv',
#     kwargs={'map_name' : '4x4', 'is_slippery': True}
# )

env = gym.make('FrozenLake-v0') # 미끄러움이 있음

env.reset()


env.render()

while True:
    key = readchar.readkey()
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break