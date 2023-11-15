from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel
import uvicorn
#from next_process_trigger import trigger
import os
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

if __name__=="__main__":
  uvicorn.run("api_app:app",workers=10,host="127.2.2.2",port=2000)