#!/usr/bin/env python3
"""Infer the selected limit from rendered ink, independently of the authoring function."""
from pathlib import Path
import re
import subprocess
import tempfile
from PIL import Image
from pypdf import PdfReader
from pypdf.generic import ContentStream
ROOT=Path(__file__).resolve().parents[1]

def main():
    folder=ROOT/'eval/05_caldera_formular';pdf=folder/'02_decizie.pdf'
    reader=PdfReader(pdf);assert len(reader.pages)==1 and not reader.get_fields()
    page=reader.pages[0]
    boxes=[]
    for operands,operation in ContentStream(page.get_contents(),reader).operations:
        if operation==b're':
            x,y,width,height=map(float,operands)
            if 10<=width<=25 and 10<=height<=25:boxes.append((x,y,width,height))
    boxes.sort(key=lambda b:-b[1]);assert len(boxes)==2
    text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    limits=[int(x.replace('.','')) for x in re.findall(r'([\d.]+) EUR fara TVA',text)]
    assert len(limits)==2
    with tempfile.TemporaryDirectory(prefix='pdf-oracle-',dir=ROOT/'.work') as t:
        prefix=Path(t)/'render'
        subprocess.run(['pdftoppm','-singlefile','-r','144','-gray','-png',str(pdf),str(prefix)],check=True)
        img=Image.open(str(prefix)+'.png').convert('L');pageheight=float(page.mediabox.height);scale=2
        marks=[]
        for x,y,w,h in boxes:
            crop=img.crop((round((x+3)*scale),round((pageheight-y-h+3)*scale),round((x+w-3)*scale),round((pageheight-y-3)*scale)))
            marks.append(sum(pixel<100 for pixel in crop.getdata()))
    checked=[i for i,ink in enumerate(marks) if ink>10]
    assert len(checked)==1 and marks[0]==0,marks
    limit=limits[checked[0]]
    mandate=(folder/'01_mandat.md').read_text()
    requested=int(re.search(r'tranșe de ([\d.]+) EUR',mandate)[1].replace('.',''))
    assert limit==60000 and requested==80000 and requested-limit==20000
    print(f'OK: static PDF, one page; checkbox interior ink={marks}; selected limit={limit}; request={requested}; excess={requested-limit}. Plain text contains both values but no checkbox state.')
if __name__=='__main__':main()
