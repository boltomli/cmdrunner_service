from base64 import b64encode


# Implement custom logic to run the command
def run_command(command, args=None):
    if args is None:
        args = []

    # Should check command availability, security, etc.
    if command in ["known", "secure", "path"]:
        message = f"Run {command} with {args}"
    else:
        message = f"{command} not callable"

    return {"data": b64encode(message.encode("utf-8")), "message": message}
