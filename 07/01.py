import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_account_file='green-objective-423403-j9-38810ef79733.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1RsYRscmApXM30zvEtunxnnIco9Ez7tKxtHEMREknHxc/'


sh = gc.open_by_url(survey_url)

ws = sh.worksheet_by_title('chu')
ws.update_value('A1', '中華大學')
ws.update_value('B1', '影像處理')
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
ws.set_dataframe(df1, 'A3', copy_index=True, nan='')