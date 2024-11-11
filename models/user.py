from pydantic import BaseModel

class User(BaseModel):
    nip = str
    nama = str
