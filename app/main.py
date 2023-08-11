from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def load_landing(request:Request):
    return templates.TemplateResponse("landing.html",{"request":request})

@app.get("/login",response_class=HTMLResponse)
async def load_login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/type",response_class=HTMLResponse)
async def load_type(request:Request):
    return templates.TemplateResponse("type.html",{"request":request})

@app.get("/age",response_class=HTMLResponse)
async def load_age(request:Request):
    return templates.TemplateResponse("age.html",{"request":request})

@app.get("/open-platform",response_class=HTMLResponse)
async def load_open_platform(request:Request):
    return templates.TemplateResponse("open_platform.html",{"request":request})

@app.get("/age-group-1",response_class=HTMLResponse)
async def load_age1(request:Request):
    return templates.TemplateResponse("age-grp-1.html",{"request":request})

@app.get("/age-group-2",response_class=HTMLResponse)
async def load_age2(request:Request):
    return templates.TemplateResponse("age-grp-2.html",{"request":request})

@app.get("/age-group-3",response_class=HTMLResponse)
async def load_age3(request:Request):
    return templates.TemplateResponse("age-grp-3.html",{"request":request})