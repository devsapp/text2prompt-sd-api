from fastapi import FastAPI
from fastapi.responses import StreamingResponse, RedirectResponse
import uvicorn
from schema import ChatRequest, ChatResponse
import service
app = FastAPI()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return {"answer": service.chat(request.query, **request.kwargs if request.kwargs else {})}


@app.post("/chat/stream")
def stream_chat(request: ChatRequest):
    return StreamingResponse(
        service.stream_chat(request.query, **request.kwargs if request.kwargs else {}))


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url='/docs')


uvicorn.run(app, host="0.0.0.0", port=8000)
