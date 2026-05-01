# Neural Networks — Story-Based Learning
## The Complete Mental Model for BITS Pilani's Artificial Neural Networks Course

---

> *"Every concept you will ever forget has a story that makes it unforgettable. This is that document."*

---

# PART 1: THE BIG PICTURE (Week 1)

## AI vs ML vs DL — The Three Nested Circles

**The Story:** Imagine three rooms inside a building:

- The **widest room** is **AI** — any system that **sees, decides, acts** toward a goal. A thermostat that turns on a heater when cold IS an AI system (perceive temperature → decide to heat → act). No consciousness needed.
- Inside it is **ML** — the subset where instead of programming rules by hand, you **learn the rules from data**. The thermostat doesn't get a rule like "if temp < 20°C turn on." It sees 1000 examples of (room_temp, outside_temp, season) → (heater_on/off) and figures out the pattern itself.
- Inside that is **DL** — the innermost room where you use **deep neural networks** (many layers) to learn not just the parameters, but also **the features themselves**.

**Exam Tip:** AI = perceive → decide → act toward a goal. ML = learn f(x;θ) from data. DL = learn features AND parameters jointly. Draw the nesting circles.

---

## The Biological Neuron → Artificial Neuron Bridge

**The Story:** A biological neuron has three parts:
- **Dendrites** — little antennas catching signals from other neurons
- **Soma (cell body)** — integrates all incoming signals
- **Axon** — if the combined signal is strong enough, fires an electrical pulse to the next neuron

We steal this structure for artificial neurons, but strip the biology:

| Biological | Artificial |
|------------|-----------|
| Dendrites | Input features (x₁, x₂, ...) |
| Soma | Weighted sum: w₁x₁ + w₂x₂ + ... + b |
| Axon firing | Activation function: "does output exceed threshold?" |

**The Single Neuron Equation:**
```
output = activation(w₁x₁ + w₂x₂ + ... + b)
       = activation(wᵀx + b)
```

**Exam Tip:** We keep the STRUCTURE (aggregate then decide) but replace the biology with math. That's why ANNs are useful — we can optimize them!

---

## Neuron as a Simple Feature Detector

**The Story:** Think of each neuron as a **bouncer at a club** with a specific guest list (the weights). The bouncer checks: "Does this person (input) match my list?" If yes → let them in (activate). If no → turn them away (stay silent).

The **set of weights** in a neuron IS the template/list. The input is checked against it. Strong match = strong activation.

**One neuron = one simple pattern detector.** That's why it's weak on its own — one bouncer can't run a whole club.

---

## Weights, Bias & Layers — The Assembly Line

- **Weight (w):** How much this input matters. High weight = this input is influential. Think: *importance score.*
- **Bias (b):** The threshold. "Even if the weighted sum is low, the bias says 'but start from this baseline.'" Think: *base level expectation.*
- **Layer:** A group of neurons working in parallel. Each sees the same input, each has different weights, each extracts a different feature.

**Layers are like an assembly line:**
- Layer 1 workers receive raw material (pixels) and each extracts a different simple feature (is there an edge here? a curve?)
- Layer 2 workers take those features and combine them into higher-level features (is there a corner? a texture?)
- Layer 3 workers combine those into even more abstract things (is there a nose? an eye?)
- Each layer transforms the input into a **new representation**

**Exam Tip:** Weights control influence, bias sets baseline, layers compose representations. Together they form the parametric function f(x;θ) that gets trained.

---

## Feed-Forward Architecture — The Factory Line With No Loops

**The Story:** Information flows in ONE direction — like a factory assembly line with no conveyor belt going backwards.

```
Input → Layer 1 → Layer 2 → ... → Output
```

No feedback loops. No outputs circling back to become inputs. Just: compute, pass forward, compute, pass forward.

**Why it matters:**
- Simple to understand and implement
- Gradients flow backward during training (backprop) but that's a computational path, not a data flow
- The architecture that started it all — and still the foundation of MLPs

