import t1
import numpy as np
import pandas as pd

import t5








print("trying to finding events in each iteration")




def get_results(links):

    list_results=[]

    m=0

    for i in links:


        print(f"iteration:{m} : {len(list_results)}")
        m+=1
        if len(list_results)==10:
            break


        try:
            data = t1.scrape(i)


            if data is None:
                continue

            if data["@type"]=="Event":
                list_results.append(data)
        except:
            pass





    return list_results




