HEADER = "ID,k23,kcia,kvac,kmit,kcyt,ko2,kmp\n"
lines = []
with open("validTargetCRMS.txt") as f:
    lines = f.readlines()
csv_lines = []
csv_lines.append(HEADER)
counter = 1
for line in lines:
    if line.strip():
        line = line.strip()
        line = line.replace("{","")
        line = line.replace("},","")
        row = [str(counter)]
        parts = line.split(",")
        for part in parts:
            part = part.strip()
            part = part[0:len(part)-1]
            row.append(part)
        counter += 1
        csv_lines.append(",".join(row)+"\n")

csvfile = open("../SteadyStateAnalysis/data/crmdata.csv",'w+')
csvfile.writelines(csv_lines)
csvfile.close()