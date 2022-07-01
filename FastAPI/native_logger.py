import logging
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import time
import random
import string

class User(BaseModel):
   id: int
   name: str
   email: str

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    # file_handler = logging.FileHandler(filename='./server.log')
    file_handler = logging.handlers.RotatingFileHandler("fastapi_server.log", mode="a", maxBytes = 1000*1024, backupCount = 3)
    formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s")

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logging.getLogger(__name__)

app = FastAPI()
logger = setup_logger()

# middleware
@app.middleware("http")
async def log_requests(request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    # wait to process requst and get response
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    return response

# startup event
@app.on_event("startup")
async def startup_event():
    logger.info("startup_event")

# shutdown event
@app.on_event("shutdown")
def shutdown_event():
    logger.info("shutdown_event")

# GET methods
@app.get("/")
def read_root():
    logger.info("read_root")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
   return {"item_id": item_id, "q": q}

# POST methods
@app.post('/user/update')
async def update_user(*, user: User):
   return {"code": 200}

if __name__ == "__main__":
   # setup native logger
   uvicorn.run(app, host="0.0.0.0", port=8000)