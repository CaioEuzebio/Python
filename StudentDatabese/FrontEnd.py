from Tkinter import *
import tkMessageBox


# System Front End
# import Student_Database_Backend


class Student:


    def __init__(self, root):
        self.root = root
        self.root.title = ("Banco de Dados De Alunos")
        self.root.geometry = ("1350x750+0+0")
        self.root.config(bg="black")

        aludoID = StringVar()
        primeironome = StringVar()
        sobrenome = StringVar()
        datanasc = StringVar()
        idade = StringVar()
        endereco = StringVar()
        telefone = StringVar()
        genero = StringVar()

        #===========================================Function==========================================================#

        def fnSair():
            fnSair = tkMessageBox.askyesno("Sistema De Gerenciamento De Alunos","Deseja Sair?")
            if fnSair > 0:
                root.destroy()
                return

        def limparDados():
            self.txtalunoID.delete(0,END)
            self.txtprimeironome.delete(0,END)
            self.txtsobrenome.delete(0,END)
            self.txtdatanasc.delete(0,END)
            self.txtidade.delete(0,END)
            self.txttelefone.delete(0,END)
            self.txtgenero.delete(0,END)
            self.txtendereco.delete(0,END)

        def addDados():
            if(len(aludoID.get())!=0):
                Student_Database_Backend.addDados(alunoID.get(), primeironome.get(), sobrenome.get(), datanascimento.get(),idade.get(), genero.get(), endereco.get(), telefone.get())
                alunos.delete(0,END)
                alunos.insert(END, alunoID.get(), primeironome.get(), sobrenome.get(), datanascimento.get(),idade.get(), genero.get(), endereco.get(), telefone.get())      

        #===========================================Frames==========================================================#

        MainFrame = Frame(self.root, bd=2, padx=54, pady=8, bg="black")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, height=150, bd=2, padx=54, pady=8, bg="ghost white", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=32, padx=2, height=1,font=('arial', 45, 'bold'), text="Base De Dados De alunos", bg="Ghost White")
        self.lblTitle.grid()

        
        DataFrame = Frame(MainFrame, bd=1, width=1, height=1, padx=20, pady=20, bg="black", relief=RIDGE)
        DataFrame.pack()

        ButtonFrame = Frame(MainFrame, bd=2, width=1, height=1, padx=18, pady=10, bg="black", relief=RIDGE)
        ButtonFrame.pack()

        DataFrameLEFT = LabelFrame(DataFrame, bd=2, width=1, height=1, padx=20, relief=RIDGE, bg="ghost white",
                                   font=('arial', 20, 'bold'), text='Dados do Aluno\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=2, width=1, height=1, padx=31, pady=3, relief=RIDGE, bg="ghost white",
                                    font=('arial', 15, 'bold'), text='Detalhes do aluno\n')
        DataFrameRIGHT.pack(side=RIGHT)

        #===========================================Labels and Entry===================================================#
        self.aludoID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='ID do Aluno:', bg="ghost white")
        self.aludoID.grid(row=0, column=0, sticky=W)
        self.txtalunoID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=aludoID, width=31)
        self.txtalunoID.grid(row=0, column=1)

        self.primeironome = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Primeiro Nome:', bg="ghost white")
        self.primeironome.grid(row=1, column=0, sticky=W)
        self.txtprimeironome = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=primeironome, width=31)
        self.txtprimeironome.grid(row=1, column=1)

        self.sobrenome = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Sobrenome:', bg="ghost white")
        self.sobrenome.grid(row=2, column=0, sticky=W)
        self.txtsobrenome = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=sobrenome, width=31)
        self.txtsobrenome.grid(row=2, column=1)

        self.datanasc = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Data Nasc.:', bg="ghost white")
        self.datanasc.grid(row=3, column=0, sticky=W)
        self.txtdatanasc = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=datanasc, width=31)
        self.txtdatanasc.grid(row=3, column=1)

        self.idade = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Idade:', bg="ghost white")
        self.idade.grid(row=4, column=0, sticky=W)
        self.txtidade = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=idade, width=31)
        self.txtidade.grid(row=4, column=1)

        self.endereco = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Idade:', bg="ghost white")
        self.endereco.grid(row=5, column=0, sticky=W)
        self.txtendereco = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=endereco, width=31)
        self.txtendereco.grid(row=5, column=1)

        self.telefone = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Telefone:', bg="ghost white")
        self.telefone.grid(row=6, column=0, sticky=W)
        self.txttelefone = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=telefone, width=31)
        self.txttelefone.grid(row=6, column=1)

        self.genero = Label(DataFrameLEFT, font=('arial', 20, 'bold'), padx=2, pady=2, text='Genero:', bg="ghost white")
        self.genero.grid(row=7, column=0, sticky=W)
        self.txtgenero = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=genero, width=31)
        self.txtgenero.grid(row=7, column=1)

        #===========================================List Box And Scroll Bar Widget=====================================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        listaalunos = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'))
        listaalunos.grid(row=0, column=0)
        scrollbar.config(command = listaalunos.yview)


        #===========================================Button Widget======================================================#
        self.btnAddnovo = Button(ButtonFrame, text="Adicionar Novo", font=('arial', 10, "bold"), command=addDados)
        self.btnAddnovo.grid(row=0, column=0, padx=8)
        
        self.btnAtualizar = Button(ButtonFrame, text="Atualizar", font=('arial', 10, "bold"))
        self.btnAtualizar.grid(row=0, column=1,padx=8)
        
        self.btnVisualizar = Button(ButtonFrame, text="Visualizar", font=('arial', 10, "bold"))
        self.btnVisualizar.grid(row=0, column=2,padx=8)
        
        self.btnDeletar = Button(ButtonFrame, text="Apagar", font=('arial', 10, "bold"))
        self.btnDeletar.grid(row=0, column=3,padx=8)
        
        self.btnLimpar = Button(ButtonFrame, text="Limpar", font=('arial', 10, "bold"), command=limparDados)
        self.btnLimpar.grid(row=0, column=4,padx=8)
        
        self.btnPesquisar = Button(ButtonFrame, text="Pesquisar", font=('arial', 10, "bold"))
        self.btnPesquisar.grid(row=0, column=5,padx=8)
        
        self.btnSair = Button(ButtonFrame, text="Sair", font=('arial', 10, "bold"), command=fnSair)
        self.btnSair.grid(row=0, column=6,padx=8)



if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()


