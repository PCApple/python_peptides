from Bio.Seq import Seq
import re
exec(open('dictionaries.py').read())


accession={}
for i in mrnas:
    for j in mrnas[i][1]:
        try:
            accession[j[1]]=[int(j[-2])-1,int(j[-1])]
        except:
            pass

def mut(position,transcript,mutation):
    print("inMUT")
    protein=Seq(sequence[transcript][accession[transcript][0]:accession[transcript][1]]).translate()
        
    print("in Seq")
    if position-9<0:
        
        return protein[0:position-1]+mutation+protein[position:position+8]
    else:
        
        return protein[position-9:position-1]+mutation+protein[position:position+8]


f=open(r'D:/output/MANIFEST.txt','r')
maf_patients=[]
maf_files=[]
for i in f:
    maf_patients.append(i.split('\n')[0])
    maf_files.append(i.split('\n')[0] + '.txt')


peptides={}
error = []
for i,j in zip(maf_patients,maf_files):
    x=0
    f=open(r"D:\output"+'\\'+j)
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

















