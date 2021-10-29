import sys

def data_collect(f, written_to):
    file = open(f, "r")

    instruction_storage = dict()
    data_storage = dict()

    for line in file.readlines():
        temp = line.split(",")
        tracer = temp[0][:-3]
        access_type = temp[1].strip()
        # print(access_type)
        # print(type(access_type))
        if access_type == "I":
            if tracer in instruction_storage:
                instruction_storage[tracer] += 1
            else:
                instruction_storage[tracer] = 1
        else:
            if tracer in data_storage:
                data_storage[tracer] += 1
            else:
                data_storage[tracer] = 1
    file.close()

    print(data_storage)
    print("-------------------------------")
    print(instruction_storage)
    file = open(written_to, "w")
    file.write("Instructions:\n")
    for x in sorted(instruction_storage.items(), reverse=True, key=lambda entry: entry[1]):
        file.write(x[0] + "," + str(x[1]) + "\n")
    file.write("\nData:\n")
    for x in sorted(data_storage.items(), reverse=True, key=lambda entry: entry[1]):
        file.write(x[0] + "," + str(x[1]) + "\n")
    file.close()


data_collect("tr-heaploop.ref", "tr-heaploop-data.txt")
data_collect("tr-matmul.ref", "tr-matmul-data.txt")
