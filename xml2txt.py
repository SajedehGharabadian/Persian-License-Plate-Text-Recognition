import os
import xml.etree.ElementTree as ET
from pathlib import Path


dict = {
        'الف':'A',
        'ب':'B',
        'پ':'P',
        'ت':'T',
        'ث':'Y',
        'ز':'Z',
        'ش': 'X',
        'ع': 'E',
        'ف': 'F',
        'ک': 'K',
        'گ': 'G',
        'D': 'D',
        'S': 'S',
        'ج': 'J',
        'د': 'W',
        'س': 'C',
        'ص': 'U',
        'ط': 'R',
        'ق': 'Q',
        'ل': 'L',
        'م': 'M',
        'ن': 'N',
        'و': 'V',
        'هـ': 'H',
        'ی': 'I',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'ژ (معلولین و جانبازان)':'@',
}

file_path = 'gt_train.txt'
file = open(file_path,'a')

for filename in os.listdir('train'):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join('train', filename)
    filename = Path(fullname)
    k = 'train/'+filename.stem+'.jpg'
    tree = ET.parse(fullname)
    print(fullname)
    root = tree.getroot()
    file.write(k)
    file.write('\t')
    paragraphs = tree.findall('//name')
    for i in range(1,len(paragraphs)+1):
        a = root[i][0].text
        if a == 'ه‍':
            file.write(dict['هـ'])
        else:
            file.write(dict[a])
    file.write("\n")

print('Finished')