import os
import re
import json
import base64
import pandas as pd
import numpy as np
import yaml
from tqdm import tqdm
from jinja2 import Environment, FileSystemLoader, select_autoescape
import sys
import pdfkit
import argparse

parser = argparse.ArgumentParser(description='produce pdfs of html files in target directory')
parser.add_argument('directory',
                    help= 'directory of html files converted into pdfs',
                    type = str)
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet',
                    help = 'do not display list progress',
                    action = 'store_true')
group.add_argument('-v', '--verbose',
                    help = 'display list progress',
                    action = 'store_true',
                    default = True)
args = parser.parse_args()

def pdf(args):

    renders = []

    dir = args.directory

    for root, dirs, files in os.walk(dir):
        if not dirs:
            for file in files:
                renders.append({"directory": root,
                                "filename": file})

    if args.quiet:
        for render in renders:
            # Windows uses back slashes
            # Use os.path.join Join method
            in_path_filename = os.path.join(render["directory"], render["filename"])

            out_path = os.path.join("pdfs", render["directory"].replace(dir, ""))
            out_path_filename = os.path.join(out_path, render["filename"].replace('html', 'pdf'))

            # create school dir if not exists
            if not os.path.exists(out_path):
                os.makedirs(out_path)

            # only create PDFs that don't exist
            if not os.path.exists(out_path_filename):
                # create pdf
                pdfkit.from_file(in_path_filename,
                                 out_path_filename,
                                 options={'quiet': '',
                                          'page-size': 'A4',
                                          'dpi': 650})

    if args.verbose:
        for render in tqdm(renders):

            # Windows uses back slashes
            # Use os.path.join Join method
            in_path_filename = os.path.join(render["directory"], render["filename"])

            out_path = os.path.join("pdfs", render["directory"].replace(dir, ""))
            out_path_filename = os.path.join(out_path, render["filename"].replace('html', 'pdf'))

            # create school dir if not exists
            if not os.path.exists(out_path):
                os.makedirs(out_path)

            # only create PDFs that don't exist
            if not os.path.exists(out_path_filename):
                # create pdf
                pdfkit.from_file(in_path_filename,
                                 out_path_filename,
                                 options={'quiet': '',
                                          'page-size': 'A4',
                                          'dpi': 650})

if __name__ == "__main__":
     pdf(args)
