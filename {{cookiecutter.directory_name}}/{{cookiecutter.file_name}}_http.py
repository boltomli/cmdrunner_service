import uvicorn
from fastapi import Body, FastAPI, HTTPException, status

try:
    from .cmdrunner import run_command
except Exception:
    from cmdrunner import run_command

app = FastAPI()


@app.post("/")
async def root(*, payload=Body(...)):
    if "command" not in payload:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No command parameter")
    command = payload["command"]
    args = payload["args"] if "args" in payload else None
    return run_command(command, args)


if __name__ == "__main__":
    uvicorn.run(app)
