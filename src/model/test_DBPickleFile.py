from DBPickleFile import *
from unittest import TestCase

class Test_DBPickleFile(TestCase):

    class Table(Serialisable):
        def __init__(self):
            self.tableID=0
            self.name=""
            self.age=0

    class Bar(Serialisable):
        def __init__(self):
            self.tableID=0
            self.name=""
            self.age=0

    def __init__(self,*args,**kwargs):
        super(Test_DBPickleFile,self).__init__(*args,**kwargs)
        self.db=DBPickleFile("test_db.pck")
        self.db.startDatabase()

    def test_full_cycle(self):
        self.assertTrue(os.path.exists(self.db.fileName))
        self.t1=self.Table()
        self.t1.tableID=0
        self.t2=self.Table()
        self.t2.tableID=1
        self.t3=self.Table()
        self.t3.tableID=2
        self.assertTrue(self.db.addDataToDb(self.Table,self.t1))
        self.assertTrue(self.db.addDataToDb(self.Table,self.t2))
        self.assertTrue(self.db.addDataToDb(self.Table,self.t3))
        self.b1=self.Bar()
        self.b1.tableID=0
        self.b2=self.Bar()
        self.b2.tableID=1
        self.b3=self.Bar()
        self.b3.tableID=2
        self.assertTrue(self.db.addDataToDb(self.Bar,self.t1))
        self.assertTrue(self.db.addDataToDb(self.Bar,self.t2))
        self.assertTrue(self.db.addDataToDb(self.Bar,self.t3))
        self.assertListEqual([0,1,2],[ x.tableID for x in self.db.getListOfRecords(self.Bar) ]) # type: ignore
        self.assertEqual(3,self.db.getCountOfRecordsInTable(self.Table))
        self.assertEqual(3,self.db.getCountOfRecordsInTable(self.Bar))
        oldId=0
        self.t1.tableID=3
        self.db.updateDataInDb(self.Table,self.t1,oldId)
        self.assertListEqual([1,2,3],[ x.tableID for x in self.db.getListOfRecords(self.Table) ]) # type: ignore
        self.db.deleteDataFromDb(self.Table,lambda x: x.tableID==2) # type: ignore
        self.assertListEqual([1,3],[ x.tableID for x in self.db.getListOfRecords(self.Table) ]) # type: ignore
        self.assertEqual(3,self.db.getMaxIdFromTable(self.Table))
        self.assertEqual(3,self.db.getCountOfRecordsInTable(self.Bar))
        self.db.truncateTable(self.Table)
        self.assertListEqual([],[ x.tableID for x in self.db.getListOfRecords(self.Table) ]) # type: ignore
        self.assertListEqual([0,1,2],[ x.tableID for x in self.db.getListOfRecords(self.Bar) ]) # type: ignore
        self.db.resetAllDataInDb()
        self.assertListEqual([],[ x.tableID for x in self.db.getListOfRecords(self.Bar) ]) # type: ignore
