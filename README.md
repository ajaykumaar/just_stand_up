# Humanoid Wave RL Report 

## What you tried
The goal of this task is
1) Load a humanoid robot simulation
2) Design a wrapper for the environment to match the training software's specifications
3) Optionally, write test cases to check the wrapper and environment
4) Craft reward functions and employ reward shaping techniques
5) Train an agent to perform a hand wave using PPO or SAC
6) Validate the trained agent and optionally visualize the agent's performance

## What worked / didn’t
#### The setup
The dm_control + Mujoco combination by default doesn't leverage GPU for simulation, and running a few training steps on the CPU took a lot of time. So, I switched to Maniskill, which uses Sapien backend for GPU simulation. Also, the classic dm_control's humanoid environment was glitchy in Maniskill--- the robot sank below the floor or was floating. Fortunately, Maniskill comes with Unitree's humanoid H1's simulation with better physics. 

<img src="https://github.com/user-attachments/assets/bf24054c-3bdc-4cb3-8d66-d083937a977f" width="360"/>

Since the simulation runs on the GPU, it was possible to run the training with multiple parallel simulations. Initially, I tried recreating the dm_control/gym's reward function for the humanoid standup task. However, despite training for hours, the result was sub-optimal and the best the robot did was sitting upright. So, I've used a robot with a stationary base and controllable torso and limbs. 

#### The Wrapper
I have used two wrappers- an Observation wrapper and a Rewards wrapper. The default observation space includes the pose of surrounding objects, which are not necessary for this task. So, I have used only the joints' position and velocity and tcp pose. The reward wrapper has been used to define a 3-part reward function that does the following:
1) Rewards the robot for lifting it's right palm and moving it closer to the goal position
2) Penalize large actions
3) Incurs a penalty if the torso is not facing the forward x direction

Exponential (sharp and pointy) functions accelerated learning compared to linear reward signals. Hence, the below reward signals have been used. In the below image, Red line represents the height reward, the Green line represents the actuation penalty and the orange line represents torso orientation penalty.

<img src="https://github.com/user-attachments/assets/04d53f1e-cc06-46af-8df8-7ea4f20970c6" width="360"/>


Also, I felt incorporating a reward/penalty for the waving part of the hand motion to the existing reward signal might be a little too restrictive and may not be very different from applying a sine wave to the elbow joint after reaching the goal height. Hence, I have added the logic to apply a sine wave to perform the wave motion after the trained agent has lifted the right palm to the target position. 

## How you’d scale it up


## Tradeoffs

## Reproducibility notes
