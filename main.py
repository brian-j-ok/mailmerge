with open('Input/Names/invited_names.txt', 'r') as names_file:
    names = [line.strip() for line in names_file]

with open('Input/Letters/starting_letter.txt') as letter_file:
    template = letter_file.readlines()

print(names)
print(template)

for name in names:
    with open(f'Output/ReadyToSend/{name}.txt', 'w') as invitation:
        for line in template:
            invitation.write(line.replace("[name]", name))
