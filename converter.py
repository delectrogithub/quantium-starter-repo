import pandas as pd
import datetime

df = pd.read_csv('./pmsales.csv')
df = df.reset_index()
datapermonth = {
'022018' : [0, 0],
'032018' : [0, 0],
'042018' : [0, 0],
'052018' : [0, 0],
'062018' : [0, 0],
'072018' : [0, 0],
'082018' : [0, 0],
'092018' : [0, 0],
'102018' : [0, 0],
'112018' : [0, 0],
'122018' : [0, 0],
'012019' : [0, 0],
'022019' : [0, 0],
'032019' : [0, 0],
'042019' : [0, 0],
'052019' : [0, 0],
'062019' : [0, 0],
'072019' : [0, 0],
'082019' : [0, 0],
'092019' : [0, 0],
'102019' : [0, 0],
'112019' : [0, 0],
'122019' : [0, 0],
'012020' : [0, 0],
'022020' : [0, 0],
'032020' : [0, 0],
'042020' : [0, 0],
'052020' : [0, 0],
'062020' : [0, 0],
'072020' : [0, 0],
'082020' : [0, 0],
'092020' : [0, 0],
'102020' : [0, 0],
'112020' : [0, 0],
'122020' : [0, 0],
'012021' : [0, 0],
'022021' : [0, 0],
'032021' : [0, 0],
'042021' : [0, 0],
'052021' : [0, 0],
'062021' : [0, 0],
'072021' : [0, 0],
'082021' : [0, 0],
'092021' : [0, 0],
'102021' : [0, 0],
'112021' : [0, 0],
'122021' : [0, 0],
'012022' : [0, 0],
'022022' : [0, 0]}

for index, row in df.iterrows():
    dateofpurchase = row['date']
    month = dateofpurchase[5] + dateofpurchase[6]
    year = dateofpurchase[0] + dateofpurchase[1] + dateofpurchase[2] + dateofpurchase[3]
    iden = str(month) + str(year)
    value = datapermonth[iden]
    value[0] = value[0]+ row['sales']
    value[1] = value[1] + 1
    datapermonth.update({iden: value})

for key,value in datapermonth.items():
    meanofsales = value[0]/value[1]
    meanofsales = round(meanofsales)
    datapermonth.update({key: meanofsales})

simplesales = pd.DataFrame(columns=['sales', 'month', 'year'])
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '02', 'year': 2018}, index=[1]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '03', 'year': 2018}, index=[2]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '04', 'year': 2018}, index=[3]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '05', 'year': 2018}, index=[4]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '06', 'year': 2018}, index=[5]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '07', 'year': 2018}, index=[6]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '08', 'year': 2018}, index=[7]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '09', 'year': 2018}, index=[8]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '10', 'year': 2018}, index=[9]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '11', 'year': 2018}, index=[10]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '12', 'year': 2018}, index=[11]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '01', 'year': 2019}, index=[12]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '02', 'year': 2019}, index=[13]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '03', 'year': 2019}, index=[14]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '04', 'year': 2019}, index=[15]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '05', 'year': 2019}, index=[16]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '06', 'year': 2019}, index=[17]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '07', 'year': 2019}, index=[18]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '08', 'year': 2019}, index=[19]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '09', 'year': 2019}, index=[20]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '10', 'year': 2019}, index=[21]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '11', 'year': 2019}, index=[22]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '12', 'year': 2019}, index=[23]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '01', 'year': 2020}, index=[24]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '02', 'year': 2020}, index=[25]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '03', 'year': 2020}, index=[26]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '04', 'year': 2020}, index=[27]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '05', 'year': 2020}, index=[28]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '06', 'year': 2020}, index=[29]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '07', 'year': 2020}, index=[30]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '08', 'year': 2020}, index=[31]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '09', 'year': 2020}, index=[32]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '10', 'year': 2020}, index=[33]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '11', 'year': 2020}, index=[34]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '12', 'year': 2020}, index=[35]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '01', 'year': 2021}, index=[36]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '02', 'year': 2021}, index=[37]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '03', 'year': 2021}, index=[38]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '04', 'year': 2021}, index=[39]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '05', 'year': 2021}, index=[40]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '06', 'year': 2021}, index=[41]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '07', 'year': 2021}, index=[42]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '08', 'year': 2021}, index=[43]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '09', 'year': 2021}, index=[44]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '10', 'year': 2021}, index=[45]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '11', 'year': 2021}, index=[46]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '12', 'year': 2021}, index=[47]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '01', 'year': 2022}, index=[48]), simplesales.loc[:]]).reset_index(drop=True)
simplesales = pd.concat(
    [pd.DataFrame({'sales': 0, 'month': '02', 'year': 2022}, index=[49]), simplesales.loc[:]]).reset_index(drop=True)


for key,value in datapermonth.items():
    for index, row in simplesales.iterrows():
        keyc1 = str(row['month']) + str(row['year'])
        if keyc1 == key:
            row['sales'] = value



simplesales.to_csv('./simplesales.csv')
