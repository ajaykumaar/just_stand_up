
import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class DummyEnv(gym.Env):
    def __init__(self):
        super(DummyEnv, self).__init__()
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(10,), dtype=np.float32)
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(4,), dtype=np.float32)

    def reset(self):
        return self.observation_space.sample()

    def step(self, action):
        obs = self.observation_space.sample()
        reward = np.random.rand()
        done = np.random.rand() > 0.95
        info = {}
        return obs, reward, done, info

def train_agent():
    env = DummyEnv()
    check_env(env)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("ppo_dummy_env")

if __name__ == "__main__":
    train_agent()
