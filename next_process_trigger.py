import pandas
import json
import os
from dotenv import load_dotenv
load_dotenv()
import requests

"""class trigger:
  def layerstacking_trigger(path,crop_id,all_dates):
    #print(os.getcwd()+"band_calculation")
    #d=json.load(p)
    #all_dates=d[crop_id]
    #print(d['400411'])
    d=requests.post(os.getenv("NEXT_TRIGGER_END_POINT"),json={"path":path,"crop_id":crop_id,"all_dates":all_dates})
    
    if d.status_code==200:
      print(d.json())
    else:
      print("request failed")
      print(d.json())

"""