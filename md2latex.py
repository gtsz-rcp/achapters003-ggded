import os
import pypandoc
from pypandoc.pandoc_download import download_pandoc

manuscript_dir = os.path.join(os.getcwd(), 'manuscript')
manuscripts = os.listdir(manuscript_dir)
latex_dir = os.path.join(manuscript_dir, 'latex')

os.makedirs(latex_dir, exist_ok=True)

for file in manuscripts:
    if file.split('.')[-1] != 'md':
        continue

    filepath = os.path.join(manuscript_dir, file)
    output = pypandoc.convert_file(filepath, 'latex')

    output_path = os.path.join(manuscript_dir, 'latex', file).split('.');
    output_path[-1] = 'tex'
    output_path = '.'.join(output_path)

    f = open(output_path, 'w', encoding='utf-8')
    f.write(output)
    f.close()
    print(f)
