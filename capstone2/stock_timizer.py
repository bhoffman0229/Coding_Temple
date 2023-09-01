



#  MULTIPLIER <->  single number <-> the repeat value for timespan
#  TIMESPAN   <->  hour/day/week/month/quarter/yea
#  FROM       <->  (YYYY-MM-DD)
#  TO         <->  (YYYY-MM-DD)
#  DATE       <->  (YYYY-MM-DD)

# This class handles the time and date formatting

class TimeConstruct():
# set these parameters in the class call to get the required date formats
    def __init__(self, MULTIPLIER, TIMESPAN, FROM, TO, DATE):
        self.MULTIPLIER = MULTIPLIER
        self.TIMESPAN = TIMESPAN
        self.FROM = FROM
        self.TO = TO
        self.DATE = DATE

# AGG = MULTI + TIMESPAN + FROM + TO
    def getAGG(self):
        AGGstamp = str(self.MULTIPLIER)+","+str(self.TIMESPAN).lower()+","+str(self.FROM)+","+str(self.TO)
        return AGGstamp
# DAILY_OPENCLOSE = DATE
    def getOPENCLOSE(self):
        return str(self.DATE)
# DAILY_CRYPTO_OPENCLOSE = DATE
    def getCOPENCLOSE(self):
        COCstamp = str(self.DATE)
        return COCstamp
# GROUPED_DAILY = DATE
    def getGROUPED(self):
        GDstamp = str(self.DATE)
        return GDstamp


