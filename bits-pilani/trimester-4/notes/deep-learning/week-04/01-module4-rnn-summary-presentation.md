# Recurrent Neural Networks

## Why Sequence Models Exist

Text, speech, time series, and video get their meaning from order. A static model ignores that: the word "bank" depends on the words around it, and a sound only makes sense in time.

A plain feedforward net has a fixed input size, no memory of earlier inputs, and no weight sharing across positions. An RNN adds a feedback loop. The hidden state $h_t$ carries history forward.

One shared weight matrix is applied at every step, so the same model accepts a sequence of any length.

| Pattern | What it does | Examples |
| --- | --- | --- |
| Sequence to vector | Compresses a whole sequence into one vector. | Sentiment, topic classification. |
| Vector to sequence | Expands one vector into a sequence. | Text generation, image captions. |
| Sequence to sequence | Maps one sequence onto another. | Translation, summarization. |

The line of models is MLP, then RNN, then LSTM, then Transformer.

## Hidden State and Unrolling

The hidden state is a vector summary of everything seen so far. The update mixes the new input with the previous state:

$h_t = f(W \cdot h_{t-1} + U \cdot x_t)$

Unrolling draws the loop as a chain of identical steps, which is the graph that training differentiates. Three matrices are shared at every step:

| Matrix | Role |
| --- | --- |
| $W$ | Previous state to next state (memory). |
| $U$ | Input to state. |
| $V$ | State to output. |

Because $W$, $U$, and $V$ do not grow with length, model size stays fixed for any sequence.

## Backpropagation Through Time

BPTT unrolls the loop for $T$ steps and runs ordinary backpropagation on that chain. The gradient for a shared matrix such as $W$ is the sum of its gradients at every step. Since $h_t$ depends on $h_{t-1}$, that sum contains a long product of derivatives. Memory grows linearly with $T$, because every intermediate state is kept.

| Failure | Condition | Result |
| --- | --- | --- |
| Exploding gradients | Spectral radius of $W$ is greater than $1$. | Values grow exponentially and training diverges. |
| Vanishing gradients | Spectral radius of $W$ is less than $1$. | Early signals die, and long-range dependencies are not learned. |

Fixes:

- **Gradient clipping** rescales the gradient when its norm exceeds a threshold $\tau$, typically between $1$ and $5$. The direction is unchanged.
- **Truncated BPTT** runs the forward pass over the full sequence and the backward pass for only $k$ steps, with $k$ often from about $20$ to $200$. Dependencies longer than $k$ steps are not learned.

## LSTM

A plain RNN stores all context in one hidden vector, so early information fades. The cell state is a separate memory path across time, guarded by gates, so a fact can survive for hundreds of steps.

| Gate | What it does |
| --- | --- |
| Forget | A sigmoid chooses what to erase from the previous cell state $C_{t-1}$. Output near $0$ drops it; output near $1$ keeps it. |
| Input | A tanh unit proposes new candidate values. A sigmoid chooses what to write. |
| Output | A sigmoid and a tanh filter the cell state into the hidden state $h_t$. |

The cell update is additive. Gradients are not forced through a long product of multiplications, so they do not decay exponentially. LSTMs are used in language, time-series forecasting, and speech.

## GRU and Bidirectional RNNs

A vanilla RNN's useful memory is on the order of about $10$ steps. The GRU (Cho et al., 2014) uses two gates and is simpler than an LSTM, with similar accuracy on many tasks.

- The **update gate** $z$ sets how much of the past state to carry forward. $z \approx 1$ keeps the memory. $z \approx 0$ resets it.
- The **reset gate** $r$ sets how much past context is used to build the new candidate state.
- The candidate state mixes the current input with that gated history.

A **bidirectional** RNN runs one pass from $1$ to $T$ and another from $T$ to $1$, then combines them. It needs the full sequence before it can start, so it is not for real-time prediction. A BiGRU is that pattern with the GRU's smaller parameter count. Uses include translation, named entity recognition, and speech recognition.

## Sequence-to-Sequence and Attention

An encoder-decoder maps a source sequence to a target sequence whose length can differ, as in translation.

- The encoder reads tokens one by one. Its final hidden state is the context vector.
- The decoder starts from that vector and emits tokens until an end token, feeding each output back in.
- The fixed vector is a bottleneck. Quality drops once the source is longer than roughly $20$ tokens.

Attention replaces that single summary. For each output step the decoder builds a fresh context $c_t$:

1. Score how relevant each encoder state $h_i$ is to the current decoder state $s_t$.
2. Softmax turns those scores into weights.
3. $c_t$ is the weighted sum, so the decoder reads the source positions that matter for this token.

The alignment is trained with the rest of the network. This mechanism is the step that leads to the Transformer.

## Applications

- **Sentiment** is many-to-one: the final state $h_t$ is classified as positive, negative, or neutral.
- **Text generation** is many-to-many and autoregressive: each predicted token is the next input.
- **Forecasting** uses the same recurrence for prices, hourly load, and climate series. Long series need LSTM or GRU, because a vanilla RNN loses the early signal.
- The practical split: LSTM gates (input, forget, output) store information over long spans. GRU gates (update, reset) train faster at similar quality.

---

**← [Previous](../week-03/01-module3-cnn-architectures-yolo-summary-presentation.md) · [Index](../README.md) · [Next](../week-05/01-module5-transformers-i-summary-presentation.md) →**
