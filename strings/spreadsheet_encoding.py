from test_framework import generic_test


"""
Spreadsheets often use an alphabetical encoding of the successive columns. Specifically, columns are identified by 
"A',"B","C",,,,,"X","Y","Z","AA',"AB",.,.,"ZZ","AAA',"AAB",.,..
Implement a function that converts a spreadsheet column id to the corresponding integer, 
with "A" corresponding to 1. For example, you should return 4 for "D" ,27 for " AA' ,702 for "ZZ" , etc.
"""


def ss_decode_col_id(col: str) -> int:
    symbol_map = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    col_id = 0
    for i in range(0, len(col)):
        col_id = col_id * 26 + symbol_map.index(col[i])

    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
