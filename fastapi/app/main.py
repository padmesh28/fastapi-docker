from fastapi import FastAPI
from .tasks import long_running_task

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/process/{value}")
def process(value: int):
    task = long_running_task.delay(value)
    return {
        "task_id": task.id,
        "status": "submitted"
    }

