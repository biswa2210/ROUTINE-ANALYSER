from accessXlsx import dataFetchAndCatagories
from GUI_RESULT_DISPLAY import result
def Searching(f_id,sheetNo):
    dataForSearch=dataFetchAndCatagories(sheetNo)
    s=f_id
    Output=[]
    for item in dataForSearch:
        if (str(item[2]).lower().find(s.lower()) == -1):
            continue
        else:
            Output.append(item)
    print(len(Output),Output)
    result(Output,sheetNo)