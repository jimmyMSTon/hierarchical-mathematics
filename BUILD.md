# Build and verify the manuscripts

The manuscript sources are UTF-8 LaTeX and contain their own bibliography and TikZ drawings. No proprietary fonts, external figures or bibliography files are required. Version 1.0.1 uses the original v1.0.0 manuscript sources, with a PDF-only Chinese Unicode-map repair. No mathematical content changed.

## Reference environment

TeX Live 2025/dev (Debian), pdfTeX 1.40.26 for English, XeTeX / xdvipdfmx for Chinese. A sufficiently complete current TeX Live distribution (or MacTeX) can provide the required packages. On Debian/Ubuntu, the following is an example:

```sh
sudo apt-get install latexmk texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-pictures texlive-xetex texlive-lang-chinese poppler-utils poppler-data
python3 -m venv .venv
. .venv/bin/activate
python -m pip install PyMuPDF
```

English packages include geometry, fontenc, lmodern, amsmath, amssymb, amsthm, mathtools, booktabs, tabularx, TikZ, xcolor, hyperref and microtype. Chinese additionally uses ctexart (Fandol), array, fancyhdr and enumitem. TeX Live provides the required Fandol fonts; no additional font download is needed for reading the published PDFs.

From the repository root:

```sh
mkdir -p build/en build/zh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build/en source/Paradigm_EN.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build/zh source/Paradigm_ZH.tex
python tools/fix_unicode.py build/zh/Paradigm_ZH.pdf build/zh/Paradigm_ZH_unicode.pdf
```

On platforms where the Adobe CMap is not installed at the default Debian path, pass the explicit path to the standard Adobe-GB1-UCS2 map from Poppler data as the last argument. The script adds ToUnicode maps only to missing Fandol Adobe-GB1 Identity-H font dictionaries. It does not rasterize pages, change page contents or replace fonts. If the compiler already generated those maps, no repair is needed.

## Verify the published artifacts

```sh
sha256sum -c SHA256SUMS
pdffonts paper/Paradigm_EN.pdf
pdffonts paper/Paradigm_ZH.pdf
pdftotext paper/Paradigm_ZH.pdf -
```

On macOS use `shasum -a 256 -c SHA256SUMS` instead of sha256sum. Each listed published font is embedded and has a Unicode map. The repair was tested with Poppler, PyMuPDF and pypdf; rendering was compared at 144 dpi using MuPDF. Exact PDF byte reproduction is not promised across TeX versions, timestamps, font subsets and operating systems. SHA256SUMS verifies the actual released files, not independently rebuilt files. Selectable text does not constitute full PDF/UA tagging or screen-reader certification; the LaTeX source is an additional machine-readable representation.

## Licensing

The manuscripts, original research documentation and original repair script retain the author's CC BY 4.0 publication license. The embedded standard Adobe-GB1 CMap retains its own upstream copyright and license notice; the script uses a separately installed CMap, not a distributed font file.
