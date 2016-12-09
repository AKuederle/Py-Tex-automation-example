import re
import os
import shutil

import argparse


parser = argparse.ArgumentParser(description='Render a LaTex Template with variables.')

parser.add_argument('-i','--in', help='Input File', required=False, default='./example.txt' )
parser.add_argument('-t','--template', help='Template File', required=False, default='./template.tex')
args = vars(parser.parse_args())


project = "./"
in_file = args['in']
build_d = "{}.build/".format(project)
template_file = args['template']
out_file = "{}renderer_template".format(build_d)


current_object = None
current_content = ""
latex_formated_variables = ""

with open(in_file) as f:
    content = f.read()
    keys = re.findall(r"%(.+):", content)
    values = re. findall(r":\s*([\w\W]+?)\s*(?:%|$)", content)

options = dict(zip(keys, values))

######
# modified from http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
import jinja2
import os
from jinja2 import Template
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template(template_file)
######

renderer_template = template.render(**options)

if not os.path.exists(build_d):  # create the build directory if not exisiting
    os.makedirs(build_d)

with open(out_file+".tex", "w") as f:  # saves tex_code to outpout file
    f.write(renderer_template)


os.system('pdflatex -output-directory {} {}'.format(os.path.realpath(build_d), os.path.realpath(out_file + '.tex')))

shutil.copy2(out_file+".pdf", os.path.dirname(os.path.realpath(in_file)))
