import PyPDF2

no_of_files=int(input("Enter the number of files to be merged: "))

files=[]

#genrating a list of files that will be merged
while (no_of_files>0):
    file=str(input("Enter file name: "))
    files.append(file)
    no_of_files-=1

#creating an instance of pdf merger
merger=PyPDF2.PdfMerger()

#Merging the files one by one
for pdf in files:
    pdfile= open(pdf,"rb")
    pdfReader= PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)

pdfile.close()

#resulting the merged files
result=input("Enter the name of merged file: ")
merger.write(result)