# pdf-mailmerge


Mailmerge to a pdf or html file. Adds csv data to an html jinja template.
Can be configured to generate filenames and subdirectories as well as sort order from columns in the csv.

## Install

```
pip install pdf-mailmerge
```

## Usage

Requires a `config.yml` file in your directory containing:

```
data: Some.csv

template: "Some_jinja.html"

identifier_columns:
  - "col1"
  - "col2"

filename_columns:
  - "col3"
  - "col4"

output_folders:
  - "col1"
  - "col5"

sort:
  - "col2"
  - "col3"
```

#### Required Configuration Fields

`data`: csv file with the data you wish to mailmerge

`template`: jinja template being used for the mailmerge

`identifier_columns`: columns used to construct a primary key for the data. If a column already contains the primary key, list it but only it. A mailmerge document will be created for every unique value or unique value combination of the identifier columns.

`filename_columns`: columns used to construct the filename for the document. Name will be "col1_col2_" etc.

#### Optional Configuration Fields

`output_folders`: columns used to construct output subdirectories. All files placed in either `html` or `pdf` directory. Additional folder nesting levels based on order of output folders. Sample file path `pdf/col1/col5`. 

`sort`: columns used to sort documents within their output folder. If multiple options, sort precedence given in order of list.
