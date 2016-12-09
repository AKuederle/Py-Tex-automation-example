import re
import os
import shutil

project = "./"
in_file = "{}example.txt".format(project)
build_d = "{}.build/".format(project)
out_file = "{}renderer_template".format(build_d)
template = "test"


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
template = latex_jinja_env.get_template('template.tex')
######

renderer_template = template.render(**options)

if not os.path.exists(build_d):  # create the build directory if not exisiting
    os.makedirs(build_d)

with open(out_file+".tex", "w") as f:  # saves tex_code to outpout file
    f.write(renderer_template)


os.system('pdflatex -output-directory {} {}'.format(os.path.realpath(build_d), os.path.realpath(out_file + '.tex')))

shutil.copy2(out_file+".pdf", os.path.dirname(os.path.realpath(in_file)))
