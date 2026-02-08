filenames=["1.doc","2.doc","3.doc","4.doc","5.doc"]
filenames=[filename.replace('.','-') + '.txt' for filename in filenames]
print(filenames)