# Model Parallelism – Splitting the Network (Week 11 – Foundations of Distributed ML)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain when model size exceeds single GPU memory constraints
- Design strategies for partitioning neural network architectures across multiple devices
- Implement tensor parallelism for distributed execution of large layers
- Analyze pipeline parallelism for sequential layer scheduling
- Evaluate communication patterns and synchronization challenges in model parallel training

## Core Concept: When Model Exceeds Single-Device Capacity
For modern large language models (LLMs) and deep networks:
- **Parameter Scale**: Hundreds of billions of weights → requires >1TB RAM for a single copy
- **Memory Constraints**: Even 8×A100 GPUs (40GB each) cannot hold one full copy
- **Model Parallelism Necessity**: Required when model size > maximum device memory

## Partitioning Strategies

### 1. Pipeline Parallelism (Layer Partitioning)
- **Concept**: Split model layers across different devices sequentially
- **Example**: 
  - Node A: Layers 1‑10  
  - Node B: Layers 11‑20  
  - Node C: Layers 21‑30
- **Data Flow**: Input propagates sequentially through stages
- **Key Challenge**: Keeping all devices busy; avoiding pipeline stalls

### 2. Tensor Parallelism
- **Concept**: Split individual tensor operations across devices
- **Implementation**: Multiple GPUs compute matrix multiplications together
- **Parallelization Dimension**: Often uses NVIDIA Megatron-LM pattern
- **Example**: 8-way tensor parallelism distributes matrix multiplies across 8 GPUs

### 3. Hybrid Approaches
- **Common Practice**: Combine pipeline + tensor parallelism
- **Example**: 
  - 2 pipeline stages × 8 tensor parallel replicas = 16 GPUs total
  - Enables scaling to 100B+ parameter models

## Communication Patterns in Model Parallelism
- **Forward Pass Communication**: 
  - Activation data moves from one stage to the next
  - Must be carefully buffered to hide latency
- **Backward Pass Communication**: 
  - Gradients flow in reverse direction
  - Requires synchronized communication across stages
- **Key Tradeoff**: 
  - More partitions → higher communication volume
  - Larger partitions → better compute balance but more memory per device

## Pipeline Scheduling Strategies
| Strategy | Description | Idle Time | Complexity |
|----------|-------------|-----------|-----------|
| **Static Offload** | Fixed batching of layers to devices | High | Low |
| **Dynamic Chunking** | Reallocate layers based on utilization | Medium | Medium |
| **Optimized Prefetching** | Overlap computation between stages | Low | High |

## Practical Implementation Example
```python
# PyTorch Distributed Pipeline Parallel Example
import torch.distributed.alpha as dist

# Assume 3 stages across 3 devices
model.stage1 = torch.nn.Sequential(layer1, ..., layer10)
model.stage2 = torch.nn.Sequential(layer11, ..., layer20)
model.stage3 = torch.nn.Sequential(layer21, ..., layer30)

def forward_pass(input, stage):
    if stage == 1:
        output = model.stage1(input)
        dist.send(output, dst=2)  # Pass to stage 2
    elif stage == 2:
        input_from_stage1 = recv_from_prev_stage()
        output = model.stage2(input_from_stage1)
        dist.send(output, dst=3)  # Pass to stage 3
    elif stage == 3:
        input_from_stage2 = recv_from_prev_stage()
        final_output = model.stage3(input_from_stage2)
        return final_output
```

## Performance Considerations
- **Batch Size Adjustment**: Larger batches hide communication latency
- **Overlap Strategy**: Pipelining forward and backward passes
- **Stage Sizing**: Balance work across stages to minimize idle time
- **Network Topology**: Co-locate communicating stages on connected devices

## Summary
Model parallelism solves the **scale wall** that data parallelism cannot:
- Enables training of models **larger than any single device**
- Distributes computation while maintaining coherent forward/backward flows
- Introduces **new communication complexity** that requires careful orchestration
- Forms the foundation for training today’s largest LLMs and vision models

The next lesson will dive into **distributed stochastic gradient descent** – the engine that coordinates learning across these distributed model components.