from fastapi import FastAPI,Request,Form,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Models import User
from fastapi import FastAPI, Form
from database import get_db, Base, engine
from sqlalchemy.orm import Session



Base.metadata.create_all(bind = engine)

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
async def home_page(request:Request,db:Session = Depends(get_db)):
    contacts = db.query(User).all()
    return templates.TemplateResponse("index.html", {"request": request, "contacts":contacts})





@app.post("/post")
async def create_contact(request: Request,
    Name: str = Form(...),
    contact: str = Form(...),
    Email: str = Form(...),
    Address: str = Form(...),
    db: Session = Depends(get_db)):
   
   new_item = User(Name = Name, contact=contact, Email = Email, Address=Address)
   db.add(new_item)
   db.commit()
   db.refresh(new_item)

   contacts = db.query(User).all()
   return templates.TemplateResponse("index.html",{"request":request,"contacts":contacts})



@app.post("/delete/{contact_id}",response_class=HTMLResponse)
async def delete_contact(contact_id:int,request:Request,db:Session = Depends(get_db)):
    contact = db.query(User).filter(User.id == contact_id).first()

    if contact:
        db.delete(contact)
        db.commit()

    contacts = db.query(User).all()
    return templates.TemplateResponse("index.html",{"request":request,"contacts":contacts})




@app.get("/update/{contact_id}", response_class=HTMLResponse)
async def update_page(contact_id:int,request:Request,db:Session = Depends(get_db)):

    contact = db.query(User).filter(User.id == contact_id).first()

    if not contact:
        return HTMLResponse(content="Contact not found", status_code=404)
    
    return templates.TemplateResponse("update.html",{"request":request, "contact":contact})





@app.post("/update/{contact_id}",response_class=HTMLResponse)
async def update_contact(contact_id: int,request:Request,
    Name: str = Form(...),
    contact: str = Form(...),
    Email: str = Form(...),
    Address: str = Form(...),
    db: Session = Depends(get_db)):

    contact_item = db.query(User).filter(User.id == contact_id).first()

    if not contact_item:
        return {"error":"cannot found"}
    
    contact_item.Name = Name
    contact_item.contact = contact
    contact_item.Email = Email
    contact_item.Address = Address
    db.commit()

    contacts = db.query(User).all()
    return templates.TemplateResponse("index.html", {"request": request, "contacts":contacts})






    




