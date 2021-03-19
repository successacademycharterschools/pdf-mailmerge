import os
import re
import json
import base64
from jinja2 import Environment, FileSystemLoader, select_autoescape

def create_filename(scholar_id, parent_email, main_office_email, principal):
    """
    Creates base64 encoded file name for report cards and
    progress reports

    :param scholar_id: (str, or int) scholar id
    :param parent_email: (str) parent's email address
    :param main_office_email: (str) school's main office email address
    :returns: (str) base64 encoded filename with '.html'
    """
    filename = base64.b64encode(
        json.dumps({'scholar_id': scholar_id,
                    'recipient': parent_email,
                    'sender': main_office_email,
                    'principallastname': principal.replace(' ', '+')
                   })
        .replace(' ', '')
        .encode('utf-8'))
    return str(filename, 'utf-8')


def populate_jinja_template(scholar_id, parent_email, main_office_email,
                            principal, template, rc_data, directory=None):
    """
    Takes inputs, and creates an html file based on a template.
    """

    # process report cards with jinja2
    this_dir = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists('generated'):
        os.makedirs('generated')

    if directory:
        if not os.path.exists(f'generated/{directory}'):
            os.makedirs(f'generated/{directory}')

        file_loc = f'generated/{directory}/{filename}.html'

    else:
        file_loc = f'generated/{filename}.html'


    env = Environment(loader=FileSystemLoader(this_dir),
                      autoescape=select_autoescape(['html', 'xml']))

    if not os.path.exists('generated'):
        os.makedirs('generated')

    if not os.path.exists(f'generated/{directory}'):
        os.makedirs(f'generated/{directory}')

    file_loc = f'generated/{directory}/{filename}.html'

    env.get_template(template)\
        .stream(rc_data)\
        .dump(file_loc)
