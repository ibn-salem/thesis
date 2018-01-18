#!/usr/bin/env python

"""
despan.py
Pandoc filter to convert all regular text to uppercase.
Code, link URLs, etc. are not affected.
"""

from pandocfilters import toJSONFilter, Str

def despan(key, value, format, meta):
  if key == 'Span':
    return []

if __name__ == "__main__":
  toJSONFilter(despan)
