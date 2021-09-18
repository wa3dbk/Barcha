import re 

mapp=dict()
with open('AB263') as f:
    for line in f:
        line=line.strip()

        if re.match('^[A-Z][A-Z] ', line):
            ID=line[:2]
            mapp[ID]=line[3:]
        else:
            mapp[ID]+=line

print(mapp)
