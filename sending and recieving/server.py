from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class GradeRequest(BaseModel):
    score: int


@app.post("/analyze-grade")
def analyze_grade(data: GradeRequest):
    result = "Pass" if data.score >= 50 else "Fail"
    return {"status": result, "message": f"Your score is {data.score}"}
