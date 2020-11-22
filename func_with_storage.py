import lithops
from storage_util import get_bucket_contents

def list_bucket(bucket_name):
    get_bucket_contents(bucket_name)

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(list_bucket, 'lithops-bucket-habib01')
    print(fexec.get_result())