
import pandas as pd
# CREATED BY BISWARUP BHATTACHARJEE
def dataFetchAndCatagories(shtno):



    pd_xl_file = pd.ExcelFile("DemoExcel.xlsx")
    df = pd_xl_file.parse(shtno)

    print("\n--------------------------------------------------------------------------------->\n")
    c = 0
    Data = []
    for i in range(1, df.shape[0]):

        if (c == 3):
            c = 0
            cleanlist = [x for x in list(df.loc[0]) if str(x) != 'nan']
            cleanlist1 = [x for x in list(df.loc[i - 3]) if str(x) != 'nan']
            cleanlist2 = [x for x in list(df.loc[i - 2]) if str(x) != 'nan']
            cleanlist3 = [x for x in list(df.loc[i - 1]) if str(x) != 'nan']
            a = "Stream: - " + cleanlist1[0] + " & Subject : - "
            cleanlist1.pop(0)
            for j in range(len(cleanlist1)):
                cleanlist1[j] = a + cleanlist1[j]

            cleanlist1.pop(0)
            cleanlist2.pop(0)
            cleanlist3.pop(0)
            zip1 = zip(cleanlist, cleanlist1, cleanlist2, cleanlist3)
            mainlist = list(zip1)
            Data = Data + mainlist
            # print(mainlist)
            """
            print(len(cleanlist1), cleanlist1)
            print(len(cleanlist2), cleanlist2)
            print(len(cleanlist3), cleanlist3)
            """
            # print("\n--------------------------------------------------------------------------------->\n")
        c = c + 1
        if (i == df.shape[0] - 1):
            i = i + 1
            cleanlist = [x for x in list(df.loc[0]) if str(x) != 'nan']
            cleanlist1 = [x for x in list(df.loc[i - 3]) if str(x) != 'nan']
            cleanlist2 = [x for x in list(df.loc[i - 2]) if str(x) != 'nan']
            cleanlist3 = [x for x in list(df.loc[i - 1]) if str(x) != 'nan']
            cleanlist1.pop(0)
            for j in range(len(cleanlist1)):
                cleanlist1[j] = a + cleanlist1[j]
            cleanlist1.pop(0)
            cleanlist2.pop(0)
            cleanlist3.pop(0)
            zip2 = zip(cleanlist, cleanlist1, cleanlist2, cleanlist3)
            mainlist2 = list(zip2)
            Data = Data + mainlist2
            # print(mainlist2)
            """
                 print(len(cleanlist1), cleanlist1)
                 print(len(cleanlist2), cleanlist2)
                 print(len(cleanlist3), cleanlist3)
            """
    print("DATA:-", len(Data), Data)
    print("\n--------------------------------------------------------------------------------->\n")
    return Data
