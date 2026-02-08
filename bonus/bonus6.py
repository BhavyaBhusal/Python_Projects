contents=["All Niggers are the same","All Niggers are reportedly black","All Niggers are told to be YNs"]
filename=["doc.txt","report.txt","presentation.txt"]
for content,filename in zip(contents,filename):
    file= open(f"../files/{filename}","w")
    file.write(content)

