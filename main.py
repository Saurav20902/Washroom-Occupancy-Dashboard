from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
import uvicorn
import asyncio
import time
import threading
import webbrowser

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Facility data
facilities = {
    "female":   {"icon": "♀", "total": 8,  "vacant": 8},
    "male":     {"icon": "♂", "total": 10, "vacant": 10},
    "family":   {"icon": "👨‍👩‍👧", "total": 1,  "vacant": 1},
    "disabled": {"icon": "♿", "total": 2,  "vacant": 2},
    "prayer":   {"icon": "🕌", "total": 1,  "vacant": 1},
}

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.get_template("index.html").render({"request": request, "facilities": facilities})

@app.get("/updates")
async def updates():
    async def generator():
        while True:
            cycle = int(time.time() % 20)

            if cycle < 5:       # All vacant → green
                for f in facilities: facilities[f]["vacant"] = facilities[f]["total"]
            elif cycle < 10:    # Half occupied
                facilities["female"]["vacant"] = 2
                facilities["male"]["vacant"] = 3
                facilities["disabled"]["vacant"] = 0
            elif cycle < 15:    # Almost full → red
                for f in facilities: facilities[f]["vacant"] = 0
            else:               # Mixed
                facilities["female"]["vacant"] = 7
                facilities["male"]["vacant"] = 8
                facilities["disabled"]["vacant"] = 1
                facilities["prayer"]["vacant"] = 0

            # Update text
            for f in facilities:
                facilities[f]["text"] = "空置中 Vacant" if facilities[f]["vacant"] > 0 else "使用中 Occupied"

            yield {"data": str(facilities)}
            await asyncio.sleep(5)   # changes every 5 seconds

    return EventSourceResponse(generator())

# ——— THIS PART IS PERFECT NOW ———
if __name__ == "__main__":
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://127.0.0.1:8006")

    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run(app, host="0.0.0.0", port=8006)