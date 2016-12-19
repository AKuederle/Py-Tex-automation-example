import argparse
import utils


parser = argparse.ArgumentParser(description='Render a LaTex Template with variables.')

parser.add_argument('-i','--in', help='Input File', required=False, default='./example.txt' )
parser.add_argument('-t','--template', help='Template File', required=False, default='./template.tex')
args = vars(parser.parse_args())


project = "./"
in_file = args['in']
build_d = "{}.build/".format(project)
template_file = args['template']
out_file = "{}renderer_template.pdf".format(project)

options = utils.get_options_from_file(in_file)

template = utils.get_template(template_file)

utils.compile_pdf_from_template(template, options, out_file)

renderer_template = template.render(**options)
