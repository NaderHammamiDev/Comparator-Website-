from helper import read_json
from helper import Read_Pdf_Bank
import json

class test:
    def __init__(self, filename, bank_name):
        self.filename = filename
        self.bank_name = bank_name

    def display_data(self):
        self.bank_data = read_json(self.filename)
        print(self.bank_data)

    def load_data(self, pdf_path):
        self.bank_data = read_json(self.filename)

        # Load and process the data
        df, data_frames = load_data(pdf_path)

        # Iterate over each DataFrame
        for df_number, df in enumerate(data_frames):
            df.set_index(df.columns[1], inplace=True)
            print(df)
            try:
                row_number = df.index.get_loc('Offre Pro Santé')
                print(df_number)
                print(row_number)
                print(df.iloc[row_number])

                # Find the matching product_name
                for entry in self.bank_data:
                    if entry['product_name'] == 'Offre Pro Santé':
                        # Update the 'Row' and 'Table Number' fields
                        entry['Row'] = str(row_number)
                        entry['Table Number'] = str(df_number)

                break
            except:
                pass

        # Write the updated data back to the JSON file
        with open(self.filename, 'w') as file:
            json.dump(self.bank_data, file, indent=4)
