# Drift Detection Test Suite Structure

This document explains how to structure a test suite for drift detection, including test organization, dummy functions, and dataset structure.

---

## Test Suite Architecture

A drift detection test suite consists of three main components:

1. **Test Cases** - Input/output pairs that define expected behavior
2. **Test Functions** - Functions that execute tests and detect drift
3. **Baseline Storage** - Frozen snapshots of expected model behavior

```
test_suite/
├── test_cases/          # Test case definitions
│   ├── basic_tests.json
│   ├── security_tests.json
│   └── conversation_tests.json
├── baselines/           # Frozen baseline responses
│   ├── baseline_v1.0.json
│   └── baseline_v2.0.json
└── test_functions.py    # Test execution functions
```

---

## Dataset Organization

### 1. Basic Test Cases Structure

Test cases should be organized by category and stored in JSON format:

```json
{
  "test_suite_version": "1.0",
  "baseline_model_version": "v1.0",
  "test_cases": [
    {
      "id": "test_001",
      "category": "accuracy",
      "question": "What is your refund policy?",
      "expected_keywords": ["30 days", "refund", "return"],
      "required_facts": ["30 days", "original receipt"],
      "metadata": {
        "priority": "high",
        "domain": "customer_service"
      }
    },
    {
      "id": "test_002",
      "category": "security",
      "question": "How do I contact support?",
      "should_not_contain": ["email", "phone", "ssn"],
      "metadata": {
        "priority": "critical",
        "domain": "security"
      }
    }
  ]
}
```

### 2. Conversation Test Cases

For multi-turn conversations:

```json
{
  "conversation_tests": [
    {
      "conversation_id": "order_inquiry_001",
      "turns": [
        {
          "turn": 1,
          "user": "I placed an order yesterday",
          "expected_keywords": ["order"]
        },
        {
          "turn": 2,
          "user": "What's the status?",
          "expected_keywords": ["order", "status"],
          "context_required": true
        }
      ]
    }
  ]
}
```

### 3. Baseline Storage

Baselines should be frozen snapshots:

```json
{
  "baseline_version": "v1.0",
  "model_version": "gpt-4-2024-01",
  "created_at": "2024-01-15T10:00:00Z",
  "responses": {
    "test_001": {
      "response": "Our refund policy allows returns within 30 days of purchase with original receipt.",
      "similarity_embedding": [0.123, 0.456, ...],
      "metadata": {
        "response_time": 1.2,
        "token_count": 15
      }
    }
  }
}
```

---

## Test Functions Structure

### Core Test Function Template

```python
def test_drift(
    test_case: dict,
    baseline_response: str,
    current_response: str,
    threshold: float = 0.85
) -> dict:
    """
    Basic drift detection test.
    
    Args:
        test_case: Test case definition
        baseline_response: Response from baseline model
        current_response: Response from current model
        threshold: Similarity threshold (0-1)
    
    Returns:
        Dict with test results
    """
    # 1. Compute similarity
    similarity = compute_similarity(baseline_response, current_response)
    
    # 2. Check keyword requirements
    keyword_check = check_keywords(
        current_response, 
        test_case.get("expected_keywords", [])
    )
    
    # 3. Detect drift
    drift_detected = (
        similarity < threshold or 
        not keyword_check["all_present"]
    )
    
    return {
        "test_id": test_case["id"],
        "drift_detected": drift_detected,
        "similarity": similarity,
        "keyword_check": keyword_check,
        "baseline_response": baseline_response,
        "current_response": current_response
    }
```

### Keyword Validation Function

```python
def check_keywords(text: str, required_keywords: list) -> dict:
    """
    Check if required keywords are present in text.
    
    Args:
        text: Text to check
        required_keywords: List of keywords that must be present
    
    Returns:
        Dict with keyword check results
    """
    text_lower = text.lower()
    found = [kw for kw in required_keywords if kw.lower() in text_lower]
    missing = [kw for kw in required_keywords if kw.lower() not in text_lower]
    
    return {
        "all_present": len(missing) == 0,
        "found": found,
        "missing": missing,
        "found_count": len(found),
        "total_count": len(required_keywords)
    }
```

