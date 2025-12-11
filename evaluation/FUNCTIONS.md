# Drift Detection Functions

This document contains simple, practical implementations of drift detection functions. Each function is designed to be easy to understand, implement, and extend.

---

## 1. Behavioral Check

**Purpose**: Detect changes in model behavior, style, tone, and response patterns using semantic similarity.

**What it checks**:
- Semantic similarity between baseline and current responses
- Behavioral consistency using embeddings

### Implementation

```python
import numpy as np
from typing import Dict


def get_embedding(text: str) -> np.ndarray:
    """
    Get semantic embedding for text.
    
    In production, use sentence-transformers:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text)
    
    For demo, returns mock embedding.
    """
    # Mock embedding - replace with real implementation
    np.random.seed(hash(text) % 2**32)
    return np.random.rand(384)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two vectors"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def check_behavioral_drift(
    baseline_response: str,
    current_response: str,
    similarity_threshold: float = 0.85
) -> Dict:
    """
    Detect behavioral drift using semantic similarity.
    
    Args:
        baseline_response: Response from baseline model
        current_response: Response from current model
        similarity_threshold: Minimum similarity to consider no drift (0-1)
    
    Returns:
        Dict with drift detection results
    """
    # Get semantic embeddings
    baseline_embedding = get_embedding(baseline_response)
    current_embedding = get_embedding(current_response)
    
    # Calculate semantic similarity
    similarity = cosine_similarity(baseline_embedding, current_embedding)
    
    # Detect drift if similarity is below threshold
    drift_detected = similarity < similarity_threshold
    
    return {
        'drift_detected': drift_detected,
        'similarity_score': float(similarity),
        'similarity_threshold': similarity_threshold,
        'baseline_response': baseline_response,
        'current_response': current_response
    }


# Example usage
if __name__ == "__main__":
    # Example 1: Behavioral drift detected
    baseline = "I would be happy to assist you with your request. Please provide more details."
    current = "Yeah, I can help. What do you need?"
    
    result = check_behavioral_drift(baseline, current, similarity_threshold=0.85)
    print("Example 1 - Behavioral Drift:")
    print(f"Similarity: {result['similarity_score']:.3f}")
    print(f"Drift detected: {result['drift_detected']}")
    print()
    
    # Example 2: No drift (similar meaning, different wording)
    baseline = "Thank you for your inquiry. I'll be happy to help."
    current = "Thank you for your question. I would be pleased to assist you."
    
    result = check_behavioral_drift(baseline, current, similarity_threshold=0.85)
    print("Example 2 - No Drift:")
    print(f"Similarity: {result['similarity_score']:.3f}")
    print(f"Drift detected: {result['drift_detected']}")
    print()
    
    # Example 3: Different behavior
    baseline = "Our refund policy allows returns within 30 days of purchase."
    current = "You can return stuff. Just bring it back whenever."
    
    result = check_behavioral_drift(baseline, current, similarity_threshold=0.85)
    print("Example 3 - Different Behavior:")
    print(f"Similarity: {result['similarity_score']:.3f}")
    print(f"Drift detected: {result['drift_detected']}")
```

### Usage in Drift Detection

```python
from behavioral_check import check_behavioral_drift

# Compare baseline vs current
baseline_response = baseline_model(question)
current_response = current_model(question)

result = check_behavioral_drift(
    baseline_response, 
    current_response,
    similarity_threshold=0.85  # 85% similarity threshold
)

if result['drift_detected']:
    print(f"⚠️ Behavioral drift detected!")
    print(f"Similarity: {result['similarity_score']:.3f}")
    # Log or alert
```

### Key Features

1. **Simple**: Just one function, easy to understand
2. **Semantic**: Uses embeddings to capture meaning, not just words
3. **Flexible**: Works with any text comparison
4. **Configurable**: Adjust threshold based on your needs

### Configuration

- `similarity_threshold`: Minimum similarity to avoid drift detection (0.0-1.0, default 0.85)
  - Higher (0.9-0.95) = stricter (detects small changes)
  - Lower (0.7-0.8) = more lenient (only major changes)
  - Recommended: 0.85 for most use cases

### Production Setup

Replace the mock `get_embedding` function with:

```python
from sentence_transformers import SentenceTransformer

# Initialize once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> np.ndarray:
    """Get real semantic embedding"""
    return model.encode(text)
```

