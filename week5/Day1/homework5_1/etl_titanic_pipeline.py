import pandas as pd

df = pd.read_csv('/home/user/Documents/coding_temple/week5/day1/homework5_1/titanic.csv')
df.columns = df.columns.str.lower()
df.columns = df.columns.map(lambda x : x.replace('.', '_').replace(' ', '_'))
df.columns = df.columns.str.strip()
con = 'postgresql://kneuyrwx:vY9XtUr7Exgazfi0Of_3RZ5strw35xt2@batyr.db.elephantsql.com/kneuyrwx'
df.to_sql('titanic',con = con, schema = None, if_exists='replace')