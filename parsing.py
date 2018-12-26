
f=open(r'F:/refdata/ref.txt', "r")
rawdata=[]
count = 0
pod1 = False
blankcount =0
joindata = []
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
        start= ''
        end = ''
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

print("at Parsed.txt")
f=open('D:/parsed.txt','w')
for i in rawdata:
    for j in i:
        #print("writing")
        f.write(j)
        f.write("\t")
    f.write("\n")
f.close()
