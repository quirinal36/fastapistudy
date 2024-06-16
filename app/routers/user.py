from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_303_SEE_OTHER
from app.database import SessionLocal, engine
from app.crud import get_users, create_user
from app.schemas import UserCreate
from app.utils import normalize_phone_number
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)

    context={
        "request": request,
        "title":"user infomation",
        "users":users
        }
    return templates.TemplateResponse('index.html', context)

@router.get("/add_user", response_class=HTMLResponse)
def add_user_form(request:Request):
    return templates.TemplateResponse('add_user.html', {"request":request})

@router.post("/add_user", response_class=RedirectResponse)
def add_user(name: str=Form(...), phone: str = Form(...), db: Session = Depends(get_db)):
    normalized_phone = normalize_phone_number(phone)
    user = UserCreate(name=name, phone=normalized_phone)
    create_user(db, user)
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)