import lithops
import pyodbc 

def connect(tablename):
    server = 'cap-au-sg-prd-04.securegateway.appdomain.cloud,15275' 
    database = 'jtiiasset' 
    username = 'sa' 
    password = 'Pas5word' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM ' + tablename)

    for row in cursor:
        print(row)

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(connect,'asset_inventory')
    print(fexec.get_result())