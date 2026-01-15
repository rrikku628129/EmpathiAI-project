
# EmpathiAI: Conversational Mental Health Support System

**Goal:** Build a conversational AI system capable of recognizing empathy and generating safe, supportive, and personalized responses for mental-health contexts.

---

## Motivation

Mental-health care requires emotionally sensitive communication.  
Traditional chatbots lack empathy and may produce unsafe or unhelpful responses.

This project aims to understand how AI-expressed empathy influences therapeutic outcomes by examining relationships among:

- User emotional feedback
- Clinical risk patterns
- AI-generated empathetic responses

Ultimately, the system explores psychological and behavioral impacts of AI-assisted conversations.

---

## System Overview

EmpathiAI uses a hybrid architecture combining:

- Empathy classification
- Risk prediction
- Safe dialogue generation

**System Pipeline:**
```
User Input → Preprocessing → Empathy Classifier → Safe Response Generator
```

---

## Methods

### **Models**
1. **Baseline**
   - TF-IDF + Logistic Regression
2. **Main Model**
   - RoBERTa-base
   - Context + response concatenation for empathy learning

### **Training**
- Logistic Regression: Grid Search
- RoBERTa:
  - Optimizer: AdamW
  - LR = 2e-5
  - Batch = 8
  - Epochs = 3–5

### **Preprocessing**
- Text cleaning
- RoBERTa tokenization
- SMOTE oversampling for high-empathy class
- Back-translation & synonym augmentation

---

## Dataset

Source: `tcabanski/mental_health_counseling_conversations_rated`

### **Data Fields**
| Column | Description |
|---|---|
| `context` | User input text |
| `response` | Counselor reply |
| `avg_empathy_score` | Empathy 1–5 |
| `avg_appropriateness_score` | Appropriateness 1–5 |
| `avg_relevance_score` | Relevance 1–5 |

Dataset contains human-rated conversational counseling pairs.

---

## Evaluation

To evaluate conversational quality, four LLMs were scored on:

- Empathy
- Appropriateness
- Relevance
- Average Score

### **Model Comparison Results**
| Model          | Empathy | Appropriateness | Relevance | Average |
|----------------|---------|-----------------|-----------|---------|
| LLaMA3.1-8B    | 3.54    | 4.41            | 4.68      | 4.21    |
| LLaMA3.2-3B    | 4.05    | 4.20            | 4.04      | 4.09    |
| Qwen2.5-7B     | 3.01    | 4.04            | 3.67      | 3.57    |
| LLaMA3.2-1B    | 3.19    | 3.25            | 3.95      | 3.46    |

### **Key Findings**
- **LLaMA3.1-8B** achieved the highest overall performance (4.21), with strong balance across empathy, appropriateness, and relevance.
- **LLaMA3.2-3B** performed consistently across dimensions (avg 4.09).
- **Qwen2.5-7B** scored well in appropriateness (4.04) but underperformed in empathy & relevance.
- **LLaMA3.2-1B** ranked last across all metrics.

---

## System Components (High-level)

```
├── empathy_classifier/
├── safe_generation/
├── preprocessing/
└── evaluation/
```

---

## Example Use Case

> User expresses anxiety → System detects emotional context → Predicts empathy level → Generates safe and supportive response.

---

## Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Scikit-learn
- SMOTE
- Back-translation augmentation

---

## Future Directions

- Integrate clinical safety constraints
- Expand multi-modal emotion signals (speech, facial expressions)
- Fine-tune instruction-following models for therapy alignment

---

## Reference 

This repository corresponds to the research poster:  
“EmpathiAI: Conversational Mental Health Support System” :contentReference[oaicite:1]{index=1}

---

## Contact

If you'd like to collaborate on empathetic AI, LLM safety, or mental-health HCI research, feel free to reach out.