---

# PART 2: THE MATH YOU NEED (Week 2)

## Derivatives — The Rate of Change

**The Story:** You drive from Delhi to Jaipur. Your **speed** at any moment = how fast your **position** is changing with respect to **time**. That's a derivative: `ds/dt`.

In ML: the derivative of the loss with respect to a weight tells you: **"If I nudge this weight a tiny bit, how much does the loss change?"**

- Large derivative = weight matters a lot right now
- Small derivative = weight barely affects the loss
- Negative derivative = increasing this weight would DECREASE the loss

**Partial Derivatives:** When a function has multiple inputs, you take the derivative with respect to ONE while holding the others constant. Like asking: "If I only change the steering wheel and keep the accelerator constant, how does the car's direction change?"

---

## Chain Rule — The连环 Riddle

**The Story:** You want to know: "How does the first gear turning affect how fast the last wheel spins?"

You can't directly measure it. But you CAN ask:
- "How does Gear 1 turning affect Gear 2?" × "How does Gear 2 turning affect Gear 3?" × ... × "How does Gear N turning affect the wheel?"

**The chain rule is:** `d(output)/d(first) = d(output)/d(second) × d(second)/d(third) × ... × d(last-1)/d(last)`

In a neural network, the loss depends on the output, which depends on layer L, which depends on layer L-1, ... which depends on the weights. To find how the weights affect the loss, you **multiply all the local derivatives** through the chain.

> **Chain rule = multiply your way back from loss to weights.**

---

## Gradient Vector — The Compass Pointing Downhill

**The Story:** At any point on the loss mountain, the gradient is the **direction of steepest ascent**. Flip the sign, and it's the **direction of steepest descent** — which way to take the next step.

The gradient is a **vector** because it has both:
1. **Direction** — which way is downhill
2. **Magnitude** — how steep the slope is

**Exam tip:** The gradient ∇L points in the direction of steepest ascent. The update rule `θ = θ - η∇L` goes in the opposite direction — steepest descent.

---

## Numerical Stability — The "Don't Divide by Zero" Rule

**The Story:** When you compute `x / y`, if y gets very small, x/y explodes. When you subtract two nearly equal numbers, you lose precision (the "catastrophic cancellation" problem).

In neural networks this matters because:
- During forward pass: if activations grow exponentially, you overflow (NaN)
- During backward pass: if gradients multiply many small numbers, they vanish; if they multiply many large numbers, they explode

**Solutions:**
- **Log-space computations:** instead of multiplying many small probabilities, sum their logs
- **Clipping:** prevent any value from going beyond a threshold
- **ε (epsilon) in denominator:** never divide by exactly zero

---

# PART 3: THE PERCEPTRON & ITS LIMITS (Week 3)

## Perceptron — The Line Drawer

**The Story:** A perceptron is a single neuron that draws a **straight line** (or hyperplane) to separate two classes. Everything on one side = Class A. Everything on the other = Class B.

It works like this:
1. Compute: `z = w₁x₁ + w₂x₂ + b`
2. If `z > 0` → output = 1 (Class A)
3. If `z ≤ 0` → output = 0 (Class B)

**The Learning Rule:**
- If correctly classified → do nothing
- If wrongly classified → nudge the weights: `w = w + η × (y - ŷ) × x`

That's it. It's linear classification with a binary output.

---

## Linear Separability — Can You Draw One Line?

**The Story:** Before running a perceptron, ask: *"Can I separate these two groups with one straight line?"*

- **Linearly separable:** Yes — a single straight line cleanly divides the classes. Perceptron WILL find it.
- **Not linearly separable:** No — no matter how you tilt the line, some points of each class are mixed into the other's side. Perceptron will **never** converge.

**Exam Tip:** Linear separability is a GEOMETRIC property of the data, not of the algorithm.

