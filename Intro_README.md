## 🧠 Take-Home Project: Just Stand Up

Thank you for your interest in Tuesday Lab! This take-home exercise is meant to reflect the kind of work you'll be doing here: building ML infrastructure for robot training, training policies from scratch, and navigating ambiguous or underspecified problems.

---

### 🎯 Task

Your goal is to train a humanoid agent to **stand up from the ground** using reinforcement learning.

You are provided with:
- A Colab notebook that sets up Mujoco via `dm_control`
- A PPO starter agent that runs on a dummy Gym environment
- A partially structured codebase to help you modularize your work

Your job is to:
- Wrap the `dm_control` humanoid stand environment so it works with `stable-baselines3`
- Train a policy using PPO (or a method of your choice)
- Get the humanoid to reliably stand up
- Log your design decisions, tradeoffs, and learnings

---

### ⏱ Time Limit

Please spend no more than **6 hours total** on this project. You may break this up across multiple days.

---

### 💻 Compute Budget

You will need access to a GPU to train PPO efficiently. Please:
- Sign up for **Colab Pro+ ($49)** if you don’t already have access
- Save your receipt—we will reimburse you. We will only reimburse you for up to $49.
- If you’re unable to use Colab, let us know and we’ll provide alternative access

---

### 📦 What to Submit

- A GitHub repo containing:
  - Your code
  - A completed version of `report_template.md`
  - Optional: test coverage (you’ll find a few starter tests in `tests/`)
- A link to your Colab notebook or a brief demo video (optional)

---

### 🧪 Evaluation Criteria

We are **not** evaluating this based on final reward alone. Instead, we are looking for:

| Category                  | What We're Looking For                                           |
|---------------------------|------------------------------------------------------------------|
| 🚀 Execution speed        | Can you get something working in limited time?                   |
| 🌫️ Comfort with ambiguity | Did you make reasonable assumptions when things were underspecified? |
| 📦 Reproducibility        | Can we run your code and get similar results?                    |
| 🧱 Code quality           | Clear structure, modularity, no duplication                      |
| 🧪 Test coverage          | Bonus: meaningful unit tests                                     |
| 🧠 Reward shaping         | Did you explore techniques to make learning easier?              |
| 🗣️ Communication          | Did you clearly explain what you tried and why?                  |

---