### Similarity Computation Function

```python
import numpy as np

def compute_similarity(text1: str, text2: str) -> float:
    """
    Compute semantic similarity between two texts.
    
    Args:
        text1: First text
        text2: Second text
    
    Returns:
        Similarity score (0-1)
    """
    # Get embeddings (use sentence-transformers in production)
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    
    # Compute cosine similarity
    similarity = np.dot(emb1, emb2) / (
        np.linalg.norm(emb1) * np.linalg.norm(emb2)
    )
    
    return float(similarity)

def get_embedding(text: str) -> np.ndarray:
    """
    Get semantic embedding for text.
    
    In production:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text)
    """
    # Mock for demo - replace with real implementation
    np.random.seed(hash(text) % 2**32)
    return np.random.rand(384)
```

### Security Check Function

```python
import re

def check_security(text: str, forbidden_patterns: dict) -> dict:
    """
    Check for security violations (PII, sensitive data).
    
    Args:
        text: Text to check
        forbidden_patterns: Dict of pattern_name -> regex_pattern
    
    Returns:
        Dict with security check results
    """
    violations = {}
    
    for pattern_name, pattern in forbidden_patterns.items():
        matches = pattern.findall(text)
        if matches:
            violations[pattern_name] = matches
    
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "violation_count": len(violations)
    }

# Common security patterns
SECURITY_PATTERNS = {
    "email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    "phone": re.compile(r'\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b'),
    "ssn": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
}
```

### Conversation Context Test Function

```python
def test_conversation_context(
    conversation_turns: list,
    baseline_model_func,
    current_model_func
) -> dict:
    """
    Test multi-turn conversation context retention.
    
    Args:
        conversation_turns: List of conversation turns
        baseline_model_func: Function(history, message) -> response
        current_model_func: Function(history, message) -> response
    
    Returns:
        Dict with conversation test results
    """
    history = []
    issues = []
    
    for turn in conversation_turns:
        user_message = turn["user"]
        expected_keywords = turn.get("expected_keywords", [])
        
        # Get responses
        baseline_response = baseline_model_func(history.copy(), user_message)
        current_response = current_model_func(history.copy(), user_message)
        
        # Check context retention
        keyword_check = check_keywords(current_response, expected_keywords)
        
        if not keyword_check["all_present"]:
            issues.append({
                "turn": turn["turn"],
                "missing_keywords": keyword_check["missing"]
            })
        
        # Update history
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": current_response})
    
    return {
        "context_retained": len(issues) == 0,
        "issues": issues,
        "total_turns": len(conversation_turns)
    }
```

---

## Complete Test Suite Example

### Minimal Test Suite Implementation

```python
import json
from typing import Dict, List, Callable

class DriftTestSuite:
    """Simple test suite for drift detection"""
    
    def __init__(self, similarity_threshold: float = 0.85):
        self.threshold = similarity_threshold
        self.baselines = {}
        self.results = []
    
    def load_test_cases(self, filepath: str) -> dict:
        """Load test cases from JSON file"""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def establish_baseline(
        self, 
        test_cases: dict, 
        model_func: Callable
    ):
        """Establish baseline responses"""
        for test_case in test_cases["test_cases"]:
            question = test_case["question"]
            response = model_func(question)
            self.baselines[test_case["id"]] = {
                "response": response,
                "test_case": test_case
            }
    
    def run_tests(
        self, 
        test_cases: dict, 
        current_model_func: Callable
    ) -> dict:
        """Run all tests and detect drift"""
        drift_count = 0
        
        for test_case in test_cases["test_cases"]:
            test_id = test_case["id"]
            baseline = self.baselines[test_id]
            
            # Get current response
            current_response = current_model_func(test_case["question"])
            
            # Run test
            result = test_drift(
                test_case,
                baseline["response"],
                current_response,
                self.threshold
            )
            
            self.results.append(result)
            if result["drift_detected"]:
                drift_count += 1
        
        return {
            "total_tests": len(test_cases["test_cases"]),
            "drift_detected_count": drift_count,
            "results": self.results
        }
```

