import pandas as pd
import utils

product_data = pd.read_excel('./test_data.xls')

categories = product_data['Category'].unique()
nested_product_list = {k:product_data[product_data['Category']==k].T.to_dict() for k in categories}

template = utils.get_template('./example1_template.tex')
variable_dict = {'products': nested_product_list}
utils.compile_pdf_from_template(template, variable_dict, './ex1.pdf')
