from helper import read_json
from helper import Read_Pdf_Bank
import json

class MyDataLoader:

    def __init__(self, json_file, bank_name):
        all_bank_data = read_json(json_file)
        bank_data = list(filter(lambda x: (x['bank'] == bank_name), all_bank_data))
        self.bank_data = bank_data
        
    def display_data(self):
        print(self.bank_data)

    def load_data(self, pdf_file,json_file):
        # Load and process the data
        df, data_frames = Read_Pdf_Bank(pdf_file)

        # Iterate over each DataFrame
        for df_number, df in enumerate(data_frames):
            df.set_index(df.columns[1], inplace=True)
            print(df)
            try:
                row_number = df.index.get_loc('Pack Bledi+')
                print(df_number)
                print(row_number)
                print(df.iloc[row_number])

                # Update the 'Ligne' field in the JSON data
                self.bank_data[row_number-1]['Row'] = str(row_number)
                self.bank_data[row_number-1]['Table Number'] = str(df_number)

                break
            except:
                pass

        # Write the updated data back to the JSON file
        with open(json_file, 'w',encoding='utf-8') as file:
            json.dump(self.bank_data, file, indent=4,ensure_ascii=False)




