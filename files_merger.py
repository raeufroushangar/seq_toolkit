
import os

def fileMergerFunc (dirList, outputFile):
    """
    -Functionality: Merge multiple files into single file.
    """
    data = ""
    for i in dirList:
        if '.fasta' in i:
            with open(i) as f1:
                data = f1.readlines()
            with open(outputFile, 'a') as f2:
                f2.writelines(data)
                f2.write("\n")



if __name__ == '__main__':
    fileMergerFunc(os.listdir(),"merged_fasta_files.fasta")

