import lithops

def hello_world(name):
    return 'Hello {}!'.format(name)

def hello_world2(name):
    return 'Hello World'

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    # fexec.call_async(hello_world, 'World')
    fexec.call_async(hello_world2,'halo')
    print(fexec.get_result())