---

## 2. Tone Detection

**Purpose**: Detect the tone of text using semantic similarity to reference examples.

**What it checks**:
- Tone classification (formal, casual, polite, professional, etc.)
- Tone drift between baseline and current responses
- Semantic tone matching (not keyword-based)

### Implementation

```python
import numpy as np
from typing import Dict, List
from sentence_transformers import SentenceTransformer

# Initialize model once (reuse across calls)
# model = SentenceTransformer('all-MiniLM-L6-v2')

# Define tone reference examples
TONE_REFERENCES = {
    'formal': [
        "I would be pleased to assist you with your inquiry.",
        "Thank you for contacting us. We appreciate your business.",
        "I respectfully request your attention to this matter.",
        "We would be grateful if you could provide additional information."
    ],
    'casual': [
        "Hey! I can help you with that.",
        "No problem, happy to help!",
        "Sure thing, let me know what you need.",
        "Yeah, I got you covered."
    ],
    'polite': [
        "Please let me know if you need any assistance.",
        "Thank you so much for your patience.",
        "I would be grateful if you could provide more details.",
        "I appreciate your understanding in this matter."
    ],
    'professional': [
        "Our team will review your request and respond promptly.",
        "We value your feedback and will address your concerns.",
        "I'll ensure this matter is handled with the utmost priority.",
        "We are committed to providing you with the best service."
    ],
    'friendly': [
        "I'm here to help! What can I do for you?",
        "Happy to assist! Let's get this sorted out.",
        "No worries at all! I've got you covered.",
        "Absolutely! I'd be glad to help with that."
    ],
    'neutral': [
        "I can provide information about that.",
        "Here are the details you requested.",
        "The information is as follows.",
        "Let me explain how this works."
    ]
}


def detect_tone(text: str, model: SentenceTransformer = None) -> Dict:
    """
    Detect tone by comparing text to reference examples using semantic similarity.
    
    Args:
        text: Text to analyze
        model: SentenceTransformer model (if None, uses mock for demo)
    
    Returns:
        Dict with detected tone, confidence, and all tone scores
    """
    # For demo: use mock embedding if no model provided
    if model is None:
        # Mock embedding - replace with real model in production
        np.random.seed(hash(text) % 2**32)
        text_embedding = np.random.rand(384)
        
        # Mock tone scores
        tone_scores = {tone: np.random.rand() * 0.3 + 0.5 for tone in TONE_REFERENCES.keys()}
        best_tone = max(tone_scores, key=tone_scores.get)
        
        return {
            'tone': best_tone,
            'confidence': tone_scores[best_tone],
            'all_scores': tone_scores
        }
    
    # Real implementation with sentence-transformers
    text_embedding = model.encode(text, normalize_embeddings=True)
    
    tone_scores = {}
    for tone_name, examples in TONE_REFERENCES.items():
        # Get embeddings for all reference examples
        example_embeddings = model.encode(examples, normalize_embeddings=True)
        
        # Calculate cosine similarity with each example
        similarities = [
            np.dot(text_embedding, ex) for ex in example_embeddings
        ]
        # Use average similarity as tone score
        tone_scores[tone_name] = float(np.mean(similarities))
    
    # Get the tone with highest similarity
    best_tone = max(tone_scores, key=tone_scores.get)
    confidence = tone_scores[best_tone]
    
    return {
        'tone': best_tone,
        'confidence': confidence,
        'all_scores': tone_scores
    }


def check_tone_drift(
    baseline_response: str,
    current_response: str,
    model: SentenceTransformer = None,
    allow_tone_change: bool = False
) -> Dict:
    """
    Check if tone has drifted between baseline and current responses.
    
    Args:
        baseline_response: Response from baseline model
        current_response: Response from current model
        model: SentenceTransformer model (if None, uses mock for demo)
        allow_tone_change: If True, only flags drift if confidence drops significantly
    
    Returns:
        Dict with tone drift detection results
    """
    baseline_tone = detect_tone(baseline_response, model)
    current_tone = detect_tone(current_response, model)
    
    tone_changed = baseline_tone['tone'] != current_tone['tone']
    confidence_drop = baseline_tone['confidence'] - current_tone['confidence']
    
    # Drift detected if:
    # 1. Tone changed (unless allow_tone_change=True)
    # 2. Confidence dropped significantly (>0.2)
    drift_detected = (
        (tone_changed and not allow_tone_change) or
        (confidence_drop > 0.2)
    )
    
    return {
        'tone_drift': drift_detected,
        'baseline_tone': baseline_tone['tone'],
        'current_tone': current_tone['tone'],
        'tone_changed': tone_changed,
        'baseline_confidence': baseline_tone['confidence'],
        'current_confidence': current_tone['confidence'],
        'confidence_drop': confidence_drop,
        'baseline_all_scores': baseline_tone['all_scores'],
        'current_all_scores': current_tone['all_scores']
    }


# Example usage
if __name__ == "__main__":
    # Example 1: Formal tone
    text1 = "I would be pleased to assist you with your inquiry. Please provide additional details."
    result1 = detect_tone(text1)
    print("Example 1 - Formal Tone:")
    print(f"Detected tone: {result1['tone']}")
    print(f"Confidence: {result1['confidence']:.3f}")
    print()
    
    # Example 2: Casual tone
    text2 = "Hey! I can help you with that. What do you need?"
    result2 = detect_tone(text2)
    print("Example 2 - Casual Tone:")
    print(f"Detected tone: {result2['tone']}")
    print(f"Confidence: {result2['confidence']:.3f}")
    print()
    
    # Example 3: Tone drift detection
    baseline = "I would be happy to assist you with your request. Please provide more details."
    current = "Yeah, I can help. What do you need?"
    
    drift_result = check_tone_drift(baseline, current)
    print("Example 3 - Tone Drift:")
    print(f"Baseline tone: {drift_result['baseline_tone']}")
    print(f"Current tone: {drift_result['current_tone']}")
    print(f"Tone changed: {drift_result['tone_changed']}")
    print(f"Drift detected: {drift_result['tone_drift']}")
    print()
    
    # Example 4: No tone drift (similar tone)
    baseline = "Thank you for your inquiry. I'll be happy to help."
    current = "Thank you for your question. I would be pleased to assist you."
    
    drift_result = check_tone_drift(baseline, current)
    print("Example 4 - No Tone Drift:")
    print(f"Baseline tone: {drift_result['baseline_tone']}")
    print(f"Current tone: {drift_result['current_tone']}")
    print(f"Drift detected: {drift_result['tone_drift']}")
```

