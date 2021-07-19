from pyTabela import PyTabela

tab = PyTabela()
tab.addCampos(["numero","nome","sobrenome","idade"])
tab.addLinha([15,"Vitoria","Sousa",20])
tab.addLinha([10,"Pablo","Silva", 21])
tab.addLinha([2,"Valderlandia","Macedo",19])
tab.addLinha([20,"Artur","Hildegardo",20])
print(tab)


