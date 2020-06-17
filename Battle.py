from sqliteTwist import simpleToolSql
import random
class CBattle():
    def __init__(self, Con):
        self.con = Con

    def getEnemy(self, enemyID):
        res = self.con.query("select * from Enemy where id = ?;", (enemyID,))
        self.name     = res[0][1]
        self.BP       = res[0][2]
        self.itemDrop = res[0][3].split(',')
        dropRate = res[0][4].split(',')
        self.dropRate = []
        for i in dropRate:
            self.dropRate.append(int(i))
        return res

    def DoAttack(self, cb):
        print("Attack")
        cb(self.name)            

if __name__ == "__main__":
    DbCon = simpleToolSql("Dta")
    b =CBattle(DbCon)
    b.getEnemy(1)
    print(b.itemDrop)
    print(b.dropRate)
    DbCon.close()
