
# Dependences:
import os

"""
Discription:
------------
This function reads the '.genome' file and count number of sequenced chromosomes.

Inputes:
--------
1: Path of parent directory where all "sequenced" subdirectories are located.
"""

def chromosomeCount ():

    print("""\n--set parant directory where sequence directories are located--\n""")

    while True:
        usr_dir_input = input("enter path of working directory: ") # ask user ot enter path
        if usr_dir_input == "0":
            print('good bye!\n')
            break
        else:
            try:
                working_dir = os.chdir(usr_dir_input) # set path
                print("path is set!\n")
                """loop over each sub directory"""
                for i in os.listdir(working_dir):
                    try:
                        # directory_list = os.listdir(i) # list files in each directory
                        """loop over files in each directory"""
                        for j in os.listdir(i):
                            if ".genome" in j: # check file name has 'genome' in it
                                file_path = (i+"/"+j) # genome file path
                                genome_file = open(file_path, "r") # read genome file
                                genome_seq = genome_file.readlines() 
                                
                                count = 0 # set a counter
                                for line in genome_seq:
                                    if ">" in line:
                                        count +=1 # add 1 each time '>' is found
                                print(f"{file_path}, has {count} chromosomes.")
                    except:
                        continue
            except:
                print("path not found. Please retry.\n") # print if path is not found
                continue
            break


if __name__ == '__main__':
    chromosomeCount()