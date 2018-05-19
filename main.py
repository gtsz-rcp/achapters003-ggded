import BartlebyMachine.main as bartleby
# from bartleby import Bartleby

config = bartleby.Config('config.yaml')
bartleby = bartleby.Bartleby(config)
bartleby.addTableOfContent('toc.ggded.yaml')
bartleby.markdownToLatex()
bartleby.writeLatex()
