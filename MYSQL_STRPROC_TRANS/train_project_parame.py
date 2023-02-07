import mysql.connector
from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclstoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata=('123',)
            self.cursor.callproc("get_no_avl_sts",mydata)#by cursor object we arre calling stored procedure
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()#realising the cursor
                self.connection.close()

connect_obj=HclstoredProcedure();
connect_obj.connect('localhost','root','Root','train')
connect_obj.execute_str_procedure()