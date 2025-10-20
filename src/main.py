from fastapi import FastAPI, HTTPException
from src.math_ops import add, subtract, multiply, divide

app = FastAPI(title="Math Operations API")

@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    return {"result": subtract(a, b)}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"result": multiply(a, b)}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