---

## The XOR Problem — The Problem That Killed Single-Layer AI

**The Story:** XOR is the simplest possible truth table that **cannot be solved by one straight line**:

| x₁ | x₂ | XOR |
|----|----|-----|
| 0  | 0  | 0   |
| 0  | 1  | 1   |
| 1  | 0  | 1   |
| 1  | 1  | 0   |

Plot it. The two 0s sit on **opposite corners** of the square. The two 1s sit on the **other opposite corners**. No single straight line can separate 0s from 1s.

**This broke the entire field in 1969.** Minsky showed mathematically that a single perceptron **cannot** solve XOR. The AI winter began.

**The solution (Week 3):** Multi-layer networks. Two lines can partition the XOR space:
- Line 1 separates (0,0) from (0,1) and (1,0)
- Line 2 combines them correctly

> **XOR = the problem that proved single-layer perceptrons were fundamentally limited, and that motivated hidden layers.**

---

# PART 4: ACTIVATION FUNCTIONS (Week 4)

## Why We Need Non-Linearity — The Cardboard Factory

**The Story:** Imagine stacking THREE linear transformations:

- Layer 1: z₁ = W₁x + b₁
- Layer 2: z₂ = W₂z₁ + b₂
- Layer 3: z₃ = W₃z₂ + b₃

Substitute z₂ into z₃, then z₁ into that... and you get:
```
z₃ = W₃(W₂(W₁x + b₁) + b₂) + b₃ = (W₃W₂W₁)x + (W₃W₂b₁ + W₃b₂ + b₃)
```

This is **still just ONE linear transformation** of x. Three layers, no non-linearity = just one layer. Stacking linear layers is as useful as stacking cardboard boxes.

**Activation functions BREAK the linearity.** Each layer now computes: `z = activation(Wx + b)`. Now the chain doesn't collapse because `activation()` is non-linear.

> **Without activation functions, deep networks = one linear model. With them, depth = real power.**

---

## Sigmoid — The Squash Function

**What it does:** Squashes any number to between 0 and 1.

σ(x) = 1 / (1 + e⁻ˣ)

**The Story:** Imagine a volume knob. Turn it all the way left (very negative input) → output = 0 (silence). Turn it all the way right (very positive) → output = 1 (full volume). But near the middle, small twists of the knob make a difference.

**Problems:**
- Derivative is at most 0.25 (and near extremes, nearly 0!)
- Nearly zero gradient when saturated → **vanishing gradients** (see Part 5)
- Not zero-centered (output always positive)

**When used:** Output layer for binary classification (gives probability between 0 and 1).

---

## Tanh — The Zero-Centered Sigmoid

**What it does:** Squashes any number to between -1 and 1.

tanh(x) = 2σ(2x) - 1

**Improvement over sigmoid:** Zero-centered — outputs can be positive or negative, which makes learning easier (gradients can flow in both directions).

**Still has vanishing gradient problem** (derivative ≤ 1 in fact, ≤ 0.25 near extremes).

**When used:** Hidden layers in simple networks. RNNs traditionally used tanh.

---

## ReLU — The Light Switch

**What it does:** `max(0, x)` — if negative, output 0; if positive, output x unchanged.

```
ReLU(x) = x     if x > 0
        = 0     if x ≤ 0
```

**The Story:** Like a **light switch.** Either FULLY on (positive values pass through unchanged) or FULLY off (negatives give zero). No gradual dimming.

**Why it became the default:**
- Derivative is **0 (off) or 1 (on)** — no vanishing gradients in the active region
- Computationally cheap: just a comparison, no exponentials
- Sparse activation: many neurons output 0 → efficient networks

**The dying ReLU problem:** If a neuron's weighted sum is always negative, it stays off (outputs 0) forever and never learns. Solution: Leaky ReLU (small slope for negative side).

**Leaky ReLU:** `max(0.01x, x)` — even negative inputs get a tiny non-zero signal.

