name = input('input your XDARCAR:')
output_name = input("input your outfile name:")

with open(name, 'r') as f:
    content = f.readlines()
    
    
N_atom = 0
N_period = 0
atom_type = []
atom_num = []
for index, line in enumerate(content):
    if 'Direct configuration=' in line:
        N_period = index + 1
        first_configuration = 0
        for item in content[index - 1].split():
            N_atom += int(item)
        atom_type = content[index - 2].split()
        atom_num = content[index - 1].split()
        break
        
with open(output_name, 'w') as f:
    for i in range(int(len(content) / (N_atom + N_period))):
        f.write(f'{N_atom}\n')
        f.write(f'FORCE:    ...  ENERGY:  energy(sigma->0)\n')
        count = 0
        for atom_n, atom_t in zip(atom_num, atom_type):
            for n_add in range(1, int(atom_n) + 1):
                true_index = (N_atom + N_period) * i + N_period + n_add + count - 1
                f.write(f"{atom_t:>2}     {float(content[true_index].split()[0]):5.8f}     {float(content[true_index].split()[1]):5.8f}     {float(content[true_index].split()[2]):5.8f}\n")
            count += int(atom_n)

print("FINISHED!!!")
