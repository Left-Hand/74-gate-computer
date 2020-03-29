plist = ["NON", "ACP", "AMR", "STL", "STR", "LDM", "BLLD", "BHLD",
         "AILD", "MLD", "STC", "CLC", "REC", "NF", "CAI", "ACLD",
         "PCLLD", "PCMLD", "PCHLD", "FBK", "RD", "WT", "RET", "GED",
         "JMP", "HLT", "JC", "JNC", "JZ", "JNZ", "JV", "JNV",
         "T0LLD", "T0HLD", "T1LLD", "T1HLD", "CTC", "CTI", "INT3", "INT1",
         "IO0", "IO1", "CLD", "DLD", "IOLD", "", "", "",
         "", "", "", "", "", "", "", "",
         "SAM", "IVS", "WVGA", "YP", "LXB", "LX", "LYB", "LY"]
olist = ["BUSO", "UO", "DO", "AOO", "ACO", "PCLO", "PCMO", "PCHO",
         "RDTO", "INTO", "CRO", "DRO","IO0O", "IO1O"]
outlines = []
for i in range(1000):
    outlines.append("00")
m = 0
i = 0
'''----------------------------------------'''
fpath = "D:\GUN\programs\\Hello_World.txt"
'''----------------------------------------'''
class config():
    def __init__(self):
        self.forward = 1
        self.size = 0
insconfig = config()
def findins(ins):
    global plist
    global m
    try:
        m = 0
        return(plist.index(ins))
    except ValueError:
        m = 1
        return(olist.index(ins))
    except ValueError:
        print(str(i))
def delline(line):
    global i
    global outlines
    global insconfig
    outline = ""
    ins = hex(findins(line[0])).replace("0x", "")
    if len(line) > 0:
        if len(line) > 1:
            if line[1][0] != "#":
                outlines[i] = gethex(ins, m, 1)
                outline +=(outlines[i] + ",");  insconfig.size += 1;    i += 1
                outlines[i] = (reformatnum(line[1]))
                outline +=outlines[i];  insconfig.size += 1;    i += 1
        else:
            outlines[i] = gethex(ins, m, 0)
            outline +=outlines[i];  insconfig.size += 1;    i += 1
    if len(line) > 1 and line[1][0] != "#":
        print(hex(i-2) + "." + line[0] +" " + line[1] +"  ->  " + outline)
    elif len(line) == 1:
        print(hex(i-1) + "." + line[0] + "  ->  " + outline)
def gethex(ins, m, n):
    if len(ins) == 1:
        ins = "0"+ins
    ins = hex(int(ins[0])+8*n+4*m).replace("0x", "")+ins[1:2]
    return ins
with open(fpath, "r",encoding='utf-8') as file:
    lines = file.readlines()
    lineindex = 0
    for lineindex in range(len(lines)):
        lines[lineindex] = lines[lineindex].split()
def reformatnum(num):
    if num[0:2] == "0x" or num[0:2] =="0X":
        num = num.replace("0x", "")
        num = num.replace("0X", "")
    else:
        num = hex(int(num)).replace("0x", "")
    if len(num) == 1:
        num = "0" + num
    return num
def output():
    lastline = ""
    i = 0
    global outlines
    for i in range(insconfig.size + 1):
        if i % 16 == 0:
            lastline += "\n"
        lastline += (outlines[i] + ",") 
    lastline = lastline[0:len(lastline)-1]
    print(lastline)
#    print(lastline.replace(",", " "))
    print("--------")
    print(lastline.replace("00", "."))
    print("--------")
    print((lastline.replace("\n", "")))
    print("成功编译！程序共计使用" + str(insconfig.size) + "字节")
def printALL():
    for i in range(len(olist)):
        print("|" + bool(i % 8 == 0)*"__"+(8-len(bin(i)))*"0" + bin(i).replace("0b","")+bool(i % 8 == 0)*"__"+ "|" + olist[i] +"|"+"|")
def main():
    global i
    for line in lines:
        if len(line) != 0:
            if line[0][0] == "!":
                if line[0] == "!forward:":
                    insconfig.forward = line[1]
            elif line[0][0] == "*":
                addres = (int(line[2], 16))
                if addres < i:
                    print("代码与常量重合")
                else:
                    outlines[addres] = reformatnum(line[1])
                    if insconfig.size < addres:
                        insconfig.size = addres
            elif line[0][0] == "&":
                addres = (int(line[1], 16))
                if addres < i:
                    print("与前面的代码重合")
                else:
                    if insconfig.size < addres:
                        insconfig.size = addres
                    i = addres
            elif len(line) != 0 and line[0][0] != "#":
                delline(line)
    output()
main()
