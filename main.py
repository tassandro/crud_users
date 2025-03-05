from fastapi import FastAPI
from models.database import engine, Base
from routes import user_routes

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routes.router)

@app.get("/")
def home():
    return {"message": "API está rodando!"}