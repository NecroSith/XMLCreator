# -*- coding: utf-8 -*-
import xml.etree.cElementTree as et
import tkinter as tk
from tkinter import Tk, ttk, Frame, BOTH
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.ttk import *
from pathlib import Path

class Converter(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        frameStyle = Style()
        frameStyle.configure('My.TFrame', background='white')
        frame = Frame(master, style='My.TFrame')
        frame.pack()
        self.initUI(master)

    def initUI(self, master):
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black")
        style.configure("LabelError.TLabel", foreground="red")
        style.configure("SuccessLabel.TLabel", foreground="green")
        self.pack(fill=BOTH, expand=1)
        self.style = "BW.TLabel"

        self.entries = []

        generalLabel = ttk.Label(text="Укажите:", style="BW.TLabel")
        generalLabel.place(x=10, y=10)

        name = ttk.Label(text="наименование органа государственной власти \n или орган местного самоуправления", style="BW.TLabel")
        name.place(x=20, y=30, width=270, height=40)

        self.nameEntry = ttk.Entry()
        self.nameEntry.place(x=300, y=35, width=190)
        # here is the application variable
        self.nameEntryContent = tk.StringVar()
        # set it to some value
        self.nameEntryContent.set("")
        # tell the entry widget to watch this variable
        self.nameEntry["textvariable"] = self.nameEntryContent
        self.entries.append(self.nameEntry)

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        # self.nameEntry.bind('<Key-Return>',
                             # self.print_contents)

        governanceCode = ttk.Label(text="код органа государственной власти или \nорган местного самоуправления", style="BW.TLabel")
        governanceCode.place(x=20, y=75, width=270, height=40)

        self.governanceCodeEntry = ttk.Entry()
        self.governanceCodeEntry.place(x=300, y=80, width=190)
        self.governanceCodeEntryContent = tk.StringVar()
        self.governanceCodeEntryContent.set("")
        self.governanceCodeEntry["textvariable"] = self.governanceCodeEntryContent
        self.entries.append(self.governanceCodeEntry)

        email = ttk.Label(text="адрес электронной почты", style="BW.TLabel")
        email.place(x=20, y=120, width=270, height=20)

        self.emailEntry = ttk.Entry()
        self.emailEntry.place(x=300, y=120, width=190)
        self.emailEntryContent = tk.StringVar()
        self.emailEntryContent.set("")
        self.emailEntry["textvariable"] = self.emailEntryContent
        self.entries.append(self.emailEntry)

        familyName = ttk.Label(text="фамилию", style="BW.TLabel")
        familyName.place(x=20, y=145, width=270, height=20)

        self.familyNameEntry = ttk.Entry()
        self.familyNameEntry.place(x=300, y=145, width=190)
        self.familyNameEntryContent = tk.StringVar()
        self.familyNameEntryContent.set("")
        self.familyNameEntry["textvariable"] = self.familyNameEntryContent
        self.entries.append(self.familyNameEntry)

        firstName = ttk.Label(text="имя", style="BW.TLabel")
        firstName.place(x=20, y=170, width=270, height=20)

        self.firstNameEntry = ttk.Entry()
        self.firstNameEntry.place(x=300, y=170, width=190)
        self.firstNameEntryContent = tk.StringVar()
        self.firstNameEntryContent.set("")
        self.firstNameEntry["textvariable"] = self.firstNameEntryContent
        self.entries.append(self.firstNameEntry)

        patronymic = ttk.Label(text="отчество", style="BW.TLabel")
        patronymic.place(x=20, y=195, width=270, height=20)

        self.patronymicEntry = ttk.Entry()
        self.patronymicEntry.place(x=300, y=195, width=190)
        self.patronymicEntryContent = tk.StringVar()
        self.patronymicEntryContent.set("")
        self.patronymicEntry["textvariable"] = self.patronymicEntryContent
        self.entries.append(self.patronymicEntry)

        codeDocument = ttk.Label(text="код документа", style="BW.TLabel")
        codeDocument.place(x=20, y=220, width=270, height=20)

        self.codeDocumentEntry = ttk.Entry()
        self.codeDocumentEntry.place(x=300, y=220, width=190)
        self.codeDocumentEntryContent = tk.StringVar()
        self.codeDocumentEntryContent.set("")
        self.codeDocumentEntry["textvariable"] = self.codeDocumentEntryContent
        self.entries.append(self.codeDocumentEntry)

        series = ttk.Label(text="серию документа", style="BW.TLabel")
        series.place(x=20, y=245, width=270, height=20)

        self.seriesEntry = ttk.Entry()
        self.seriesEntry.place(x=300, y=245, width=190)
        self.seriesEntryContent = tk.StringVar()
        self.seriesEntryContent.set("")
        self.seriesEntry["textvariable"] = self.seriesEntryContent
        self.entries.append(self.seriesEntry)

        number = ttk.Label(text="номер документа", style="BW.TLabel")
        number.place(x=20, y=270, width=270, height=20)

        self.numberEntry = ttk.Entry()
        self.numberEntry.place(x=300, y=270, width=190)
        self.numberEntryContent = tk.StringVar()
        self.numberEntryContent.set("")
        self.numberEntry["textvariable"] = self.numberEntryContent
        self.entries.append(self.numberEntry)

        date = ttk.Label(text="дату выдачи документа", style="BW.TLabel")
        date.place(x=20, y=295, width=270, height=20)

        self.dateEntry = ttk.Entry()
        self.dateEntry.place(x=300, y=295, width=190)
        self.dateEntryContent = tk.StringVar()
        self.dateEntryContent.set("")
        self.dateEntry["textvariable"] = self.dateEntryContent
        self.entries.append(self.dateEntry)

        issueOrgan = ttk.Label(text="организацию выдавшую документ", style="BW.TLabel")
        issueOrgan.place(x=20, y=320, width=270, height=20)

        self.issueOrganEntry = ttk.Entry()
        self.issueOrganEntry.place(x=300, y=320, width=190)
        self.issueOrganEntryContent = tk.StringVar()
        self.issueOrganEntryContent.set("")
        self.issueOrganEntry["textvariable"] = self.issueOrganEntryContent
        self.entries.append(self.issueOrganEntry)

        snils = ttk.Label(text="СНИЛС", style="BW.TLabel")
        snils.place(x=20, y=345, width=270, height=20)

        self.snilsEntry = ttk.Entry()
        self.snilsEntry.place(x=300, y=345, width=190)
        self.snilsEntryContent = tk.StringVar()
        self.snilsEntryContent.set("")
        self.snilsEntry["textvariable"] = self.snilsEntryContent
        self.entries.append(self.snilsEntry)

        agentKind = ttk.Label(text="вид представительства", style="BW.TLabel")
        agentKind.place(x=20, y=370, width=270, height=20)

        self.agentKindEntry = ttk.Entry()
        self.agentKindEntry.place(x=300, y=370, width=190)
        self.agentKindEntryContent = tk.StringVar()
        self.agentKindEntryContent.set("")
        self.agentKindEntry["textvariable"] = self.agentKindEntryContent
        self.entries.append(self.agentKindEntry)

        appointment = ttk.Label(text="должность", style="BW.TLabel")
        appointment.place(x=20, y=395, width=270, height=20)

        self.appointmentEntry = ttk.Entry()
        self.appointmentEntry.place(x=300, y=395, width=190)
        self.appointmentEntryContent = tk.StringVar()
        self.appointmentEntryContent.set("")
        self.appointmentEntry["textvariable"] = self.appointmentEntryContent
        self.entries.append(self.appointmentEntry)

        self.var = BooleanVar()
        self.remember = Checkbutton(master, text='Запомнить данные', variable=self.var, onvalue=1, offvalue=0)
        self.remember.place(x=300, y=420)

        self.fileNameLabel = ttk.Label(text="Путь отсутствует", style="BW.TLabel")
        self.fileNameLabel.place(x=20, y=450, width=270, height=20)
        self.filePath = ''

        self.statusLabel = ttk.Label(text="Файл не выбран", style="LabelError.TLabel")
        self.statusLabel.place(x=140, y=425, width=150, height=20)

        self.xmlChoose = tk.Button(self, text="Выбрать файл", command=self.chooseTXT)
        self.xmlChoose.place(x=20, y=420)

        self.launchButton = tk.Button(self, text="Сгенерировать XML", command=self.createXML)
        self.launchButton.place(x=300, y=450)

        self.quitButton = tk.Button(self, text="Выход", command=master.destroy)
        self.quitButton.place(x=430, y=450)

        self.checkConfig()

    def checkConfig(self):
        configFile = Path('config.txt')
        configs = []
        print('checking...')
        try:
            with open(str(configFile), 'r') as file:
                for index in file:
                    
                    #self.appointmentEntryContent.set(index.strip())
                    #self.entries[1].config(text=index.strip())
                    configs.append(index.strip())

            # I know this code sucks - I am ashamed of myself 
            print('config array has been created')
            print(configs[0])
            self.nameEntryContent.set(str(configs[0]))
            self.governanceCodeEntryContent.set(str(configs[1]))
            self.emailEntryContent.set(str(configs[2]))
            self.familyNameEntryContent.set(str(configs[3]))
            self.firstNameEntryContent.set(str(configs[4]))
            self.patronymicEntryContent.set(str(configs[5]))
            self.codeDocumentEntryContent.set(str(configs[6]))
            self.seriesEntryContent.set(str(configs[7]))
            self.numberEntryContent.set(str(configs[8]))
            self.dateEntryContent.set(str(configs[9]))
            self.issueOrganEntryContent.set(str(configs[10]))
            self.snilsEntryContent.set(str(configs[11]))
            self.agentKindEntryContent.set(str(configs[12]))
            self.appointmentEntryContent.set(str(configs[13]))
                    
        except IOError:
            print('IOError')
        #print(configs)
        #print(self.entries)
        #for i in range(13):
            #self.entries[i].config(text=configs[i])
            
    def createXML(self):
        if self.var.get() is True:
            configFile = open('config.txt', 'w')
            
            configFile.write(self.nameEntry.get() + '\n')
            configFile.write(self.governanceCodeEntry.get() + '\n')
            configFile.write(self.emailEntry.get() + '\n')
            configFile.write(self.familyNameEntry.get() + '\n')
            configFile.write(self.firstNameEntry.get() + '\n')
            configFile.write(self.patronymicEntry.get() + '\n')
            configFile.write(self.codeDocumentEntry.get() + '\n')
            configFile.write(self.seriesEntry.get() + '\n')
            configFile.write(self.numberEntry.get() + '\n')
            configFile.write(self.dateEntry.get() + '\n')
            configFile.write(self.issueOrganEntry.get() + '\n')
            configFile.write(self.snilsEntry.get() + '\n')
            configFile.write(self.agentKindEntry.get() + '\n')
            configFile.write(self.appointmentEntry.get() + '\n')
            
            configFile.close()

        try:
            with open(self.filePath, 'r') as read_file:
                #fixLine = read_file.read().replace(':', '-')
                print('Creating xml...')
                for i in read_file:
                    line = i.rstrip()
                    requestGKN = et.Element("RequestGKN",NameSoftware="ГИС Земля", GUID="583a010b-615b-4f95-a6f2-3fddefd7b8fa", VersionSoftware="01" )
                    title = et.SubElement(requestGKN, "Title")
                    
                    et.SubElement(title, "RecipientName").text = "Архангельская область"
                    et.SubElement(title, "RecipientType").text = "Орган кадастрового учёта"

                    declarant = et.SubElement(requestGKN, "Declarant", declarantKind="Укажите вид заявителя (категория подателя запроса)")

                    governance = et.SubElement(declarant, "Governance")

                    et.SubElement(governance, "Name").text = self.nameEntry.get()
                    et.SubElement(governance, "GovernanceCode").text = self.governanceCodeEntry.get()
                    et.SubElement(governance, "Email").text = self.emailEntry.get()

                    agent = et.SubElement(governance, "Agent")

                    et.SubElement(agent, "FamilyName").text = self.familyNameEntry.get()
                    et.SubElement(agent, "FirstName").text = self.firstNameEntry.get()
                    et.SubElement(agent, "Patronymic").text = self.patronymicEntry.get()

                    document = et.SubElement(agent, "Document")

                    et.SubElement(document, "CodeDocument").text = self.codeDocumentEntry.get()
                    et.SubElement(document, "Series").text = self.seriesEntry.get()
                    et.SubElement(document, "Number").text = self.numberEntry.get()
                    et.SubElement(document, "Date").text = self.dateEntry.get()
                    et.SubElement(document, "IssueOrgan").text = self.issueOrganEntry.get()

                    et.SubElement(agent, "SNILS").text = self.snilsEntry.get()
                    et.SubElement(agent, "agentKind").text = self.agentKindEntry.get()
                    et.SubElement(agent, "Appointment").text = self.appointmentEntry.get()

                    et.SubElement(declarant, "IncomigDate").text = "Укажите дату выдачи"

                    requiredData = et.SubElement(requestGKN, "RequiredData")

                    kpt = et.SubElement(requiredData, "KPT")

                    et.SubElement(kpt, "CadastralNumber").text = i

                    delivery = et.SubElement(requestGKN, "Delivery")

                    et.SubElement(delivery, "WebService").text = "true"

                    appliedDocuments = et.SubElement(requestGKN, "AppliedDocuments")

                    appliedDocument = et.SubElement(appliedDocuments, "AppliedDocument")

                    et.SubElement(appliedDocument, "CodeDocument").text = "558101010000"
                    et.SubElement(appliedDocument, "Name").text = "Запрос о предоставлении сведений, внесенных в государственный кадастр недвижимости"
                    et.SubElement(appliedDocument, "Number").text = "1"
                    et.SubElement(appliedDocument, "Date").text = "Укажите дату запроса"
                    et.SubElement(appliedDocument, "IssueOrgan").text = "Укажите автора"

                    concept = et.SubElement(requestGKN, "Concept")

                    et.SubElement(concept, "ProcessingPeronalData")

                    split = line.split(':')
                    split2 = split[2]
                    
                    tree = et.ElementTree(requestGKN)
                    #print(split)
                    tree.write('./xml/%s.xml' % split2)
            self.statusLabel.config(text="XML сгенерирован", style="SuccessLabel.TLabel")
        except:
             self.statusLabel.config(text="Файл не выбран", style="LabelError.TLabel")
             

    def chooseTXT(self):
        print("test")
        xmlChoose = askopenfilename(initialdir = "/",title = "Выберите файл для загрузки",filetypes = (("текстовый документ","*.txt"),("all files","*.*")))
        self.fileNameLabel.config(text=xmlChoose)
        self.filePath = xmlChoose
        self.statusLabel.config(text="Файл выбран", style="SuccessLabel.TLabel")
        print(self.filePath)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Converter(master=root)
    app.master.title("Сборщик XML alpha v0.2")
    app.master.minsize(500, 500)
    app.master.maxsize(500, 500)
    app.mainloop()

if __name__ == '__main__':
    main()
    
    
    
    
    
    
