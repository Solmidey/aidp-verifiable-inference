import torch
from .model import model, tokenizer

@torch.inference_mode()
def run_inference(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False,  # IMPORTANT: deterministic
        temperature=0.0
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
