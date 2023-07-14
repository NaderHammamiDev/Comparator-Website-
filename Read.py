from helper import Read_Zitouna_Bank
from helper import Read_BT_Bank




"""pdf_file="pdf_file/Conditions Tarifaires Banque Zitouna.pdf"
Text= Read_Zitouna_Bank(pdf_file)
print(Text)
"""


pdf_file="pdf_file/fiche condition 052023vf.pdf"
df, data_frames = Read_BT_Bank(pdf_file)

for df_number, df in enumerate(data_frames):
    print(df)