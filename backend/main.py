from fastapi import FastAPI

from app.api.v1.router import router as v1_router

app = FastAPI(
    title="Classifyd API",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)