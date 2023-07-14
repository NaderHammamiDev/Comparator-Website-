import json
import pdfplumber
import pandas as pd



def read_json(path):
  
    # Opening JSON file
    f = open(path,encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    f.close()
    # Closing file
    
    return data


def Read_Pdf_Bank(pdf_path):
        data_frames = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    data_frames.append(df)
            return df ,data_frames
        
        
def Read_Zitouna_Bank(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text 


def Read_BT_Bank(pdf_path):
    data_frames = []

    # Définir la largeur maximale de colonne
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.max_rows", None)

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                data_frames.append(df)
    return df, data_frames



       