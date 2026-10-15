# Zero to Hero — Deep Learning

> A structured, first-principles learning path from mathematical foundations to modern Transformers, LLMs, and Multimodal systems.

Each module is an interactive Jupyter Notebook (`.ipynb`) built on a strict pedagogical standard:
- **Notes First:** Conversational explanations, real-world analogies, step-by-step deep dives, ASCII diagrams, and quick reference tables.
- **Code Second:** Hands-on Python, NumPy, and PyTorch implementations with clear comments and visible execution outputs.

---

## Curriculum Roadmap

```mermaid
flowchart TD
    M1["01: Introduction to DL"] --> M2["02: Mathematics for DL"]
    M2 --> M3["03: Python & Scientific Stack"]
    M3 --> M4["04: Machine Learning Foundations"]
    M4 --> M5["05: Neural Networks from Scratch"]
    M5 --> M6["06: PyTorch from Scratch"]
    M6 --> M7["07: Regularization & Training"]
    
    M7 --> M8["08: Computer Vision (CNNs)"]
    M7 --> M9["09: Sequences & RNNs"]
    
    M8 --> M10["10: The Transformer Architecture"]
    M9 --> M10
    
    M10 --> M11["11: NLP with Deep Learning"]
    M11 --> M12["12: LLMs & Fine-Tuning"]
    M10 --> M13["13: Generative Models (Diffusion, VAEs)"]
    M10 --> M14["14: Vision Transformers (ViT)"]
    M14 --> M15["15: Multimodal (Vision + Audio + Text)"]
    M12 --> M16["16: Reinforcement Learning & RLHF"]
    M16 --> M17["17: MLOps & Production Serving"]
    M17 --> M18["18: Ethics, Safety & Explainability"]
```

---

## Modules & Progress

