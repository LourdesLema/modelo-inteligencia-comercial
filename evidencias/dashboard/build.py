from pathlib import Path
p=Path(__file__).parent
text=(p/'template_v02.html').read_text()
(p/'dist').mkdir(exist_ok=True)
(p/'dist/index.html').write_text(text.replace('__DATA__',(p/'data.json').read_text().replace('</','<\\/')))
