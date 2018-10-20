#import HTMLParser
#from html.parser import HTMLParser
import html
import unicodedata
from unidecode import unidecode

#htmlparser = HTMLParser.HTMLParser()

def is_ascii(s):
        return all(ord(c) < 128 for c in s)

def clean_parsed_string(string):
    if len(string) > 0:
        ascii_string = string
        if is_ascii(ascii_string) == False:
            #ascii_string = unicodedata.normalize('NFKD', ascii_string).encode('ascii', 'ignore')
            #ascii_string = unicodedata.normalize('NFKD', ascii_string)
            #print(unidecode(ascii_string))
            ascii_string = unidecode(ascii_string)
            #print(ascii_string)
            # for norm in ('NFC', 'NFKC', 'NFD','NFKD'):
            #     #b = unicodedata.normalize(norm, ascii_string).encode('ascii', 'ignore')
            #     b = unicodedata.normalize(norm, ascii_string).encode('utf-8')
            #     print(b, len(b))
        return str(ascii_string)
    else:
        return None

def get_parsed_string(sel, xpath):
    return_string = ''
    raw_string = sel.xpath(xpath).extract_first()
    if raw_string is not None:
        return_string = html.unescape(raw_string)
    return return_string

def get_parsed_review_element(raw_review, xpath):
    return_string = ''
    extracted_list = raw_review.select(xpath).extract()
    if len(extracted_list) > 0:
        raw_string = extracted_list[0].strip()
        if raw_string is not None:
            return_string = htmlparser.unescape(raw_string)
        return return_string