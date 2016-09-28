__author__ = 'Vincent'

import _mysql

class ServerAction(object):

    def __init__(self, clientString):

        self.clientString = clientString
        self.returnMsg = ""
        self.type = self.clientString[0:2]

        if self.type == "TX":
            self.fromAcct = self.clientString.split("$")[1]
            self.Amount = int(self.clientString.split("$")[2])
            self.toAcct = self.clientString.split("$")[3]
            self.washAcct = "W999999"


    def sendSQL(self, sqlString, retunsValue):

        db = _mysql.connect(host="localhost",user="python",passwd="sqlPassword",db="txdb")
        db.query(sqlString)

        if retunsValue == False:
            return None
        else:
            r = db.store_result()
            return r.fetch_row(0)


    def credit(self, acct, amt):
        sqlString = "Call %s ('%s',%d)" %("CREDIT", acct, amt)
        return self.sendSQL(sqlString, False)

    def debit(self, acct, amt):
        sqlString = "Call %s ('%s',%d)" %("DEBIT", acct, amt)
        return self.sendSQL(sqlString, False)

    def balance(self, acct):
        sqlString = "Call %s ('%s', @var)" %("BALANCE", acct)
        return int(self.sendSQL(sqlString, True)[0][0])

    def sufficient_funds(self, acct):

        if self.balance(acct) - self.Amount >0:
            return True
        else:
            return False


    def transact(self):

        if self.type == "TX":
            if self.sufficient_funds(self.fromAcct) == True:

                self.debit(self.fromAcct,self.Amount)
                self.credit(self.washAcct,self.Amount)
                self.debit(self.washAcct,self.Amount)
                self.credit(self.toAcct,self.Amount)

                self.returnMsg = "$TX RECORDED"
            else:
                self.returnMsg = "$TX REJECTED: INSUFFICIENT FUNDS"



        print self.balance(self.fromAcct)
        print self.returnMsg

