from unsloth import FastLanguageModel
import torch

def load_nihon_cs_model():
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "vwrizz/japanese-cs-llama3",
        max_seq_length = 2048,
        load_in_4bit = True,
    )
    FastLanguageModel.for_inference(model)
    return model, tokenizer

def translate(text, model, tokenizer):
    prompt = f"Translate the following English CS sentence into Japanese:\nInput: {text}\nResponse:"
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=64)
    return tokenizer.batch_decode(outputs)[0]

if __name__ == "__main__":
    m, t = load_nihon_cs_model()
    print(translate("What is a binary search tree?", m, t))