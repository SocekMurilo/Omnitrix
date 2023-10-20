commands = { "AlienX": "DFVR436TFDG",  "4Bracos" : "DGSF546D4GS", "FogoSelvagem": "25GF27478SD", "Chama": "ASDF42452FV", "EcoEco": "OIHE432ERFV", "end": "SKEJ4345DFG", "jump": "SEOHOREI453" }
output = []

f = open("../main.omnitrix", "r")

file = f.readlines()

for line in file:
    if line[0] == '\n':
        continue
    command = line.split('(')[0]
    if command in commands.keys():
        output.append(commands[command])

    
    values = line.split('(')[1].split(')')[0]

    if output[-1] == "DFVR436TFDG":
        for i in values:
            output.append(i)
        output.append(commands["end"])
    if output[-1] == "DGSF546D4GS":
        values = values.split(',')
        for i in values:
            output.append(i)
        output.append(commands["end"])

f.close()


fileOutput = open("../output.omnitrix", "w")
fileOutput.write(str(output))
fileOutput.close()







# for line in file:
#     if line[0] == '\n':
#         continue
#     command = line.split('(')[0]
#     if command in commands.keys():
#         output.append(commands[command])

#     values = line.split('(')[1].split(')')[0]
    
#     string = []
#     flag = False
#     for l in values:
#         if l == "'" or l == '"':
#             flag = not flag
#             print(flag)
#         if flag:
#             string.append(l)
#     m = str(string).replace("'", '')
        
        

    
    
# print(output)

# for i, key in commands.items():
#     print("chave: " , key)
#     print("valor: ",  i)