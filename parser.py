import sys
def originToStr(origin):
    if origin == "App": return "Clause Deletion"
    elif origin == "EmS": return "Empty Sort"
    elif origin == "SoR": return "Sort Resolution"
    elif origin == "EqR": return "Equality Resolution"
    elif origin == "EqF": return "Equality Factoring"
    elif origin == "MPm": return "Merging Paramodulation"
    elif origin == "SpR": return "Superposition Right"
    elif origin == "SPm": return "Paramodulation"
    elif origin == "OPm": return "Ordered ParamodulatioN"
    elif origin == "SpL": return "Superposition Left"
    elif origin == "Res": return "General Resolution"
    elif origin == "SHy": return "Simple Hyper"
    elif origin == "OHy": return "Ordered Hyper"
    elif origin == "URR": return "UR Resolution"
    elif origin == "Fac": return "General Factoring"
    elif origin == "Spt": return "Splitting"
    elif origin == "Inp": return "Input"
    elif origin == "Rew": return "Rewriting"
    elif origin == "CRw": return "Contextual Rewriting"
    elif origin == "Con": return "Condensing"
    elif origin == "AED": return "Assignment Equation Deletion"
    elif origin == "Obv": return "Obvious Reductions"
    elif origin == "SSi": return "Sort Simplification"
    elif origin == "MRR": return "Matching Replacement ResolutioN"
    elif origin == "UnC": return "Unit Conflict"
    elif origin == "Def": return "DefApplication"
    elif origin == "Ter": return "Terminator"
    else: return "Unknown"

class Clause:
    number = 0
    origin = ""
    consLits = []
    anteLits = []
    succLits = []
    parents = []

    def simplePrint(self):
        if len(self.consLits) == 0 and len(self.anteLits) == 0 and len(self.succLits) == 0:
            outputfile.write("%d\t END\n" % self.number)
        elif (len(self.consLits) != 0 or len(self.anteLits) != 0) and len(self.succLits) == 0:
            string = ""
            for cons in self.consLits:
                string += "~%s OR " % cons
            for ante in self.anteLits:
                string += "~%s OR " % ante
            string = string[0:-4]
            outputfile.write("%d\t %s\n" % (self.number, string))
        elif len(self.consLits) == 0 and len(self.anteLits) == 0 and len(self.succLits) != 0:
            for succ in self.succLits:
                outputfile.write("%d\t %s\n" % (self.number, succ))
        else:
            string = ""
            for cons in self.consLits:
                string += "%s AND " % cons
            for ante in self.anteLits:
                string += "%s AND " % ante
            string = string[0:-5] + " -> "
            
            for succ in self.succLits:
                string += "%s OR " % succ
            string = string[0:-5]
            outputfile.write("%d\t %s\n" % (self.number, string))

    def printClause(self):
        outputfile.write("Method: %s\n" % originToStr(self.origin))
        for clause in self.parents:
            clause.simplePrint()
        outputfile.write("##\n")
        self.simplePrint()
        outputfile.write("---------------------------------------\n")    

inputfile = sys.stdin
outputfile = sys.stdout

if len(sys.argv) > 1:
    inputfile = open(sys.argv[1]) 

if len(sys.argv) > 2:
    outputfile = open(sys.argv[2], "w") 

lines = inputfile.readlines()
proofstart = 0
proofend = 0
#Fix this workaround to something better
for num, line in enumerate(lines):
    if line.startswith("Here is a proof with depth"):
        proofstart = num
    if line.startswith("Formulae used in the proof"):
        proofend = num

if proofend > proofstart:
    lines = lines[proofstart+1:proofend]
else:
    print("Missing proof")
    sys.exit(0)


s = "".join(lines).strip()

cls = {int(c.split('[')[0]) : '[' + c.split('[')[1][0:-1] for c in s.split('\n')}

clauses = {}

for number in sorted(list(cls.keys())):
    c = Clause()
    c.number = number
    text = cls[number] 
    c.origin = text.split(':')[1].split(']')[0]
    if c.origin != "Inp":
        parentsStr = text.split(':')[2].split(']')[0]
        c.parents = list(set([clauses[int(p.split('.')[0])] for p in parentsStr.split(',')]))
    
    literals = text.split(']')[1]
    consLitsStr = literals.split('||')[0].strip()
    anteLitsStr = literals.split('||')[1].split('->')[0].strip()
    succLitsStr = literals.split('->')[1].strip()
    c.consLits = consLitsStr.split(' ') if consLitsStr != '' else []
    c.anteLits = anteLitsStr.split(' ') if anteLitsStr != '' else []
    c.succLits = succLitsStr.split(' ') if succLitsStr != '' else []

    clauses[number] = c

for n in sorted(list(clauses.keys())):
    clauses[n].printClause()
