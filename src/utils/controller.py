
async def controllerCode(code):
    forbidden_keys = ["marshal", "os", "subprocess", "shel", "sys", "exec(", "pip"]
    for forbidden in forbidden_keys:
        if forbidden in code:
            return False
    return True
