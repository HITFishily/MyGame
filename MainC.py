from sqliteTwist import *
import os.path
class CMainCharacter():
	def __init__(self, DbConn):
		res = DbConn.query("select * from MainCharacter;")
		#print(res)
		self.Name 			= res[0][0]
		self.Level 			= res[0][1]
		self.LevelMax		= res[0][2]
		self.Exp			= res[0][3]
		self.NextExp		= res[0][4]
		self.TotalExp		= res[0][5]

		self.DbCon			= DbConn

	def UpdateDB(self):
		self.DbCon.execute("UPDATE MainCharacter SET Level=?, LevelMax=?, Exp=?, NextExp=?, TotalExp=? WHERE Name=?",
			(self.Level, self.LevelMax, self.Exp, self.NextExp, self.TotalExp, self.Name))

	def setLevel(self):
		self.Level = self.Level + 1

	def isLevelUp(self):
		if self.Exp >= self.NextExp:
			self.Level 	 = self.Level + 1
			self.Exp 	 = self.Exp - self.NextExp
			self.NextExp = self.NextExp + 10
			return True
		return False 

	def IncreaseExp(self, exp):
		self.Exp 		= self.Exp + exp
		self.TotalExp 	= self.TotalExp + exp
		return self.isLevelUp()

if __name__ == "__main__":
	if os.path.isfile("init") == False:
		DbCon = simpleToolSql("Dta")
		f = DbCon.execute("create table MainCharacter (Name text,Level int, LevelMax int, Exp int, NextExp int, TotalExp int);")
		f = DbCon.execute("create table MainCharacter (Name text,Level int, LevelMax int, Exp int, NextExp int, TotalExp int);")
		DbCon.execute("insert into MainCharacter (Name,Level,LevelMax,Exp,NextExp,TotalExp) values (?,?,?,?,?,?);",[('Guo',1,20,0,5,0)])
		DbCon.close()
	else:
		DbCon = simpleToolSql("Dta")
		mc = CMainCharacter(DbCon)
		mc.setLevel()
		mc.UpdateDB()
		DbCon.close()