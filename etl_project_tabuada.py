import pandas as pd

# EXTRACTING
source_file = r"C:\Users\Temp\Desktop\dio\santander\etl_project.csv"

df = pd.read_csv(source_file)


# TRANSFORMING
df['do_1'] = df['Tabuada'] * 1
df['do_2'] = df['Tabuada'] * 2
df['do_3'] = df['Tabuada'] * 3
df['do_4'] = df['Tabuada'] * 4
df['do_5'] = df['Tabuada'] * 5
df['do_6'] = df['Tabuada'] * 6
df['do_7'] = df['Tabuada'] * 7
df['do_8'] = df['Tabuada'] * 8
df['do_9'] = df['Tabuada'] * 9


# LOADING
target_file = r"C:\Users\Temp\Desktop\dio\santander\etl_project_final.csv"

df.to_csv(target_file, index=False)

print("ETL completo! Sua tabuada do 1 ao 9 está pronta.")