### Usage in Drift Detection

```python
from sentence_transformers import SentenceTransformer
from tone_detection import detect_tone, check_tone_drift

# Initialize model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Compare baseline vs current
baseline_response = baseline_model(question)
current_response = current_model(question)

# Check for tone drift
result = check_tone_drift(
    baseline_response, 
    current_response,
    model=model,
    allow_tone_change=False  # Flag any tone change as drift
)

if result['tone_drift']:
    print(f"⚠️ Tone drift detected!")
    print(f"Baseline: {result['baseline_tone']} (confidence: {result['baseline_confidence']:.3f})")
    print(f"Current: {result['current_tone']} (confidence: {result['current_confidence']:.3f})")
    # Log or alert
```

### Key Features

1. **Semantic**: Uses embeddings to understand tone meaning, not keywords
2. **Flexible**: Easy to add new tone categories by adding reference examples
3. **Simple**: Just compare against reference examples
4. **Configurable**: Control whether tone changes are considered drift

### Configuration

- **Tone Categories**: Add or modify tones in `TONE_REFERENCES` dictionary
- **allow_tone_change**: 
  - `False` (default): Any tone change = drift
  - `True`: Only flag if confidence drops significantly
- **Confidence threshold**: Drift if confidence drops > 0.2 (adjustable in code)

### Production Setup

```python
from sentence_transformers import SentenceTransformer

# Initialize once (reuse across calls)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Use in functions
result = detect_tone(text, model=model)
```

### Customizing Tone Categories

To add new tone categories, simply add to `TONE_REFERENCES`:

```python
TONE_REFERENCES['apologetic'] = [
    "I sincerely apologize for the inconvenience.",
    "I'm sorry about that. Let me fix it right away.",
    "My apologies for the confusion."
]
```

---

## Future Functions

More functions will be added here as requested:
- [ ] Semantic similarity check
- [ ] Fact validation check
- [ ] PII security check
- [ ] Performance metrics check
- [ ] Multi-turn conversation check

