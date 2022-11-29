from Bio import Entrez as en
from Bio import SeqIO



#email used to access NCBI-GEO
en.email = "bioinfo@gmail.com"

"""
   Downloading sequences fasta files from NCBI-Nucleotide for multiple sequence alignment.
"""

def ncbi_download (arg):
      for gene_symbol, gene_id in arg.items():
            ncbi_handle = en.efetch(db= 'nucleotide', id= gene_id, rettype='fasta')
            record = SeqIO.read(ncbi_handle, 'fasta')
            print("Downloading %s with sequence length %d" % (record.name, len(record.seq)))
            output_name = gene_symbol+'.fasta'
            SeqIO.write(record, output_name, 'fasta')


# Gene symbol and GenBank ID
dict={'G3QWX4':'SRLZ01002358.1',
      'E7F9E5':'CU652893.6',
      'F7AH40':'QNVO02003165.1',
      'Q5EGZ1':'CH474014.2',
      'Q8R0I0':'AL671706.8',
      'F6WXR7':'AAFR03034356.1',
      'G1KTF3':'AAWZ02007819.1',
      'Q56H28':'JAFEKA010000012.1',
      'Q5RFN1':'NDHI03003400.1'}

if __name__ == '__main__':
    ncbi_download(dict)
