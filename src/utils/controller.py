
async def controllerCode(code):
    forbidden_keys = ["marshal", "os", "subprocess", "shel", "sys", "exec(", "pip", "base64",
                      "ctfde", "base32", "base85", "binascii", "binary", "marshal", "marshcom",
                      "unpickle", "pickle", "unzlib", "zlib"]
    for forbidden in forbidden_keys:
        if forbidden in code:
            return False
    return True
