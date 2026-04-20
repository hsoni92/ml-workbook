# Stride and Padding: Controlling Output Size - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what **stride** does during convolution.
2. Explain why **padding** is introduced.
3. Compute how stride and padding affect **feature-map size**.
4. Discuss the trade-off between **efficiency** and **spatial detail**.

---

## Why Output Size Matters

Every convolution layer changes not only the representation, but also potentially the **spatial dimensions** of the data.

If output size is not controlled carefully:

- feature maps may shrink too quickly,
- edge information may be lost,
- later layers may receive overly compressed representations.

So stride and padding are not minor details. They are key design choices in CNN architecture.

---

## What Is Stride?

**Stride** tells us how far the filter moves each time it shifts across the input.

- `stride = 1`: move one pixel at a time
- `stride = 2`: move two pixels at a time

Larger stride means the filter is applied at fewer locations. As a result:

- output feature maps become smaller,
- computation decreases,
- spatial detail is reduced.

So stride controls the **sampling density** of convolution.

---

## What Is Padding?

**Padding** adds extra values, usually zeros, around the border of the input.

Padding is introduced for two main reasons:

1. **Border handling**: without padding, edge pixels are used fewer times than central pixels.
2. **Size control**: padding can preserve spatial size or slow down how quickly it shrinks.

This is especially important in deeper CNNs where repeated shrinking could otherwise destroy useful spatial information too early.

---

## Intuition Through Examples

### Stride example

Suppose the input is `7 x 7` and the filter is `3 x 3`.

- With `stride = 1`, the filter visits many locations, so the output is relatively dense.
- With `stride = 2`, the filter skips positions, so the output becomes much smaller.

This shows the main trade-off:

- **smaller stride** -> more detailed spatial coverage
- **larger stride** -> lower compute, but coarser representation

### Padding example

Suppose the input is `3 x 3` and we use a `2 x 2` filter.

- Without padding, the output shrinks because the filter can be applied only where it fully fits.
- With padding, the input is extended at the border, so the filter can be applied more broadly and output size can be larger.

---

## Output Dimension Formula

For one spatial dimension:

`out = floor((in - kernel + 2 * padding) / stride) + 1`

For a 2D input, apply the same logic separately to **height** and **width**.

This formula matters for exams, but the intuition matters more:

- larger **kernel** tends to shrink size,
- larger **stride** shrinks size faster,
- larger **padding** helps preserve size.

---

## Same vs Valid Padding

| Mode | Meaning | Intuition |
|---|---|---|
| **Valid padding** | No padding | Output shrinks |
| **Same padding** | Padding chosen to roughly preserve size when `stride = 1` | Keeps spatial dimensions more stable |

This distinction is useful when reading CNN architectures.

---

## Design Trade-offs

| Choice | Benefit | Cost |
|---|---|---|
| Larger stride | Lower computation, faster shrinking | Loss of fine spatial detail |
| More padding | Better border treatment, shape preservation | Extra computation and more border values |
| Small stride with padding | Richer spatial information | More memory and compute |

---

## Common Confusions

- Stride can reduce spatial size **even without pooling**.
- Padding is about **border handling and output shape**, not regularization.
- In formula-based questions, do not forget the **floor** operation.

---

## Summary

- **Stride** controls how far the filter moves.
- **Padding** controls how borders are handled and helps manage output size.
- Larger stride usually means lower resolution and lower compute.
- Padding helps preserve information near the image boundaries.

**Bridge to the next note:** stride and padding control size during convolution, but CNNs also use a separate operation for downsampling and robustness: **pooling**.
