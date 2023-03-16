from bsedata.bse import BSE
from pprint import pprint
from datetime import datetime
b = BSE()
b = BSE(update_codes = True)
scripCode = b.getScripCodes()
scripCodeList = list(scripCode.items())
print(str(len(scripCode.keys())))
filename = "BseMarketData_"+datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+".txt"
with open(filename,'w') as f:
	columnHeader = "Status,scripCode,companyName,2WeekAvgQuantity,52weekHigh,52weekLow,change,currentValue,dayHigh,dayLow,faceValue,marketCapFreeFloat,marketCapFull,pChange,previousClose,previousOpen,totalTradedQuantity,totalTradedValue,updatedOn,weightedAvgPrice"
	f.write(columnHeader)
	f.write("\n")
	rowValue = ""
	for r in range(0,len(scripCode.keys())+1):
		print(r)
		try:		
			q = b.getQuote(str(scripCodeList[r][0]))
			rowValue = rowValue+ "Success,"+str(q["scripCode"]).replace(",","")+","+str(q["companyName"]).replace(",","")+","+str(q["2WeekAvgQuantity"]).replace(",","")+","+str(q["52weekHigh"]).replace(",","")+","+str(q["52weekLow"]).replace(",","")+","+str(q["change"]).replace(",","")+","+str(q["currentValue"]).replace(",","")+","+str(q["dayHigh"]).replace(",","")+","+str(q["dayLow"]).replace(",","")+","+str(q["faceValue"]).replace(",","")+","+str(q["marketCapFreeFloat"]).replace(",","")+","+str(q["marketCapFull"]).replace(",","")+","+str(q["pChange"]).replace(",","")+","+str(q["previousClose"]).replace(",","")+","+str(q["previousOpen"]).replace(",","")+","+str(q["totalTradedQuantity"]).replace(",","")+","+str(q["totalTradedValue"]).replace(",","")+","+str(q["updatedOn"]).replace(",","")+","+str(q["weightedAvgPrice"]).replace(",","")+"\n"	
		except Exception as error:
			rowValue = rowValue+ "Error,"+str(scripCodeList[r][0])+","+str(scripCodeList[r][1])+"\n"
	f.write(rowValue)


