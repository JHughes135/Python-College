input_file = open("hnr.abc", "r")
output_file = open("output.txt", "w")

for line in input_file:
    if (line[:1] == 'X') and (line[1:2] == ':'):
        print(line, file=output_file)

    if (line[:1] == 'T') and (line[1:2] == ':'):
        print(line, file=output_file)

    if (line[:1] == 'M') and (line[1:2] == ':'):
        print(line, file=output_file)

    if (line[:1] == 'K') and (line[1:2] == ':'):
        print(line, file=output_file)

input_file.close()
output_file.close()