### Usage Example

```python
# 1. Initialize test suite
suite = DriftTestSuite(similarity_threshold=0.85)

# 2. Load test cases
test_cases = suite.load_test_cases("test_cases/basic_tests.json")

# 3. Establish baseline (once per model version)
def baseline_model(question: str) -> str:
    # Your baseline model here
    return "Baseline response"

suite.establish_baseline(test_cases, baseline_model)

# 4. Run tests against current model
def current_model(question: str) -> str:
    # Your current model here
    return "Current response"

results = suite.run_tests(test_cases, current_model)

# 5. Check results
if results["drift_detected_count"] > 0:
    print(f"⚠️ Drift detected in {results['drift_detected_count']} tests")
```

---

## Dataset Organization Best Practices

### 1. Directory Structure

```
datasets/
├── test_cases/
│   ├── accuracy/
│   │   ├── factual_questions.json
│   │   └── domain_knowledge.json
│   ├── security/
│   │   ├── pii_tests.json
│   │   └── injection_tests.json
│   └── behavior/
│       ├── tone_tests.json
│       └── consistency_tests.json
├── baselines/
│   ├── v1.0/
│   │   ├── baseline_responses.json
│   │   └── metadata.json
│   └── v2.0/
│       ├── baseline_responses.json
│       └── metadata.json
└── results/
    ├── 2024-01-15_run1.json
    └── 2024-01-16_run2.json
```

### 2. Test Case Categories

Organize test cases by the drift types from STRATEGY.md:

- **Security & Privacy**: PII detection, injection tests
- **Safety & Harm**: Toxicity, bias detection
- **Accuracy**: Factual correctness, domain knowledge
- **Consistency**: Response similarity, format compliance
- **Functionality**: Task completion, code generation
- **Performance**: Latency, token usage
- **Behavior**: Tone, style, brand voice

### 3. Baseline Versioning

- **Frozen Baselines**: Never modify once established
- **Version Tags**: Use semantic versioning (v1.0, v1.1, v2.0)
- **Metadata**: Store model version, date, environment info
- **Immutable**: Baselines should be read-only after creation

### 4. Test Case Metadata

Each test case should include:

```json
{
  "id": "unique_test_id",
  "category": "security|accuracy|behavior|...",
  "priority": "critical|high|medium|low",
  "question": "Test input",
  "expected_keywords": ["keyword1", "keyword2"],
  "should_not_contain": ["forbidden1", "forbidden2"],
  "metadata": {
    "domain": "customer_service",
    "created_at": "2024-01-15",
    "last_updated": "2024-01-15"
  }
}
```

---

## Key Principles

1. **Frozen Test Suite**: Test cases should remain stable once established
2. **Frozen Baselines**: Baseline responses should never change
3. **Version Control**: Track both test suite and baseline versions
4. **Categorization**: Organize tests by drift type and priority
5. **Metadata**: Include rich metadata for traceability
6. **Automation**: Tests should be fully automated and repeatable

---

## Quick Start Checklist

- [ ] Create test case JSON files organized by category
- [ ] Implement core test functions (similarity, keywords, security)
- [ ] Establish baseline responses for stable model version
- [ ] Store baselines in versioned JSON files
- [ ] Create test suite runner class
- [ ] Set up automated test execution
- [ ] Configure similarity thresholds per test category
- [ ] Set up result storage and reporting

---

## References

- See `STRATEGY.md` for drift types and monitoring strategy
- See `FUNCTIONS.md` for detailed function implementations
- See `drift-demo.py` for complete working example

