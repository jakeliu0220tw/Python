import logging
import uvicorn
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel

class User(BaseModel):
   id: int
   name: str
   email: str

class Agent(BaseModel):
   id: str
   name: str
   invite_code: str

app = FastAPI()

# startup event
@app.on_event("startup")
async def startup_event():
   logging.info("test")
   with open("log.txt", mode="a") as log:
      log.write("Application startup\n")

# shutdown event
@app.on_event("shutdown")
def shutdown_event():
   with open("log.txt", mode="a") as log:
      log.write("Application shutdown\n")

# GET methods
@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.get("/ping")
def read_ping():
   return {"code": 200, "message": "pong"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
   return {"item_id": item_id, "q": q}

# POST methods
@app.post('/user/update')
async def update_user(*, user: User):
   return {"code": 200}

@app.post('/agent/build')
async def agent_build(*, agent: Agent):
   return {"code": 200, "message": "trigger to build", "id":agent.id, "name": agent.name, "invite_code": agent.invite_code}

# Backgroud Task
def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

if __name__ == "__main__":
   # setup logger with config file
   uvicorn.run(app, host="0.0.0.0", port=8000, log_config="log_config.json")