#!/bin/sh

# build html version
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

# build pdf version
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book', clean = FALSE)"

# build epub version
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book', clean = FALSE)"
