"""Crop an exact-size shared background; never silently resize."""
import argparse
from pathlib import Path
from PIL import Image
p=argparse.ArgumentParser()
p.add_argument('input');p.add_argument('output_dir');p.add_argument('--width',type=int,required=True);p.add_argument('--height',type=int,required=True);p.add_argument('--pages',type=int,required=True)
a=p.parse_args()
if min(a.width,a.height,a.pages)<=0:p.error('dimensions and pages must be positive')
im=Image.open(a.input)
if im.size!=(a.width*a.pages,a.height):p.error('input must equal page width * pages by page height; no implicit resize')
out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
paths=[out/f'page-{i+1:02d}.png' for i in range(a.pages)]
if any(x.exists() for x in paths):p.error('output exists; use a fresh directory')
for i,path in enumerate(paths):im.crop((i*a.width,0,(i+1)*a.width,a.height)).save(path)
print(f'Created {a.pages} background slices; visually check seams before delivery.')
