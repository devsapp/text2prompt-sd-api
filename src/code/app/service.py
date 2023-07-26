# pylint: disable=global-statement, invalid-name
import os
from threading import Thread
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.generation import TextIteratorStreamer
MODEL_PATH = os.environ.get("MODEL_PATH")
PROMPT = os.environ.get("PROMPT", "")
tokenizer = None
model = None


def init():
    global tokenizer
    if not tokenizer:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    global model
    if not model:
        model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True).eval()


def generate_prompt(query: str):
    return PROMPT.replace("{query}", query) if "{query}" in PROMPT else query


def chat(query: str, **kwargs):
    init()
    prompt = generate_prompt(query)
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(input_ids, **kwargs)
    answers = [
        answer.strip()
        for answer in tokenizer.batch_decode(
            outputs[:, input_ids.size(1):],
            skip_special_tokens=True)]
    return "\n".join(answers)


def stream_chat(query: str, **kwargs):
    init()
    prompt = generate_prompt(query)
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True)
    thread = Thread(target=model.generate, kwargs={
                    "inputs": input_ids, "streamer": streamer, **kwargs})
    thread.start()
    return streamer
