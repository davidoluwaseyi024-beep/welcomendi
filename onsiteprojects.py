#1 task Collect raw data

print("oil well production report ")
print("please Enter wells_id in this format: WellA-1500, wellb-2000, wellC-1750")

well_name=input ("Well name")
well_id=input ("Well Id")
well_location=input ("Well Location")
well_status=input ("Well Status")
well_date=input ("dd/mm/yyyy")
total_revenue=input ("7 Barrels")

#2 task clean report

report = f"{well_name} {well_id} {well_location} {well_date} {well_date} {total_revenue} "
print("everything to lowercase")
cleaned = report.lower()
cleaned = cleaned.replace("," ,":")
print("\nCleaned Report:")
print(cleaned)

#3 Task spliting data
wellname= input("please enter well name:")
splited_well_name = wellname.split(" ,")
wellid= input("enter well id:")
splited_well_id = well_id.split(" ,")
welllocation= input("enter well location:")
splited_well_location = well_location.split(" ,")
wellstatus = input("enter well status:")
splited_well_status = well_status.split(" ,")
welldate= input("enter well date:")
splited_date = well_date.split(" ,")
totalrevenue= input("enter total revenue:")
splited_revenue = totalrevenue.split(" ,")
print("splited_wellname:, splited_id:, splited_well_location:, splited_status:, splited_date:,")






