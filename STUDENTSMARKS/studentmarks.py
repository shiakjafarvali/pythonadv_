import pandas as pd
import numpy as np
# df=pd.read_csv("C://Users/user786/Desktop/Book1.csv")
#df['Total']=df.iloc[:].sum(axis=1)
#print(df)
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df1=pd.read_csv(self.path)
        # self.df=pd.DataFrame(self.path)
        print("hello")
        return self.df1
    def total_df(self):
        #self.df['Total']=self.df['M1']+self.df['M2']+self.df['M3']+self.df['M4']+self.df['M5']
        self.df1['Total'] = self.df1.iloc[:,2:].sum(axis=1)
        return self.df1
    def avg_df(self):
        self.df1['avg]']=self.df1['Total']/5
        return self.df1
        self.df1['Rank']=self.df1['avg'].rank()
        self.df['Result']=np.where((self.df1['M1']>=35 & self.df1['M2']>=35 & self.df1['M3']>=35 & self.df1['M4']>=35 & self.df1['M5']>=35))
        print(self.df1.sort_values(by=['Rank']))
        print(self.df1['Total'])
obj=Readcsv()
print(obj.create_df("c://Users/user786/Desktop/Book1.csv"))
print(obj.total_df())
print(obj.avg_df())