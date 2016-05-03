#!/usr/bin/python

    def id_map(file_id, frmt):        
        with open('d_id_map.txt', 'w') as file2:
            with open(file_id, 'r') as file_id_name:
                for line in file_id_name:
                    line=line.split()
                    with open(frmt, 'r') as fr:
                        for f in fr:
                            f=f.split()
                            if len(line)>2:
                                if line[1]==f[0]:
                                    result= line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+f[1]+'\t'+f[2]+'\t'+f[3]
                                    if result>0:
                                        with open('d_id_map.txt', 'a') as file2:
                                            file2.write(result+'\n')

    def cc_mapping(mu, frmt_file):
        """continuation of codon calculation (cc) with formated gff file, the file product is the protein id with mutated codons"""
        with open('mutation.txt', 'w') as file4:
            with open(frmt_file,'r') as f_file:
                for line in f_file:
                    line=line.split()
                    with open(mu, 'r') as m:
                        for m in m:
                            m=m.split()
                            if line[2]==m[0]:
                                q= int(float(line[4]))-int(float(m[1]))
                                q1=int(q)/3
                                q2=m[0]+'\t'+str(q1)
                                with open('mutation.txt', 'a') as file4:
                                    file4.write(q2+'\n')
                                    
    
    def code(): 

    """ codon calculations where ref and mutant base unknown """

    try:
        cc_mapping('mutation.txt', 'd_id_map.txt')
    except IOError:
            pass
    return "codons are available to map on functional entities"
    
    
