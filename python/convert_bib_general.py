"""
Read markdown with references and convert it into proper lables
Example reference:

81. Miller, D.T., Adam, M.P., Aradhya, S., Biesecker, L.G., Brothman,
A.R., Carter, N.P., Church, D.M., Crolla, J.A., Eichler, E.E., Epstein,
C.J., et al. (2010). Consensus statement: chromosomal microarray is a
first-tier clinical diagnostic test for individuals with developmental
disabilities or congenital anomalies. Am J Hum Genet 86, 749-764.


"""

import argparse # reads commandline arguments
import re

def commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=str, required=True, help="input file.")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="output file")
    parser.add_argument("-r", "--ref_title", type=str, default = "**References**")
    parser.add_argument("-nt", "--next_title", type=str, default = "1.  Tables")
    parser.add_argument("-in", "--intro_name", type=str, default = "**Introduction**")
    parser.add_argument("-ss", "--separater_str", type=str, default = ",\\ ")
    return parser.parse_args()



def read_references(infile, ref_title, next_title) :
    """
    returns an dictionary with numbers mapping to AuthorYear string.
    """
    lines = []
    d = {}

    # # in reference section
    content = open(infile).read()
    refPart = content.split(ref_title + "\n", 1)[1]
    # split to take part before next tile as references
    refPart = refPart.split(next_title)[0]

    # remove span blocks
    refPart = re.sub("<span .*?</span>", "", refPart)

    # mark double line breaks
    refPart = re.sub("\n\n", "NEXTREF", refPart)

    # remove single line breaks
    refPart = re.sub("\n", "", refPart)
    # print("DEBUG HEEEEERE THE REFS:")
    # print(refPart[0:1000])

    # join line into one string
    refs = refPart.split("NEXTREF")
    print(refPart[0:6])

    # iterate across references
    for ref in refs:
      # text = 'gfgfdAAA1234ZZZuijjk'

      try:
        # extract number
        number = re.search('^(\d+)(\\\)?\. ?', ref).group(1)
        print("number", number)
        # extract first author:
        author = re.search('^\d+(\\\)?\. ?(.*?) ', ref).group(2)
        print("author", author)

        # extract year
        year = re.search('[ .;](\d{4})[;|. ]', ref).group(1)

        print("number, author, year:")
        print(number, author, year)
        d[number] = author + year

      except AttributeError:
        # AAA, ZZZ not found in the original string
        found = '' # apply your error handling
        print(ref)
        print("WARNING! could not parse reference above")

    return(d)

def write_references_table(infile, mapping):
  with open(infile + ".reference_table.txt", 'w') as outHandle:
    for key in mapping:
      outHandle.write(key + "\t" + mapping[key] + "\n")

def parse_range(in_str, separater_str):
    from_str = in_str.split('\xe2\x80\x93')[0]
    to_str = in_str.split('\xe2\x80\x93')[1]
    print(from_str + "|" + to_str)
    out_str = separater_str.join([str(i) for i in range(int(from_str), int(to_str))])
    return(out_str)

def replace_refs(content, mapping, intro_name, separater_str):

  def my_repl(match):

    print("HERE: =====")
    print match.group(0)
    numbers_str = match.group(0).strip("^").strip("\[").strip("\]")
    print(numbers_str)

    # handle range of keys: 1-8
    # if "-" in numbers_str:
    #   from_str = numbers_str.split("-")[0]
    #   to_str = numbers_str.split("-")[1]
    #   print(from_str + "|" + to_str)
    #   numbers_str = ",\\ ".join([str(i) for i in range(int(from_str), int(to_str))])

    numbers_str = numbers_str.replace("\\\\", "\\")
    print(numbers_str)
    numbers = numbers_str.split(",")
    print("Splitted:")
    print(numbers)
    numbers = [parse_range(n, separater_str) if ('\xe2\x80\x93' in n or "-" in n) else n for n in numbers]
    print(numbers)
    # combine list, if parts are rnage and other parts just numbers
    numbers = separater_str.join(numbers).split(separater_str)
    print(numbers)
    mapped_keys = ["@" + mapping[n.strip(";")] for n in numbers]
    print(mapped_keys)

    keys_str = "[" + "; ".join(mapped_keys) + "]"
    print(keys_str)

    return keys_str

  # split by Introduction header
  before_intro =  content.split(intro_name, 1)[0]
  after_intro = content.split(intro_name, 1)[1]

  # pattern = "(\^\d+.*?\^)"
  pattern = "\\\\\[(\d+.*?)\]"
  converted_content = re.sub(pattern, my_repl, after_intro)

  # remove everything after section References
  converted_content = converted_content.split("**References**", 1)[0]

  # put parts together
  result_content = before_intro + "**Introduction**" + converted_content

  return(result_content)


def remove_span(content):
  pattern = "<span .*?</span>"
  converted_content = re.sub(pattern, "", content)
  return(converted_content)


if __name__ == "__main__":

    # read commandline argumets
    args = commandline()

    mapping = read_references(args.input_file, args.ref_title, args.next_title)

    write_references_table(args.input_file, mapping)

    with open(args.input_file) as inHandle:
      content = inHandle.read()

    content = remove_span(content)
    content = replace_refs(content, mapping, args.intro_name, args.separater_str)

    with open(args.output_file, 'w') as outHandle:
      outHandle.write(content)

