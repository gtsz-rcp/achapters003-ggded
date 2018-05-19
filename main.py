import BartlebyMachine.main as bartleby
# from bartleby import Bartleby

bartleby = bartleby.Bartleby()
bartleby.addTableOfContent('toc.ggded.yaml')
bartleby.markdownToLatex()
