import BartlebyMachine.main as bartleby
import BartlebyMachine.book as book

bartleby = bartleby.Bartleby()
bartleby.addTableOfContent('toc.ggded.yaml')
bartleby.markdownToLatex()
bartleby.writeLatex()
