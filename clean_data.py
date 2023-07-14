from MyDataLoader import MyDataLoader

def clean_data():
    filename = 'products2.json'
    bank_name = 'Attijari'
    pdf_path ="pdf_file/Barème_des_conditions_de_banque_Mars_2023.pdf"
    data_object = MyDataLoader(filename, bank_name)
    data_object.display_data()
    data_object.load_data(pdf_path,filename)