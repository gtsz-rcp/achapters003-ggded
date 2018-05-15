import BartelbyMachine.main as bartelby
# from bartelby import Bartelby

bartleby1 = bartelby.Bartelby()
bartleby1.addTableOfContent('toc.lump-of-meat.json');
bartleby1.markdowntolatex()

bartleby2 = bartelby.Bartelby()
bartleby2.addTableOfContent('toc.neighbors.json');
bartleby2.markdowntolatex()

bartleby3 = bartelby.Bartelby()
bartleby3.addTableOfContent('toc.weathers.json');
bartleby3.markdowntolatex()

bartleby4 = bartelby.Bartelby()
bartleby4.addTableOfContent('toc.cell.json');
bartleby4.markdowntolatex()
