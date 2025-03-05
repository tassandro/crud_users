from pydantic import BaseModel

# Modelo para criação de usuário
class UserCreate(BaseModel):
    full_name: str
    username: str
    password: str

    class Config:
        orm_mode = True

# Modelo para o token de acesso
class Token(BaseModel):
    access_token: str
    token_type: str

# Modelo de saída para um usuário (não inclui senha)
class UserOut(BaseModel):
    id: str
    full_name: str
    username: str

    class Config:
        orm_mode = True
        from_attributes = True
