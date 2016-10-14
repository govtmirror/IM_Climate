library(IMClimateR)

# ACIS Data Service Docs: http://www.rcc-acis.org/docs_webservices.html

findStation(parkCodes = "MABI", climateParams=list('pcpn'))
findStation(parkCodes = "MABI", distance=10, climateParams=list('pcpn'))
findStation(parkCodes = "MABI", distance=10, climateParams=list('pcpn'), filePathAndName = "mabi.csv")
stations <- findStation(parkCodes = "AGFO", distance=10)
getDailyWxObservations(list('pcpn', 'avgt', 'obst', 'mint', 'maxt'), 25056, "20150801", "20150831")
getDailyWxObservations(list('pcpn', 'avgt', 'obst', 'mint', 'maxt'), 17611, "20150801", "20150831")
getDailyWxObservations(list('pcpn', 'avgt', 'obst', 'mint', 'maxt'), 25056, "20150801", "20150810", filePathAndName = "dailyWx.csv")
getDailyWxObservations(list('pcpn', 'avgt', 'obst', 'mint', 'maxt'), 60903)
getDailyWxObservations(climateParameters=list('pcpn', 'avgt', 'obst', 'mint', 'maxt'), climateStations=stations, sdate="20150801", edate="20150803")
getDailyGrids(unitCode = list("AGFO"), distance=10, sdate = "20150801", edate = "20150803", climateParameters = list("mint", "maxt"))