def schemas_user(user) -> dict :
    return {
        "id" : str(user["_id"]),
        "nip" : str(user["nip"])
    }