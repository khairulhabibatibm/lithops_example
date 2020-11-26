import lithops

inputs = ['Habib','Galang','Khairul']

def my_map_function(data):
    return "Hello " + data

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.map(my_map_function,inputs)
    print(fexec.get_result())