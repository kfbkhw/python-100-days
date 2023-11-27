with open("./Input/Names/invited_names.txt") as names:
    demo_list = names.readlines()
    name_list = []
    for name in demo_list:
        clean_name = name.strip()
        name_list.append(clean_name)

for name in name_list:
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        template = starting_letter.read()
    content = template.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as letter:
        letter.write(content)
