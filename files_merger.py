
import os

def fileMergerFunc (dirList, outputFile):
    """
    -Input: 
         1: list of fasta files names
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
    fileMergerFunc(os.listdir(),"muscle_input.fasta")
