import os, pypandoc, json
from pypandoc.pandoc_download import download_pandoc

class Bartleby:

    def __init__(self):
        self.manuscript_dir = os.path.join(os.getcwd(), 'manuscript')
        self.manuscripts = list(filter(
            lambda x: os.path.isdir(os.path.join(self.manuscript_dir, x)) == False,
            os.listdir(self.manuscript_dir)
        ))
        self.latex_dir = os.path.join(self.manuscript_dir, 'latex')
        self.toc = [];

        os.makedirs(self.latex_dir, exist_ok=True)


    def markdowntolatex(self):
        result = False

        for file in self.manuscripts:
            if file.split('.')[-1] != 'md':
                continue

            filepath = os.path.join(self.manuscript_dir, file)
            output = pypandoc.convert_file(filepath, 'latex')

            output_path = os.path.join(self.manuscript_dir, 'latex', file).split('.');
            output_path[-1] = 'tex'
            output_path = '.'.join(output_path)

            f = open(output_path, 'w', encoding='utf-8')
            f.write(output)
            f.close()

        return result


    def addTableOfContent(self, filename):
        result = False
        file = os.path.join(os.getcwd(), filename)

        if os.path.exists(file) == False:
            return result

        with open(file, encoding='utf-8') as toc_file:
            toc = json.load(toc_file)
            result = True

        self.toc.append(toc)

        return result


    def citeCount(self):
        result = False
        cite = {}
        entries = []
        if len(self.toc) < 1:
            return result

        for toc in self.toc:
            for entry in toc['content']:
                entries.append(entry['filename'])

        for script in self.manuscripts:
            needle = script.split('.')[0]
            cite[needle] = entries.count(needle)

        return cite


    def findOrphan(self):
        cite = self.citeCount();
        return list(filter(lambda x: cite[x] < 1, cite.keys()))


    def findOverCite(self):
        cite = self.citeCount();
        return list(filter(lambda x: cite[x] > 1, cite.keys()))

bartleby = Bartleby()
bartleby.addTableOfContent('toc.lump-of-meat.json');
bartleby.addTableOfContent('toc.neighbors.json');
bartleby.addTableOfContent('toc.weathers.json');
bartleby.addTableOfContent('toc.cell.json');
print(bartleby.findOrphan())
