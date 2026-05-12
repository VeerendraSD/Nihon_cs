# Nihon_cs
# 🚀 Nihon-CS: Optimized Llama-3 Translator for Technical Japanese

**Nihon-CS** is a domain-specific Large Language Model (LLM) fine-tuned to bridge the gap between English Computer Science terminology and polite Japanese (**Minna no Nihongo** style). 

[Link to Model on Hugging Face](https://huggingface.co/vwrizz/japanese-cs-llama3)

### 💡 The Problem
Machine translation often fails at technical CS concepts (e.g., "Linked List" or "Asynchronous Programming") or uses overly informal Japanese. This project adaptively fine-tunes Llama-3 to maintain technical accuracy while adhering to formal grammar.

### 🛠️ Technical Stack
- **Base Model:** Llama-3 8B
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation) via **Unsloth**
- **Quantization:** 4-bit (bitsandbytes) & GGUF (for CPU inference)
- **Deployment:** Hugging Face Hub & Gradio

### 📈 Key Highlights
- **60% VRAM Reduction:** Achieved using Unsloth's optimized kernels during training.
- **CPU Ready:** Integrated GGUF support for low-latency inference on standard hardware.
- **Curated Dataset:** Custom-built dataset mapping CS definitions to Japanese equivalents.

### 🚀 Usage
```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained("vwrizz/japanese-cs-llama3")
# ... (add your inference code here)
