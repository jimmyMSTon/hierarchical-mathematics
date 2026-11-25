#!/usr/bin/env python3
"""Embed Adobe-GB1 Unicode CMaps without modifying page contents or fonts.
Usage: python fix_unicode.py input.pdf output.pdf [path/to/Adobe-GB1-UCS2]
Requires PyMuPDF and poppler-data (or Adobe's equivalent CMap).
"""
import argparse
from pathlib import Path
import fitz

def patch(source, dest, cmap_path):
    cmap = Path(cmap_path).read_bytes()
    if b'/CMapName /Adobe-GB1-UCS2' not in cmap or b'beginbf' not in cmap:
        raise ValueError('Expected Adobe-GB1-UCS2 CMap')
    doc = fitz.open(source)
    candidates = set()
    for page in doc:
        for font in page.get_fonts():
            xref = font[0]
            if doc.xref_get_key(xref, 'Subtype')[1] != '/Type0':
                continue
            if doc.xref_get_key(xref, 'ToUnicode')[0] != 'null':
                continue
            if doc.xref_get_key(xref, 'Encoding')[1] != '/Identity-H':
                continue
            if 'Fandol' not in font[3]:
                continue
            descendants = doc.xref_get_key(xref, 'DescendantFonts')[1]
            import re
            match = re.fullmatch(r'\[\s*(\d+)\s+0\s+R\s*\]', descendants)
            if not match:
                raise ValueError('Unexpected descendant font structure')
            cid = doc.xref_get_key(int(match.group(1)), 'CIDSystemInfo')[1]
            if not (re.search(r'/Registry\s*\(Adobe\)', cid) and re.search(r'/Ordering\s*\(GB1\)', cid)):
                raise ValueError('Expected Adobe-GB1 CID collection')
            candidates.add(xref)
    if candidates:
        stream = doc.get_new_xref()
        doc.update_object(stream, '<< >>')
        doc.update_stream(stream, cmap, compress=True)
        for xref in sorted(candidates):
            doc.xref_set_key(xref, 'ToUnicode', f'{stream} 0 R')
    doc.save(dest, garbage=0, deflate=True)
    doc.close()
    print(f'Added Unicode maps to {len(candidates)} fonts.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('cmap', nargs='?', default='/usr/share/poppler/cMap/Adobe-GB1/Adobe-GB1-UCS2')
    args = parser.parse_args()
    patch(args.input, args.output, args.cmap)
