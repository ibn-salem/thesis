"""
Reads a .bib file and several Rmarkdown files and removes all non-cited entries
from the .bib file.

"""

import argparse # reads commandline arguments
import re, glob, os

def commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=str, required=True, help="input .bib file.")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="output .bib file")
    parser.add_argument("-rmd", "--rmd_files", type=argparse.FileType('r'), nargs='+')
    return parser.parse_args()

def read_citations(rmd_files) :
    """
    retunrs a set of all citation keys in input files.
    """
    cite_keys = set()

    for file in rmd_files:
      content = file.read()
      keys = re.findall("(@[a-zA-Z0-9_]+)[\] ;]", content)

      cite_keys |= set(keys)

    print "INFO: Read", len(cite_keys), "citation keys from markdown file(s)."
    return cite_keys

def filter_bib(input_file, cite_keys, output_file):
  """
  filteres input .bib file for only keys contained in cite_keys and
  writes it to ouput .bib file.
  """

  contained = False
  counter = 0
  counter_all = 0

  with open(output_file, "w") as outHandle:

    with open(input_file) as inHandle:

      for line in inHandle.readlines():

        if line.startswith("@"):

          key = re.findall("@\w+\{([a-zA-Z0-9_-]+),$", line.strip())
          # print "Debug: line:", line.strip()
          # print "Debug: key:", key
          if not key:
            print "Warning: Could not read key from this line: ", line.strip()
            contained = False
          else:
            contained = ("@" + key[0]) in cite_keys

            counter += contained

          counter_all += 1

        if contained:
          outHandle.write(line)

  print "INFO: found ", counter, "of", counter_all, "matching citations in input .bib file."

if __name__ == "__main__":

    # read commandline argumets
    args = commandline()

    cite_keys = read_citations(args.rmd_files)

    filter_bib(args.input_file, cite_keys, args.output_file)
