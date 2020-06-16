from sqliteTwist import *

class CActions():
	def __init__(self, DbConn):
		self.DbCon = DbConn

	def DoRock():
		self.DbCon.execute("UPDATE MainCharacter SET Level=?, LevelMax=?, Exp=?, NextExp=?, TotalExp=? WHERE Name=?",
			(self.Level, self.LevelMax, self.Exp, self.NextExp, self.TotalExp, self.Name))


if __name__ == "__main__":
	if os.path.isfile("init") == False:
		DbCon = simpleToolSql("Dta")
		f = DbCon.execute("create table Item (Name text,Type text, Number int,Describe text);")
		DbCon.execute("insert into Item (Name,Type,Number,Describe) values (?,?,?,?);",[("Scale","Item",0,"A Scale")])
		DbCon.execute("insert into Item (Name,Type,Number,Describe) values (?,?,?,?);",[("Bronze","Item",0,"A Bronze Rock")])
		DbCon.close()
	else:
		DbCon = simpleToolSql("Dta")
		act = CActions(DbCon)
