from common import missingValue

class observation(dict):

    def __init__(self, values):
        self['date'] = values[0].encode()
        self['wxOb']  = values[1].encode()
        self._replaceBlanks()

    @property
    def date(self):
        return self['date']

    @property
    def wxOb(self):
        return self['wxOb']

    def _replaceBlanks(self):
        #replace blanks with the missing value
        for index, value in self.items():
            if len(value.strip()) == 0:
                self[index] = missingValue

class monthlyOb(observation):
    def __init__(self, values):
        super(monthlyOb, self).__init__(values)
        self['countMissing'] = values[2]

    @property
    def countMissing(self):
        return self['countMissing']


class WxOb(observation):
    ''''
    A dictionary containing a weather observation for a specific station, parameter and date
    WxOb is indexable like a standard dictionary although values can also
    be accessed as properties:
        -WxOb.date
        -WxOb.wxOb, etc).
        -WxOb.ACIS_Flag
        -WxOb.sourceFlag
    '''
    def __init__(self, values):

        self['ACIS_Flag'] = values[2].encode()
        self['sourceFlag'] = values[3].encode()
        super(WxOb, self).__init__(values)

    @property
    def ACIS_Flag(self):
        return self['ACIS_Flag']
    @property
    def sourceFlag(self):
        return self['sourceFlag']

if __name__=='__main__':

    #Daily data
    data = ['2012-02-01',u'32.0', u' ', u'U']
    wx = WxOb(data)
    print wx

    #Monthly data
    data = [u'2012-01', u'22.60', 0]
    dmonth = monthlyOb(data)
    print dmonth