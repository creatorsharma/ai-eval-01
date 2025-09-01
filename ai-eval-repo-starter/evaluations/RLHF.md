1. Definition

Reinforcement Learning from Human Feedback (RLHF) is a machine learning technique where AI models are trained not only on raw data but also on human preferences and judgments. Instead of just predicting the next word or output, the AI learns what humans consider good, safe, and useful responses.

It combines:

Supervised learning → where the model first learns from human-annotated examples.

Reinforcement learning (RL) → where the model improves through rewards based on human or evaluator feedback.

2. Process Step by Step
   
(a) Pretraining

A base model (like GPT) is trained on huge text data.
At this stage, the model knows “language patterns” but not what humans prefer.

(b) Supervised Fine-Tuning (SFT)

Human labelers provide high-quality demonstrations (e.g., correct answers, helpful replies).
Model is fine-tuned to mimic these demonstrations.

(c) Reward Model Training

Humans compare two or more model responses to the same prompt.

Example:

Prompt: “Explain quantum physics simply.”

Response A: Uses heavy jargon, not easy.

Response B: Uses simple analogy, easy to grasp.

Human picks Response B.

A reward model learns to predict which answer humans prefer.

(d) Reinforcement Learning (PPO, etc.)

The main AI model generates outputs.

The reward model scores them.

Using algorithms like Proximal Policy Optimization (PPO), the model is updated to maximize human-preferred responses.



3. Example in Practice

Imagine training a chatbot like ChatGPT:

Prompt: “Tell me about the French Revolution in 3 points.”

Bad Output: Long essay, ignores “3 points.”

Better Output:

End of monarchy under Louis XVI.

Rise of radical political groups.

Declaration of human rights & republic.

Humans reward the second response.

Over thousands of such comparisons, the model learns to:

Follow instructions

Be factually correct

Stay safe & aligned with human expectations

4. Why Rubrics-Based Evaluation Fits into RLHF

Rubrics (like Instruction Following, Truthfulness, Contextual Awareness, etc.) are the criteria humans use when giving feedback.

Example:

If model ignores instruction, it’s a Minor/Major issue.

If model is factually wrong, it’s a Truthfulness issue.

By scoring responses this way, evaluators supply structured feedback → which is exactly what the reward model needs in RLHF.
