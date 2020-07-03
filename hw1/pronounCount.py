f=open("Mar07_GroupB.txt.xml","r")
pronounCounts={}
currentP="placeholder"
maybeP="wow"
count=0
rpFlag=False
while True:
    line=f.readline()
    if not line:
        break
    if "<token id=\"1\">" in line:
        line=f.readline()
        maybeP=line.replace("<word>","").replace("</word>","").replace("\n","").replace(" ","")
    elif "<word>-RRB-</word>"in line:
        rpFlag=True
    elif "<word>:</word>"in line and rpFlag:
        if currentP in pronounCounts:
            pronounCounts[currentP]+=count
        else:
            pronounCounts[currentP]=count
        count=0
        currentP=maybeP
        rpFlag=False
    elif "<POS>PRP$</POS>" in line or "<POS>PRP</POS>" in line:
        count+=1
    elif "</sentence>"in line:
        rpFlag=False
f.close()
d=0
for x in pronounCounts:
    print(x,":",pronounCounts[x])
    d+=pronounCounts[x]
print(d)
