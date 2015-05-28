import re
import os
import shutil

project = "./"
in_file = "{}example.txt".format(project)
build_d = "{}.build/".format(project)
out_file = "{}template".format(build_d)
template = "test"


current_object = None
current_content = ""
latex_formated_variables = ""

with open(in_file) as f:
    content = f.read()
    keys = re.findall(r"%(.+):", content)
    values = re. findall(r":\s*([\w\W]+?)\s*(?:%|$)", content)

options = zip(keys, values)

tex_code = ""
for key, value in options:
    tex_code = tex_code + "\\newcommand{{\\{}}}{{{}}}\n".format(key, value)
tex_code = tex_code + """

\\documentclass{{{}}} % din a4, 11 pt, one-sided,

\\begin{{document}}

\\end{{document}}
""".format(template)

if not os.path.exists(build_d):  # create the build directory if not exisiting
    os.makedirs(build_d)

with open(out_file+".tex", "w") as f:  # saves tex_code to outpout file
    f.write(tex_code)

os.system("pdflatex -output-directory {} {}".format(os.path.realpath(build_d), os.path.realpath(out_file)))

shutil.copy2(out_file+".pdf", os.path.dirname(os.path.realpath(in_file)))
