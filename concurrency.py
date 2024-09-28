from fastapi import FastAPI
import asyncio

app=FastAPI()

@app.get("/sleep/")
async def sleep_for_while(seconds:int):
    await asyncio.sleep(10)
    return {f"Slept for {seconds} seconds"}