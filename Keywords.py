#!/usr/bin/env python
# coding: utf-8

import io
import sys
import codecs
import importlib
from textrank4zh import TextRank4Keyword, TextRank4Sentence
importlib.reload(sys) 
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def parse():
    fp = open(path, 'rb') 
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in doc.get_pages(): 
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('/Users/liamtheron/Desktop/Deloiite/test.txt', 'a') as f:
                        results = x.get_text()
                        f.write(results) 
                        f.write('\n')

def Keyword():
    text=codecs.open('/Users/liamtheron/Desktop/Deloiite/test.txt','r',encoding='utf-8').read()
    tr4w = TextRank4Keyword()
    tr4s = TextRank4Sentence()
    tr4w.analyze(text=text, lower=True, window=2)
    tr4s.analyze(text=text, lower=True)
    print( '<关键词>：' )
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)
    print()
    print( '<关键短语>：' )
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
        print(phrase)
    print()
    print( '<摘要>：' )
    for item in tr4s.get_key_sentences(num=3):
        print(item.index, item.weight, item.sentence)

if __name__ == '__main__':
    path = '/Users/liamtheron/Desktop/Deloiite/test.pdf'
    parse()
    Keyword()
