import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/EmployeeDB')
df = pd.read_excel(r'EmployeeSample.xlsx')
df.to_sql(name='employee', con=engine, if_exists = 'replace', index=False)

listnum = list(range(1, 1000001))
listnum = ["E"+str(l) for l in listnum]
data = pd.DataFrame(listnum)
data.to_excel("e.xlsx")
