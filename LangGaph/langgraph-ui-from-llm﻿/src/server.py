from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

from .graph import generate_html_from_prompt

app = FastAPI(title="Generative UI Python Demo")

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

class GenerateRequest(BaseModel):
    description: str

@app.post("/generate")
async def generate_ui(request: GenerateRequest):
    """
    Generates HTML based on the user description.
    """
    try:
        html_content = await generate_html_from_prompt(request.description)
        return {"html": html_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    """
    Serves the index.html file.
    """
    from fastapi.responses import FileResponse
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