---

## Softmax — The Probability分配器

**What it does:** Converts any set of numbers into **probabilities that sum to 1**.

For multi-class classification: the output layer has one neuron per class. Softmax converts their raw scores into class probabilities.

**The Story:** Imagine three candidates in an election. Their raw vote counts are (10, 5, 2). Softmax asks: "What's the probability distribution over these three, given their relative strengths?" → (0.79, 0.16, 0.05). The strongest gets the highest probability.

**Exam tip:** Used ONLY in the output layer for multi-class classification. Never in hidden layers.

---

# PART 5: BACKPROPAGATION & THE GRADIENT FLOW PROBLEM (Week 5)

## Backpropagation — The Error Signal's Journey Back Home

**The Story:** The forward pass is the **factory production line** — input comes in, each layer transforms it, output comes out.

The loss is the **customer complaint.** Backpropagation is the **quality control team** tracing the complaint BACKWARDS through every station:
- "The final product is wrong" → blame Station 3
- Station 3 says "the input from Station 2 was already off" → blame Station 2
- Station 2 says "the input from Station 1 was wrong" → blame Station 1

Each station gets a **gradient** telling it how much to adjust.

**How it works:** The chain rule applied systematically. Each layer computes `∂L/∂W = ∂L/∂output × ∂output/∂z × ∂z/∂W`.

> **Backprop = chain rule + gradient routing back through layers = how networks learn from errors.**

---

## Vanishing Gradients — The Telephone Game Gone Wrong

**The Story:** Imagine playing telephone with 20 people in a line. Person 1 whispers a message. By the time it reaches Person 20, it's barely audible — the message **faded** at each step.

In a deep network, gradients **shrink** as they flow backward through layers. Each layer multiplies by its local derivative:
- If each derivative < 1 (e.g. sigmoid derivative max = 0.25) → after 20 layers: gradient ≈ (0.25)²⁰ ≈ zero
- **Early layers stop learning** — they barely receive any error signal
- Training plateaus even though the network has capacity

**Sigmoid's contribution:** σ'(x) = σ(x)(1-σ(x)) ≤ 0.25, and near extremes σ(x)≈0 or 1, so derivative ≈ 0 → strongly encourages vanishing.

---

## Exploding Gradients — The Amplified Whispers

**The Story:** The opposite problem. Instead of fading, the message **gets louder** at each step. Person 1 whispers, Person 2 speaks it at normal volume, Person 3 shouts... by Person 20, everyone is screaming.

If weights are initialized too large, or activations amplify, derivatives > 1 → gradients grow exponentially → weights become huge → loss becomes NaN or diverges.

**The fix:** Gradient clipping (cap the gradient magnitude) and good initialization (He/Xavier).

---

## Weight Initialization — The Safe Starting Point

**The Rule:** Initialize weights carefully, not randomly to any large value.

- **Too small:** signal dies quickly → vanishing gradients
- **Too large:** signal explodes → exploding gradients
- **Just right:** gradients flow healthily for several layers

**He Initialization:** For ReLU networks: `W ~ N(0, √(2/n_in))` — keeps variance of activations stable across layers.

**Xavier Initialization:** For Sigmoid/Tanh: `W ~ N(0, √(2/(n_in + n_out)))` — balances forward and backward signal variance.

> **Good initialization = giving each layer a fighting chance at the start.**

---

# PART 6: OPTIMIZATION (Week 6)

## Gradient Descent — The Blind Hiker (Recap)

**The Story:** Already told. Blind hiker, foggy mountain, feeling downhill with feet.

Key: the **learning rate** (step size) is everything:
- Too big → overshoots the valley floor, oscillates
- Too small → takes forever

---

## Momentum — The Bowling Ball

**The Story:** A bowling ball rolling downhill builds speed. Once it's going fast, it doesn't stop at every pebble. It carries through small ridges.

