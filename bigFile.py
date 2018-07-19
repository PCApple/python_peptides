# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:52:39 2018

@author: pcase
"""
from Bio.Seq import Seq
import re
path = 'C:/Users/jcase/Downloads/ex3/'
mutName = 'data_mutations_extended.txt'
manifestName = 'MANIFEST.txt'
parsedName = 'parsed.txt'
def manifesting(path, mut, manifest):
    f =open(r'' + path + mut, 'r')
    x = f.readline()
    b =0
    data = []
    while x!= '':
        print(str(b))
        b=b+1
        splited = x.split('\t')
        if splited[16] not in data:
            print('appending')
            data.append(splited[16])
        x = f.readline()
    f2 = open(path + manifest, 'w')
    for i in data:
        f2.write(i)
        f2.write('\n')
    f2.close()
    return 0
def splitMutations(path, mut, manifest):
    f =open(r'' +path+mut,'r')
    data= {}
    x = f.readline()
    while x != '':
        split = x.split('\t')
        if split[16] not in data:
            print('adding')
            data[split[16]] = x
        else:
            #print('appending')
            data[split[16]] = data[split[16]] + x
        x = f.readline()
    for i in data:
        m = open(r'' + path + manifest, 'r')
        j = m.readline()
        name =""
        while j !='':
            #print('looking')
            if j.split('\n')[0] in i:
                print('found')
                name = j.split('\n')[0]
            j = m.readline()
        w = open(path + name + '.txt', 'w')
        print('print')
        w.write(data[name])
        w.write('\n')
        w.close()
        return 1
    #from onesres.com
def parsing(path, ref, parsed):
    f=open(r'' +path + ref, "r")
    rawdata=[]
    count = 0
    pod1 = False
    blankcount =0
    max_bytes=2048*2048
    x=f.readline()
    while blankcount <1000:
        if x == '':
            #rint("blanked")
            blankcount = blankcount +1
            pass
        if "LOCUS" in x[:5]:
            length=x.split()[2]
            max_bytes=1024*1024
            x=f.readline(max_bytes)
            #print("at DEFINITION")
            rawdefinition=x.strip().split('DEFINITION')[1]
            x=f.readline()
            while 'ACCESSION' not in x:
                rawdefinition+=' '+x.strip()
                x=f.readline(max_bytes)
            #print("at ACCESSION")
            accession=x.strip().split()[1]
            x=f.readline(max_bytes)
            X=False
            gene=''
            synonyms=''
            location=''
            entrez_id=''
            mol_type = ''
            while X==False:
                if gene=='':
                    if '/gene=' in x:
                        #print("at GENE")z
                        gene=x.strip().split('/gene=')[1].strip('"')
                        if 'VIM' in gene:
                            print("at VIM")
                            pod1 = True
                            
                if entrez_id=='':
                    if r'/db_xref="GeneID:' in x:
                        #print("at GENE_ID")
                        entrez_id=x.strip().split(":")[-1][:-1]
                if mol_type == '':
                    if "/mol_type=" in x:
                        y=x.split("/mol_type=")[1]
                if synonyms=='':
                    if "/gene_synonym=" in x:
                        print("at gene synonyms")
                        y=x.split("/gene_synonym=")[1]
                        while True:
                            if '"\n' in x:
                                synonyms+=y.strip()
                                break
                            synonyms+=y.strip()
                            x=f.readline()
                            y=x
                if location=='':
                    if "/map=" in x:
                        print("at MAP")
                        location=x.split("/map=")[1].strip()
                if "  CDS  " in x:
                    #print("at CDS")
                    if "join" in x:
                        #print("at join")
                        try:
                            start=x.split("join(")[1].split("..")[0]
                            end=x.split("join(")[1].split("..")[2].strip().split(")")[0]
                        except:
                            start = x.split("join(")[1].split("..")[0]
                            end = x.split("join(")[1].split("..")[1].strip().split(")")[0]
                    else:
                        start=x.split()[1].split("..")[0]
                        end=x.split()[1].split("..")[1].strip()
                if x=='ORIGIN      \n':
                    print("at Origin")
                    sequence=""
                    x=f.readline(max_bytes)
                    while x!="//\n":
                        for i in x.strip().split()[1:]:
                            sequence+=i
                        x=f.readline(max_bytes)
                    X=True
                    #print(rawdefinition)
                    try:
                        if '('+gene+')' in rawdefinition:
                            print("Gene:" + gene)
                            genename=rawdefinition.split('('+gene+')')[0].strip()
                            transcript=rawdefinition.split('('+gene+'), ')[1]
                        elif 'scaffold' in rawdefinition:
                            print("scaffold")
                            genename = rawdefinition.split('scaffold')[0].strip() + 'scaffold'
                            transcript = rawdefinition.split('scaffold')[1]
                    
                    except:
                        genename = 'NULL'
                        transcript = 'null'
                        print('Error at: ' + rawdefinition)
                        
                    
                    count =count +1
                    rawdata.append([gene,genename,entrez_id,location,synonyms,transcript,accession,length,start,end,sequence])
                x=f.readline(max_bytes)
        x=f.readline(max_bytes)
    
    print("at Parsed")
    f=open(path + parsed,'w')
    for i in rawdata:
        for j in i:
            #print("writing")
            f.write(j)
            f.write("\t")
        f.write("\n")
    f.close()
    return 1
#from omnesres.com
def dictionaries(path, parsed):
    f=open(r'' + path +parsed, "r")
    
    mrnas={}
    sequence={}
    rawdata=[]
    
    for i in f:
        rawdata.append([j.strip() for j in i.split("\t")[:-1]])
    
    
    
    for i in rawdata:
        x = 1
        #print("hello"0
        try:
            if i[0] not in mrnas:
                #print("hello False")
                mrnas[i[0]]=[i[1:5]]
                mrnas[i[0]].append([i[5:-1]])
                sequence[i[6]]=i[-1]
                x = x+1
            else:
                #print("hello")
                mrnas[i[0]][1].append(i[5:-1])
                sequence[i[6]]=i[-1]
        except:
            pass
    return 1
#from omnesres.com
def mut(position,transcript,mutation):
    print("inMUT")
    protein=Seq(sequence[transcript][accession[transcript][0]:accession[transcript][1]]).translate()
        
    print("in Seq")
    if position-9<0:
        
        return protein[0:position-1]+mutation+protein[position:position+8]
    else:
        
        return protein[position-9:position-1]+mutation+protein[position:position+8]
# from omnesres.com, needs to be run after dictionaries
def peptides(path, manifest):
    accession={}
    for i in mrnas:
        for j in mrnas[i][1]:
            try:
                accession[j[1]]=[int(j[-2])-1,int(j[-1])]
            except:
                pass
    f=open(r'' +path + manifest,'r')
    maf_patients=[]
    maf_files=[]
    for i in f:
        maf_patients.append(i.split('\n')[0])
        maf_files.append(i.split('\n')[0] + '.txt')
    
    
    peptides={}
    error = []
    for i,j in zip(maf_patients,maf_files):
        x=0
        f=open(r'' + path +'/'+j)
        f.readline()
        for k in f:
            x=x+1
            if '#' not in k:
                #print (data) 
                #print("ran")
                data=k.strip('\n').split('\t')
                if data[0] == '':
                    pass
                else:
                    if data[9]=='Missense_Mutation':
                        print('in missent')
                        try:
                            t1 = data[118].split('.')[0]
                            peptides[i]=peptides.get(i,[])+[str(mut(int(re.findall('[0-9]+',data[112])[0]),t1,re.split('[0-9]+',data[112])[-1]))]
                            print("running peptides")
                        except:
        #                    print("passed")
                            if t1 not in error:
                                error.append(data[118])
                            print('Error at: ' + data[118])
                            pass
            else:
                #print("norun")
                pass
    
    
    
    nonamer_peptides={}
    for i in peptides:
        for j in peptides[i]:
            if '*' in j:
                j=j[0:j.find('*')]
            for k,l in zip(range(0,len(j)-8),range(9,len(j)+1)):
                if len(j[k:l])==9:
                    print("running nonamer peptides")
                    nonamer_peptides[i]=nonamer_peptides.get(i,[])+[j[k:l]]
                
                
    tetra_peptides={}
    
    for i in nonamer_peptides:
        for j in nonamer_peptides[i]:
            
            for k,l in zip(range(0,len(j)-3),range(4,len(j)+1)):
                if len(j[k:l])==4:
                    print("running tetra peptides")
                    tetra_peptides[i]=tetra_peptides.get(i,[])+[j[k:l]]
    
    
    
    nonamer_counts={}
    for i in nonamer_peptides:
        for j in nonamer_peptides[i]:
            print("running nonamer counts")
            nonamer_counts[j]=nonamer_counts.get(j,0)+1
    
    
    
    tetra_counts={}
    for i in tetra_peptides:
        for j in tetra_peptides[i]:
            print("running tetra counts")
            tetra_counts[j]=tetra_counts.get(j,0)+1