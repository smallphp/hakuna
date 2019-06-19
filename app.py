from hakuna import Hakuna
hakuna = Hakuna()
hakuna.addRoute('(<controller>)-(<action>).html',{'controller':'index'},{})
application = hakuna.wsgi()
