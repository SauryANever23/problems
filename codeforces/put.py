import os 

directory = "."
files=os.listdir(directory)
for file in files:
    if file == "src" or "." in file:
        pass
    else:
        os.system(f"mv {file} src")
