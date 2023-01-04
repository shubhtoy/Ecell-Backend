from fastapi import FastAPI,Header,HTTPException,status,Depends
from pydantic import BaseModel
import uvicorn

class User(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    fullname: str

#define documentations
title="Ecell-Backend"
description="Backend for Ecell Website"

app = FastAPI(title=title, description=description)


def application_vnd(auth: str = Header(...)):
    """Require request MIME-type to be application/vnd.api+json"""

    if auth != "website":
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            f"Unsupported header: {auth}."
            " It must be website",
        )



@app.get("/getdetails/getall",dependencies=[Depends(application_vnd)])
def get_all_details():
    return {"details": "all details"}

@app.get("/pass/auth2",dependencies=[Depends(application_vnd)])
def authenticate_user():
    return {"response": "authenticated"}

@app.get("/getdetails/event",dependencies=[Depends(application_vnd)])
def get_event_details():
    return {"event_details": "details"}

@app.get("/getdetails/chairman",dependencies=[Depends(application_vnd)])
def get_chairman_details():
    return {"chairman_details": "details"}

@app.get("/getdetails/collaborators",dependencies=[Depends(application_vnd)])
def get_collaborators_details():
    return {"collaborators_details": "details"}

@app.get("/getdetails/management",dependencies=[Depends(application_vnd)])
def get_management_details():
    return {"management_details": "details"}

@app.post("/auth/register",dependencies=[Depends(application_vnd)])
def register_user(user: User):
    return {"name": user.name, "password": user.password, "email": user.email}

@app.post("/auth/profile",dependencies=[Depends(application_vnd)])
def update_profile(user: UserLogin):
    return {"fullname": user.fullname}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0",threaded=True, port=8000)