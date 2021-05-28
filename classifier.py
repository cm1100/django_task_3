import t2
import  pandas as pd
import numpy as np
from pprint import pprint
import main2

#df = pd.read_csv("results1.csv")




interests = t2.get_interests()


#list_latest = df.T.to_dict().values()
#print(list_latest)



def classify_add(results):
    for x in results:
        list_intereset=[]
        for i in interests:
            k=False
            for m in i.split():
                if m in x['description']:
                    k=True
            if k==True:
                list_intereset.append(i)

        if(list_intereset):
            x["classification"]=str(list_intereset)
        else:
            x["classification="]="None"

    return results

















