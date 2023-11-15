from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel
import uvicorn
#from next_process_trigger import trigger
import os
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

app=FastAPI()

@app.get("/")
async def get():
  return {"status":"success","message":"from band calculation"}
class Item(BaseModel):
  crop_id: str
  file_name_consider: list 
  base_path:str
  bands:list
  all_dates:list
    
@app.post("api/post")
async def post(item:Item,next_process_trigger:BackgroundTasks):
  #print('request recieved for ',item.crop_id)
  data=item.model_dump()
  #print(data)
  
  """if bool(os.getenv("NEXT_TRIGGER_END_POINT_ENABLE"))==True:
    next_process_trigger.add_task(trigger.layerstacking_trigger,item.base_path,item.crop_id,item.all_dates)
  """
  
  #print(item.crop_id,item.bands)
  #r"D:\agribridge_projects\micro_service_arc",str(c),["NDVI", "NDWI", "VARI", "MCARI", "NIR"],file_name_consider
  return {"message":"success"}

#it gives the interface for control the apis
def my_schema():
   openapi_schema = get_openapi(
       title="Api Testing",
       version="1.0",
       description="Hi",
       routes=app.routes,
   )
   app.openapi_schema = openapi_schema
   return app.openapi_schema


if __name__=="__main__":
  uvicorn.run("api_app:app",workers=12,host="localhost",port=2000)