| # | Module | Key Topics | Status / Notebook |
|:---:|---|---|:---:|
| **1** | **Introduction to Deep Learning** | What is DL, Roles & Responsibilities, Product Impact, DL vs Traditional ML | [Chapter 1](Module-01-Introduction/Chapter-01-Introduction.ipynb) |
| **2.1** | **Linear Algebra** | Scalars, Vectors, Matrices, Tensors, MatMul, Dot Products, Transpose, Inverses, Eigenvalues, L1/L2 Norms | [Chapter 2.1](Module-02-Mathematics/Chapter-2.1-Linear-Algebra.ipynb) |
| **2.2** | **Calculus & Differentiation** | Derivatives, Partial Derivatives, Chain Rule, Gradients, Steepest Descent, Autograd Graphs | [Chapter 2.2](Module-02-Mathematics/Chapter-2.2-Calculus-and-Differentiation.ipynb) |
| **2.3** | **Probability & Statistics** | Gaussian/Bernoulli/Uniform Distributions, Mean/Var/Std, Normalization, Bayes' Theorem, MLE, KL Divergence | [Chapter 2.3](Module-02-Mathematics/Chapter-2.3-Probability-and-Statistics.ipynb) |
| **2.4** | **Information Theory Basics** | Shannon Entropy, Cross-Entropy Loss, Equivalence of Cross-Entropy and Negative Log-Likelihood | [Chapter 2.4](Module-02-Mathematics/Chapter-2.4-Information-Theory-Basics.ipynb) |
| **3.1** | **NumPy for Deep Learning** | Arrays vs Python Lists, Memory Layout, Strides, Broadcasting, SIMD Vectorization, Slicing & Stacking | [Chapter 3.1](Module-03-Scientific-Stack/Chapter-3.1-NumPy.ipynb) |
| **3.2** | **Pandas for Tabular DL** | DataFrames & Series, Missing Value Imputation, GroupBy & Merging, Feature Engineering, PyTorch Export | [Chapter 3.2](Module-03-Scientific-Stack/Chapter-3.2-Pandas.ipynb) |
| **3.3** | **Matplotlib & Seaborn** | Training/Val Loss Curves, Overfitting Diagnosis, Distribution KDEs, Correlation Heatmaps, Confusion Matrices, Image Grids | [Chapter 3.3](Module-03-Scientific-Stack/Chapter-3.3-Matplotlib-and-Seaborn.ipynb) |
| **4.1** | **Core ML Concepts** | Learning Paradigms (Supervised, Unsupervised, Self-Supervised), Bias-Variance Tradeoff, Train/Val/Test Splits, K-Fold CV, Metrics (Accuracy, Precision, Recall, F1, ROC-AUC) | [Chapter 4.1](Module-04-Machine-Learning/Chapter-4.1-Core-ML-Concepts.ipynb) |
| **4.2** | **Classical Algorithms** | Baselines for DL, Linear Regression (OLS & GD), Logistic Regression, Decision Trees (Entropy & Gini), Random Forests, Gradient Boosting (XGBoost / LightGBM) | [Chapter 4.2](Module-04-Machine-Learning/Chapter-4.2-Classical-Algorithms.ipynb) |
| **4.3** | **Unsupervised Learning** | K-Means Clustering (Centroid updates & Elbow method), Principal Component Analysis (PCA, SVD, Explained Variance) | [Chapter 4.3](Module-04-Machine-Learning/Chapter-4.3-Unsupervised-Learning.ipynb) |
| **4.4** | **Feature Engineering** | Categorical Encodings (One-Hot, Target, Ordinal), Normalization vs Standardization, Handling Imbalance (SMOTE, Class Weights) | [Chapter 4.4](Module-04-Machine-Learning/Chapter-4.4-Feature-Engineering.ipynb) |
| **5.1** | **The Perceptron** | Single Neuron Biology & Math, Weighted Sums, Bias Thresholds, Heaviside Step Activation, Decision Boundaries, Linear Separability, Solving AND/OR Gates, The XOR Limitation & AI Winter, Rosenblatt's Perceptron Learning Algorithm (PLA) from Scratch | [Chapter 5.1](Module-05-Neural-Networks/Chapter-5.1-The-Perceptron.ipynb) |
| **5.2** | **Feedforward Neural Networks (MLP)** | Input/Hidden/Output Layers, Architecture Intuition, Solving XOR with 2 Layers, Universal Approximation Theorem, Forward Propagation Matrix Math ($Z = XW + b$) | [Chapter 5.2](Module-05-Neural-Networks/Chapter-5.2-Feedforward-Neural-Networks.ipynb) |
| **5.3** | **Activation Functions** | Sigmoid (Formula, Gradient, Saturation), Tanh (Zero-Centered), ReLU (Sparsity, Dead Neurons), Leaky ReLU & ELU, Modern Activations (GELU, SiLU/Swish), Decision Guide | [Chapter 5.3](Module-05-Neural-Networks/Chapter-5.3-Activation-Functions.ipynb) |
| **5.4** | **Loss Functions** | Mean Squared Error (MSE), Binary Cross-Entropy (BCE), Categorical Cross-Entropy (CCE), Softmax vs Cross-Entropy Numerical Stability, When to Use Which | [Chapter 5.4](Module-05-Neural-Networks/Chapter-5.4-Loss-Functions.ipynb) |
| **5.5** | **Backpropagation from Scratch** | Computational Graphs, Chain Rule Step-by-Step, Analytical Gradient Derivations, Manual Weight Gradient Updates, Numerical Gradient Checking ($\epsilon$-difference) | [Chapter 5.5](Module-05-Neural-Networks/Chapter-5.5-Backpropagation-from-Scratch.ipynb) |
| **5.6** | **Gradient Descent & Optimizers** | Batch vs SGD vs Mini-Batch, Momentum (Velocity vector), RMSprop (Moving average squared gradients), Adam (First & Second moments + Bias correction), Learning Rate Schedules (Cosine Annealing, Warmup), MNIST Scratch Capstone | [Chapter 5.6](Module-05-Neural-Networks/Chapter-5.6-Gradient-Descent-and-Optimizers.ipynb) |
| **6.1** | **Tensors** | 0D-4D Tensor Hierarchy, Storage & Strides, Factory Functions, Zero-Copy NumPy Bridging, Matmul (@) vs Element-wise (*), Axis Permutation, Dynamic Device Routing (CPU/CUDA/MPS), Dimension Surgery (.view vs .reshape, squeeze, unsqueeze) | [Chapter 6.1](Module-06-PyTorch-Foundations/Chapter-6.1-Tensors.ipynb) |
| **6.2** | **Autograd** | Automatic Differentiation Engine, `requires_grad`, Dynamic Computation Graph, `grad_fn`, Backward Tape, Detaching & `torch.no_grad()` | *In Progress* |
| **6.3** | **Building Networks with `nn.Module`** | `nn.Linear`, `nn.Sequential`, Custom Module Classes, `__init__` & `forward()`, Parameter Management, Layer Freezing | *Upcoming* |
| **6.4** | **Datasets and DataLoaders** | Custom `Dataset` Class, `DataLoader` Multi-Processing, Batching, Shuffling, Transforms & Normalization | *Upcoming* |
| **6.5** | **Complete Training Loop** | End-to-End Canonical Loop, Training vs Validation Modes (`model.eval()`), Metric Tracking, Checkpoint Saving & Loading | *Upcoming* |
| **7** | Regularization & Training | Dropout, Weight Decay (L1/L2), Weight Initialization (He/Xavier), BatchNorm, LR Schedules, Augmentation | *Coming soon* |
| **8** | Convolutional Networks (CNNs) | Convolutions, Kernels, Padding/Stride, Pooling, Classic CNNs (LeNet to ResNet), Skip Connections, Transfer Learning | *Coming soon* |
| **9** | Sequence Modeling & RNNs | Sequential data, RNNs, Backprop Through Time (BPTT), LSTMs, GRUs, Seq2Seq, Attention mechanism | *Coming soon* |
| **10** | The Transformer Architecture | Scaled Dot-Product Attention, Multi-Head Attention, Positional Encodings (RoPE), Full Transformer Block | *Coming soon* |
| **11** | NLP with Deep Learning | Tokenization (BPE), Word Embeddings (Word2Vec), Language Modeling, BERT vs GPT, Modern NLP tasks | *Coming soon* |
| **12** | LLMs & Fine-Tuning | Pre-training dynamics, Scaling laws, SFT, RLHF, DPO, PEFT (LoRA, QLoRA), INT8/INT4 Quantization | *Coming soon* |
| **13** | Generative Models | Autoencoders, Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion Models (DDPM) | *Coming soon* |
| **14** | Vision Transformers (ViT) | Patch embeddings, [CLS] token, ViT vs CNN trade-offs, Modern Vision Models (CLIP, DINOv2, SAM) | *Coming soon* |
| **15** | Multimodal Deep Learning | Vision-Language alignment (CLIP), Image Captioning, Vision-Language Models (VLMs), Audio & Whisper | *Coming soon* |
| **16** | Reinforcement Learning & RLHF | MDPs, Q-Learning, Deep Q-Networks (DQN), Policy Gradients, PPO, Human Preference Alignment | *Coming soon* |
| **17** | MLOps & Production Serving | Experiment tracking (W&B), Quantization & Pruning, ONNX export, FastAPI serving, Docker, vLLM | *Coming soon* |
| **18** | Ethics, Safety & Explainability | Algorithmic bias, Hallucination mitigation, Differential Privacy, Interpretability (GradCAM, SHAP) | *Coming soon* |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Aadarshttech/zero-to-hero-deep-learning.git
cd zero-to-hero-deep-learning

# Set up environment & Jupyter
pip install jupyter numpy

# Launch notebook interface
jupyter notebook
```

---

## Learning Philosophy

> **Notes first. Code second.**  
> Every concept starts with deep conceptual intuition and real-world analogies before touching code.
