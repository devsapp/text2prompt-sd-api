from typing import Optional, Any
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    query: str
    kwargs: Optional[dict[str, Any]] = Field({
        "max_length": 1024,
        "do_sample": True,
        "temperature": 1.0,
        "top_k": 50,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
        "num_return_sequences": 1
    })

class ChatResponse(BaseModel):
    answer: str
