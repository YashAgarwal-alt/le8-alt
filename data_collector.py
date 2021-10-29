import sys

def data_collect(f):
    file = open(f, "r")

    instruction_storage = dict()
    data_storage = dict()

    for line in file.readlines():
        temp = line.split(",");
        tracer = temp[0][:-3]
        access_type = temp[1]
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
    
    print("Instructions:")
    for x in sorted(instruction_storage.items(), reverse=True):
	    print(x[0] + "," + str(x[1]))
    print("Data:")
    for x in sorted(data_storage.items(), reverse=True):
        print(x[0] + "," + str(x[1]))

if __name__ == "main":
    data_collect(sys.argv[1])