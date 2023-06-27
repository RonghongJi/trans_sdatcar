with open('XDATCAR') as inputfile:
    data = inputfile.readlines()

    number = []
    element = []
    fixed_sentence = ["FORCE:    ...  ENERGY:  hhh"]*1000
    for i,item in enumerate(data):
        if "Direct configuration" in item:
            atom_num = int(data[i-1].split()[0])+int(data[i-1].split()[1])+int(data[i-1].split()[2])+int(data[i-1].split()[3])+int(data[i-1].split()[4])
            number.append(atom_num)
            combined_string = data[i-2].split()[0]*int(data[i-1].split()[0])+data[i-2].split()[1]*int(data[i-1].split()[1])+data[i-2].split()[2]*int(data[i-1].split()[2])+data[i-2].split()[3]*int(data[i-1].split()[3])+data[i-2].split()[4]*int(data[i-1].split()[4])
            element.append((combined_string))
    position_information = []  
    for i,item in enumerate(data):
        if "Direct configuration" in item:      
            position_information.append(data[i+1:i+1+1536])
    position = []
    for i,value in enumerate(position_information):
        position_item = []
        for j, value_1 in enumerate(value):
            position_item.append((float(value_1.split()[0]),float(value_1.split()[1]),float(value_1.split()[2])))
        position.append(position_item)    


with open('output.xyz', 'w') as f:
    for i in range(1000):
        f.write(f'{number[i]}\n')
        f.write(f'{fixed_sentence[i]}\n')
        for j in range(1536):
            content = "{} {}".format(element[i][j], position[i][j])
            f.write(content+"\n")