In math: instead of jumping directly based on the current gradient, you accumulate **velocity**:
```
v = βv + (1-β)∇L     # β = friction, typically 0.9
θ = θ - ηv
```

The gradient becomes a **weighted average** of past gradients — smooth, consistent direction.

> **Momentum = bowling ball that builds speed, carries through bumps, escapes saddle points.**

---

## RMSProp — The Uneven Terrain Runner

**The Story:** Your left leg is on ice (gradients tiny), your right leg is on gravel (gradients huge). You need **different step sizes** for each leg.

RMSProp gives each **parameter** its own learning rate:
- Large recent gradients → effective learning rate **shrinks** (slow down on steep terrain)
- Small recent gradients → effective learning rate **grows** (speed up on flat terrain)

```
v = βv + (1-β)(∇L)²    # per-param squared gradients
θ = θ - η∇L / √(v + ε)
```

> **RMSProp = each foot finds its own step size on mixed terrain.**

---

## Adam — The Smart Runner Who Combines Both

Adam = **Adaptive Momentum + RMSProp**. It:
1. Accumulates velocity like **momentum** (smooths out zigzags)
2. Scales each parameter's step like **RMSProp** (each foot adjusts independently)

```
m = β₁m + (1-β₁)∇L          # momentum (velocity)
v = β₂v + (1-β₂)(∇L)²       # RMSProp (per-param adaptive)
θ = θ - η m / (√v + ε)
```

β₁=0.9, β₂=0.999, ε=1e-8

> **Adam = runner who builds speed AND adjusts each shoe size independently. The default optimizer for almost everything.**

---

## Learning Rate Schedules — Turning the Speed Dial

### Step Decay — The Staircase
Every N epochs, drop the learning rate (0.1 → 0.01 → 0.001). Like descending stairs. Early: big exploratory steps. Late: fine-tuning.

### Cosine Annealing — The Smooth Hill
Learning rate follows a cosine curve — smooth dip from high to low. No sudden jumps. Very popular in modern transformer training.

### Warm-up — The Soft Start
Start tiny, increase gradually over the first few epochs. For transformers and large-batch training, the first few steps can be **catastrophically unstable** — warm-up prevents this.

**The Combo:** Warm-up (2-5 epochs) → Cosine annealing. This is exactly what GPT, BERT, ResNet, and most modern architectures use.

> **Step decay = stairs. Cosine = smooth hill. Warm-up = walk before you run.**

---

## Gradient Clipping — The Brake Pedal

**The Story:** If a gradient suddenly becomes enormous (exploding), one update can destroy a model. Gradient clipping is the **brake pedal**: if the gradient is too big, scale it down but **keep the same direction**.

```
if ||g|| > threshold:
    g = (threshold / ||g||) × g  # same direction, smaller magnitude
```

**Norm clipping** (most common) preserves direction. **Value clipping** caps each component — cheaper but can distort direction.

> **Gradient clipping = brake pedal. Doesn't cure, just prevents crashes.**

---

# PART 7: REGULARIZATION (Week 7)

## Overfitting vs Underfitting — The Student's Two Failure Modes

**Underfitting (High Bias):** The student **never learned the material** — they get low training accuracy AND low test accuracy. The model is too simple (not enough capacity).

**Overfitting (High Variance):** The student **memorized the textbook** — they score 100% on training but bomb the exam. The model is too complex, fitting noise instead of signal.

**The Goldilocks zone:** Just right. Good training accuracy AND good test accuracy. This is what regularization achieves.

---

## Bias-Variance Trade-off — The Bullseye Analogy

**The Story:** Imagine throwing darts at a bullseye:
- **High bias, low variance:** You aim in the wrong direction consistently (systematic error), but your throws are tight together. Always miss the center the same way.
- **High variance, low bias:** You aim correctly but your throws are scattered all over. Sometimes you hit the target, but you're inconsistent.
- **Both low:** Your throws cluster around the bullseye. This is what you want.

