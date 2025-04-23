# Humanoid Wave RL Report [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10XgLbq-KwRSSQNMlcbPUsDhMK07FGXst?usp=sharing)


## What you tried
1) Load a humanoid robot simulation
2) Design a wrapper for the environment that aligns with the training framework’s specifications.
3) (Optional) Write test cases to validate the environment and wrapper functionality.
4) Craft reward functions and apply reward shaping techniques
5) Train an agent to perform a hand wave using PPO or SAC
6) Evaluate the performance of the trained agent and optionally visualize its behavior.

## What worked / didn’t
#### The setup
The dm_control + MuJoCo combination does not leverage the GPU by default, making CPU-based simulation and training painfully slow. To address this, I switched to ManiSkill, which uses the SAPIEN backend for GPU-accelerated simulation. However, the classic dm_control humanoid environment included in ManiSkill turned out to be glitchy—the robot would either sink below the floor or float. Fortunately, ManiSkill includes Unitree’s Humanoid H1 model, which has more stable and realistic physics.

<img src="https://github.com/user-attachments/assets/bf24054c-3bdc-4cb3-8d66-d083937a977f" width="360"/>

Thanks to GPU support, I was able to run multiple parallel simulations to speed up training. Initially, I tried recreating the reward function used in the dm_control/Gym stand-up task. However, even after hours of training, the best result was the robot sitting upright, sub-optimal. To simplify, I switched to using a robot with a stationary base and controllable torso and limbs, which made it easier to focus solely on training for the hand wave.

#### The Wrapper
I implemented two wrappers: an Observation Wrapper and a Reward Wrapper. The default observation space includes poses of nearby objects, which are irrelevant for this task. So, I customized the observation space to include only the joint positions, joint velocities, and the TCP  pose.
The Reward Wrapper defines a three-part reward function:
1) Reward for lifting the right palm and moving it closer to a target goal position.
2) Penalty for large action magnitudes.
3) Penalty if the torso is not oriented along the forward X-axis.

To encourage faster and more stable learning, I used exponential reward functions instead of linear ones, which tend to be smoother. In the plot below:
The red curve represents the height reward.
The green curve is the actuation penalty.
The orange curve reflects the torso orientation penalty.

<img src="https://github.com/user-attachments/assets/04d53f1e-cc06-46af-8df8-7ea4f20970c6" width="360"/>

I initially considered incorporating a wave-motion reward (penalizing or rewarding the elbow oscillation directly), but it felt too restrictive. Instead, once the agent lifts the palm to the target height, I apply a sine wave signal to the elbow joint to generate a waving gesture.

## How you’d scale it up
1) As a next step, I would modify the default reward function in dm_control to address the current sub-optimal results. The goal is to encourage the humanoid to stand up and seamlessly incorporate the hand wave motion.
2) Hand gestures can vary significantly across individuals. To produce more natural, human-like waving behavior, it would be more effective to use imitation learning or learning from human demonstrations rather than relying solely on hand-crafted, environment-specific reward signals.

## Tradeoffs
1) The robot is currently trained to wave using only its right arm. Waving with the left arm would require additional fine-tuning or retraining.
2) The resulting motion may appear robotic, as it relies on environment-specific reward shaping and a predefined sine wave signal to trigger the wave. Using human demonstrations could lead to smoother, more natural movements that would resemble real human gestures.

## Reproducibility notes

The notebook 'humanoid_task.ipynb' contains all the code required for this task. To reproduce the results:
Execute sections [0] to [5] sequentially to:

  -  Install the necessary dependencies
  -  Load the humanoid simulation
  -  Define the environment wrappers and the Actor agent
  -  Load the pre-trained checkpoint
  -  Run the simulation and generate the output video

Section [6] contains all the training and debugging code.

Note:
The notebook will automatically restart after executing section [1]. This is expected and required for properly importing the mani_skill package in section [2].
