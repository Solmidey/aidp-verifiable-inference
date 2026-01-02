import hashlib
import time
import platform
import torch

def sha256(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

def generate_receipt(prompt, output):
    return {
        "input_hash": sha256(prompt),
        "output_hash": sha256(output),
        "model": "mistral-7b-instruct",
        "torch_version": torch.__version__,
        "device": torch.cuda.get_device_name(0),
        "gpu_arch": platform.machine(),
        "timestamp": int(time.time())
    }