Deep learning goal: reduce both bias AND variance simultaneously — which sounds impossible but regularization methods do it by constraining model complexity.

---

## L2 Regularization (Weight Decay) — The Smoothness Penalty

**What it does:** Adds `½λ∑wᵢ²` to the loss. Large weights are penalized more than small ones.

**The Story:** Imagine a referee blowing a whistle for rough play. The more aggressively a player plays (larger weights), the more they get penalized. So players moderate their intensity — many small, controlled movements rather than a few huge ones.

**Effect:** Keeps all weights small and distributed → smooth, stable predictions → better generalization.

> **L2 = discourage large weights. Think: quadratic penalty on bigness.**

---

## L1 Regularization — The Feature Selector

**What it does:** Adds `λ∑|wᵢ|` to the loss. Encourages exact zeros.

**The Story:** Same referee, but this time the penalty is linear — every player who plays aggressively gets penalized. The only way to avoid penalty is to NOT PLAY AT ALL. So players drop out entirely (weight = 0). Only the truly important players (features) stay.

**Effect:** Sparse solutions — many weights exactly zero → automatic feature selection.

> **L1 = encourage sparsity. Think: linear penalty pushes weights to zero.**

---

## Dropout — The Ghost Colleagues

**The Story:** Imagine a football team where before every play, you randomly tell 4 players to sit out. The remaining players must adapt, because any of their colleagues might be missing next time. No single player becomes too dependent on specific teammates.

During training: randomly set some activations to zero (typically 20-50%). Each iteration different "team." At test time: use ALL neurons but scale down their outputs.

**Effect:** Prevents co-adaptation (neurons that only work together). Forces each neuron to be useful on its own. Like ensemble, but within one network.

> **Dropout = train a team where any member might be absent, so everyone stays independently capable.**

---

## Batch Normalization — The Standardized Test

**The Story:** Imagine students taking exams in different cities with different grading scales. Batch normalization is like **standardizing all scores to the same scale** before the exam starts — so the difficulty is consistent everywhere.

For each mini-batch:
1. Normalize activations to mean=0, variance=1
2. Scale and shift with learned γ, β parameters

**Why it helps:**
- Reduces internal covariate shift (inputs to each layer stay stable)
- Allows higher learning rates (more stable gradients)
- Acts as a mild regularizer (noise from batch statistics)
- Enables deeper networks to train

> **Batch Norm = standardize the input to each layer so training doesn't have to relearn scale at every layer.**

---

# PART 8: CONVOLUTIONAL NEURAL NETWORKS (Week 8)

## Convolution — The Pattern Scanner

**The Story:** You have a **magnifying glass** (the filter). You slide it across an image — every position you look through the glass, you ask: "Does this little patch match the pattern I'm looking for?"

If yes → strong response. If no → weak response. You slide across the entire image, noting where the pattern appears strongly.

That's a convolution layer. The **filter** is the pattern you're looking for. The **feature map** is your answer to "where does this pattern appear?"

**Why it's powerful:**
- **Weight sharing:** One filter is reused at every position — if it detects a vertical edge in one patch, it detects it everywhere
- **Local connectivity:** Each output depends only on a small patch, not the entire image

> **Convolution = slide a pattern detector across the image, marking strong matches.**

---

## Filters Learn Patterns — The Hierarchy

**The Story:** In a trained CNN:
- **Layer 1 filters** learn simple, low-level patterns: vertical edges, horizontal edges, color blobs
- **Layer 2 filters** combine those into intermediate features: corners, textures, small shapes
- **Layer 3 filters** combine those into even more abstract: object parts (wheels, windows, eyes)
- **Layer 4+:** Full object recognition

This is the **hierarchical representation** that makes CNNs so powerful for images.

---

## Stride & Padding — The Sliding Control

