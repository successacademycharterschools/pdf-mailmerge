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

dir = 'html'

def pdf(directory):

    renders = []

    for root, dirs, files in os.walk(dir):
        if not dirs:
            for file in files:
                renders.append({"directory": root,
                                "filename": file})

    for render in tqdm(renders):

        # Windows uses back slashes
        # Use os.path.join Join method
        in_path_filename = render["directory"] + "/" + render["filename"]

        out_path = "pdfs/" + render["directory"].replace(dir, "")
        out_path_filename = out_path + "/" + render["filename"].replace('html', 'pdf')

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
     pdf(dir)
