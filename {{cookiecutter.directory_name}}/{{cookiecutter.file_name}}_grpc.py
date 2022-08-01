import asyncio
from base64 import b64encode

from homi.extend.service import health_service, reflection_service

try:
    from .cmdrunner_pb2 import _RUNNER
except Exception:
    from cmdrunner_pb2 import _RUNNER

from homi import AsyncApp, AsyncServer

app = AsyncApp(
    services=[
        _RUNNER,
        reflection_service,
        health_service,
    ]
)
service_name = "cmdrunner.Runner"


# implement the command to run
def run_command(command, args=None):
    if args is None:
        args = []
    message = (f"Run {command} with {args}")
    return {"data": b64encode(message.encode("utf-8")), "message": message}


# unary-unary method
@app.method(service_name)
async def RunCommand(command, args, **kwargs):
    if not command:
        return {}
    return run_command(command, args)


# stream-stream method
@app.method(service_name)
async def RunCommandOneByOne(request_iterator, context):
    async for request in request_iterator:
        if "command" not in request:
            yield {}
        command = request["command"]
        args = request["args"] if "args" in request else None
        yield run_command(command, args)


if __name__ == "__main__":
    server = AsyncServer(app)
    asyncio.run(server.run())