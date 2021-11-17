import pandas as pd
import os
from datetime import date

dir = ("D:\Code\ClipsUploader")
today = (str)(date.today())
txtfile = "exceptionlist_"+today
def writelink(dfpickle, link = "err"):
    if not (os.path.exists(dir+"\\"+txtfile) and os.path.exists(dir+"\\"+dfpickle)):
        print("first time")
        file  = pd.DataFrame({"link": [link]})
        file.to_pickle(dfpickle)
        
    else:
        print("lmfaosf")
        file = pd.read_pickle(dfpickle)
        temp = pd.DataFrame({"link": [link]})
        result = pd.concat([file, temp])
        result.to_pickle(dfpickle)
        result.to_csv(txtfile)
    #print(file)



    
    
