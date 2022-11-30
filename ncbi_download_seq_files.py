from Bio import Entrez as en
from Bio import SeqIO

#email used to access NCBI-GEO
en.email = "bioinfo@bioinfo.com"

def ncbiFastaFilesDownloaderFunc (geneDic):
      """
      -Input: 
           1: dictionary with gene symbols and IDs
      -Functionality: Downloading sequencing fasta files from NCBI Nucleotide database for multiple 
                      sequence alignment.
      """
      for gene_symbol, gene_id in geneDic.items():
            ncbi_handle = en.efetch(db= 'nucleotide', id= gene_id, rettype='fasta') # download
            record = SeqIO.read(ncbi_handle, 'fasta') # read data
            print("Downloading %s with sequence length %d" % (record.name, len(record.seq)))
            output_name = gene_symbol+'.fasta'
            SeqIO.write(record, output_name, 'fasta') # write data into file


if __name__ == '__main__':

    # Gene symbol and GenBank ID
    dict={'E7F9E5':'XP_005169417.1',
          'F7AH40':'QLF98524.1',
          'Q8R0I0':'ACT66269.1',
          'F6WXR7':'XP_007500942.1',
          'G1KTF3':'XP_008105456.1',
          'Q56H28':'XP_044906242.1',
          'Q5RFN1':'XP_024096013.1'}
    ncbiFastaFilesDownloaderFunc(dict)

