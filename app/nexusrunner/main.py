from fastapi import FastAPI
app = FastAPI(title="NexusRunner Control Plane")

@app.get("/health")
def health():
    return {"ok": True}
