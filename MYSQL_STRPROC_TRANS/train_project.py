from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")
            #self.r=self.cursor.stored_results()
            #print(self.r)
            for r in self.cursor.stored_results():
                #print(r.fetchall())
                seats=r.fetchone()
            return seats
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass
b1=Booking()
b1.connect('localhost','root','Root','train')
sts=b1.available_seats()
seats_avl={}
seats_avl['Train_name']=sts[0]
seats_avl['Seats']=sts[1]
print(seats_avl)