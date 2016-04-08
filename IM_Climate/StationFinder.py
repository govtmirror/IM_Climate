try:    #python 2.x
    from StationInfo import StationInfo
    from ACIS import ACIS
    import hucs
except:     #python 3.x
    from .ACIS import ACIS
    from .StationInfo import StationInfo

class StationFinder(ACIS):
    def __init__(self, *args, **kwargs):
        super(StationFinder,self).__init__(*args, **kwargs)
        self.webServiceSource = 'StnMeta'

    def find(self, state = None, parameter = None, countyCode = None,
        bbox = None, HUC = None, startDate = None, endDate = None, **kwargs):
        '''
        INFO
        ----
        Standard method to find all stations and associated metadata
        based on zero or more criteria.

        ARGUMENTS
        ---------
        state - Two-letter state acronym (e.g., CO)
        parameter - Parameter code for weather element (e.g., tmin)
        countyCode - County fips code (e.g., 08117)
        bbox - A latitude/longitude bounding box defined
            in decimal degrees (West, South, East, North) with negative
            values indicating west longitude and south latitude
            (e.g. -90.7, 40.5, -88.9, 41.5).
        HUC - 8-digit hydrological unit
        startDate -
        endDate -


        RETURNS
        -------
        A station info object of station metadata
        '''
        metadata = ['uid', 'name', 'state', 'll', 'elev', 'valid_daterange']
        if not parameter:
            parameter = ['pcpn', 'snwd', 'avgt', 'obst', 'mint', 'snow', 'maxt']

        self.input_dict = {}    #Clears the input dictionary
        results =  self._call_ACIS(state = state, elems = parameter
            ,county = str(countyCode), bbox = bbox, basin = str(HUC) , meta = metadata
            , **kwargs)

        return StationInfo(results, queryParams = self.input_dict)

    def HUCs(self):
        '''
        Returns all of the HUC Codes
        '''
        return hucs.hucs

if __name__ == '__main__':
    c = StationFinder()
    print(c.parameters)
    stationInfo =  c.find(parameter = 'avgt', countyCode = '08117', startDate = '1980-01-01', endDate = '1981-12-31')
    print stationInfo
##    stationInfo =  c.find( countyCode = '08117')
##    stationInfo = c.find(HUC = 14010001, parameter = 'mint')
##    print(stationInfo.stationIDs)
##    print(stationInfo.metadata)
##    print c.HUCs()[0:5]
