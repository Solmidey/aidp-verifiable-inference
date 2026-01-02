from fastapi import FastAPI
from pydantic import BaseModel
from .inference import run_inference
from .receipt import generate_receipt

app = FastAPI(title="AIDP Verifiable Inference Gateway")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/infer")
def infer(req: PromptRequest):
    output = run_inference(req.prompt)
    receipt = generate_receipt(req.prompt, output)

    return {
        "output": output,
        "receipt": receipt
    }
