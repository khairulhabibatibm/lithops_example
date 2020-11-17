import lithops
from myfunc import my_map_function

iterdata = [1,2,3,4,5]

if __name__ == '__main__':
    pw = lithops.function_executor() 
    futures = pw.map(my_map_function, iterdata)
    print (pw.get_result())
    pw.clean()
