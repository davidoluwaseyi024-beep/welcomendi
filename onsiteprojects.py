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

wellname = input("Please enter well name: ").split(",")
splited_well_name = wellname
wellid = input("Enter well ID: ").split(",")
splited_well_id = wellid
welllocation = input("Enter well location: ").split(",")
splited_well_location = welllocation
wellstatus = input("Enter well status: ").split(",")
splited_well_status = wellstatus
welldate = input("Enter well date: ").split(",")
splited_date = welldate
totalrevenue = input("Enter total revenue: ").split(",")
splited_revenue = totalrevenue

well_data = [
    splited_well_name,
    splited_well_id,
    splited_well_location,
    splited_well_status,
    splited_date,
    splited_revenue ]
print("Well data list: well_name well_id wellLocation wellStatus wellDate totalRevenue")
print(well_data)