**Stride:** How many pixels you slide the filter over at a time. Stride 1 = slide one pixel at a time (fine search). Stride 2 = skip every other pixel (coarser, output is smaller).

**Padding:** Adding pixels of zeros around the image border. Keeps the output size from shrinking too fast with many layers. "Same padding" ensures output size = input size.

**The Story:** If you have a big carpet and you slide the magnifying glass across it, padding is like putting a frame around the carpet so you can still scan the edges.

---

## Pooling — The Condenser

**The Story:** You can't read an entire newspaper from a single magnifier. **Pooling** is like stepping back — taking a broader view by summarizing local regions.

**Max Pooling:** In each patch, keep only the strongest signal (max value). "Was there ANY edge here? Tell me the strongest one."

**Why it works:**
- Reduces spatial size → fewer parameters → less overfitting
- Provides translation invariance (the edge can shift slightly and max pooling still catches it)
- Makes the network robust to small translations

> **Max Pooling = step back from the details, keep the maximum signal in each region.**

---

## CNN Architecture Pattern — The Full Pipeline

```
Input Image
    ↓
[Conv Layer → ReLU] → [Conv Layer → ReLU] → [Pooling]
    ↓
[Conv Layer → ReLU] → [Conv Layer → ReLU] → [Pooling]
    ↓
... (repeat)
    ↓
Fully Connected Layer(s) → Softmax Output
```

Early layers: learn low-level features (edges, textures)
Middle layers: learn intermediate features (shapes, parts)
Late layers: learn high-level features (objects)
FC layers: make the final classification decision

---

# ONE-LINE SUMMARIES — The Complete Set

> **AI** = perceive → decide → act toward a goal
> **ML** = learn f(x;θ) from data instead of programming rules
> **DL** = deep networks that learn features AND parameters jointly
> **Dendrites** → inputs, **Soma** → weighted sum, **Axon** → activation
> **One neuron** = weighted evidence aggregation = one simple pattern detector
> **Weights** = importance scores, **Bias** = baseline threshold
> **Feed-forward** = assembly line with no loops
> **Chain rule** = multiply your way back from loss to weights
> **Gradient** = direction of steepest descent (flip for ascent)
> **Sigmoid** = squash to [0,1], but vanishes near extremes
> **Tanh** = squash to [-1,1], zero-centered sigmoid
> **ReLU** = light switch: on if positive, off if negative
> **Softmax** = converts scores to probabilities summing to 1
> **No activation** = linear collapse: stacking linear layers = one linear layer
> **Backprop** = error signal traced back through every layer via chain rule
> **Vanishing gradients** = whisper down the telephone (signal fades)
> **Exploding gradients** = shout down the telephone (signal amplifies)
> **He init** = weights from N(0, √(2/n_in)) for ReLU networks
> **Momentum** = bowling ball that builds speed, carries through bumps
> **RMSProp** = each foot finds its own step size on mixed terrain
> **Adam** = smart runner with momentum AND per-parameter shoe sizes
> **Step decay** = stairs, **cosine** = smooth hill, **warm-up** = walk before you run
> **Gradient clipping** = brake pedal, doesn't cure, just prevents crashes
> **Overfitting** = memorized answers (low train error, high test error)
> **Underfitting** = never learned (high error everywhere)
> **L2** = quadratic penalty, keeps weights small and distributed
> **L1** = linear penalty, pushes weights exactly to zero (sparsity)
> **Dropout** = train while randomly removing team members
> **Batch Norm** = standardize each layer's inputs
> **Convolution** = slide a pattern detector (filter) across the image
> **Weight sharing** = one filter reused at all positions (efficient)
> **Max pooling** = step back, keep the maximum signal in each region
> **CNN pipeline** = conv-relu-pool → repeat → fully connected → softmax

---

*Last compiled: 2026-05-01*
*For BITS Pilani — Artificial Neural Networks (T2-25)*
