from fastapi import FastAPI

app = FastAPI(title="ComicCraft AI")

@app.get("/")
def home():
    return {
        "message": "ComicCraft AI is running successfully!"
    }

@app.get("/api/health")
def health():
    return {"status": "ok"}