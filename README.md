
# PhD Thesis based on bookdown and cleanthesis

This repository contains my PhD thesis. It is written in [R Markdown](https://github.com/rstudio/Rmarkdown) and [bookdown](https://github.com/rstudio/bookdown). The layout is mainly based on [cleanthesis](https://github.com/derric/cleanthesis) with small customizations. 

My thesis is available [online](https://ibn-salem.github.io/thesis/) or as download in [PDF](https://ibn-salem.github.io/thesis/thesis.pdf) or [e-book](https://ibn-salem.github.io/thesis/thesis.epub) format.

Comments are welcome!

## Build your own thesis

The applied layout affects only the PDF version. If you want to use it for your own thesis or book project, find bellow some guides for customizations.

### Content 

To update just the content of the book, simply rename and modify the source .Rmd files according to your needs. 

### Cleanthesis layout

[Cleanthesis](https://github.com/derric/cleanthesis) is *a clean LaTeX style for thesis documents* created by Ricardo Langner.
To learn more about available options and modifications read the [cleanthesis documentation](https://github.com/derric/cleanthesis/blob/master/doc/cleanthesis-doc.pdf) and apply changes accordingly.

### Title page

Metadata variable such as title, university, and reviews can be modified in the file `preamble.txt`.
This template contains two different kinds of title pages. You can modify or remove them in the latex file `titlepage.tex`.

- The actual title page and second page are completely customized according to the requirements of my university. 
- The other title page (actual third page) is the title page according to the cleanthesis package. 

## Further resources

- [R Markdown](https://github.com/rstudio/Rmarkdown)
- [bookdown](https://github.com/rstudio/bookdown)
- [cleanthesis](https://github.com/derric/cleanthesis)

