import openpyxl, pprint
print("Opening workbook...")

wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}

#Fill in countyData with each couty's population & tracts.
print("Reading rows...")