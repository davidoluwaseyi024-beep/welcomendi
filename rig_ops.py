# rig_ops.py
# NDI Phase 2 — Rig Operations Data System
# Author: [Your Name]
from logging import critical

# ── STARTER DATA ─────────────────────────────────────

# List of well dictionaries
wells = [
    {"name": "Bonga-01",   "pressure": 3850, "temp": 185, "active": True,  "engineer": "Emeka Eze"},
    {"name": "Bonga-03",   "pressure": 820,  "temp": 310, "active": True,  "engineer": "Chidi Obi"},
    {"name": "Erha-02",    "pressure": 4600, "temp": 200, "active": True,  "engineer": "Fatima Bello"},
    {"name": "Bonga-07",   "pressure": 2100, "temp": 175, "active": False, "engineer": "N/A"},
    {"name": "Erha-05",    "pressure": 3200, "temp": 290, "active": True,  "engineer": "Tunde Adeyemi"},
    {"name": "Agbami-02",  "pressure": 650,  "temp": 165, "active": True,  "engineer": "Ngozi Okafor"},
]

# Tuple of rig coordinates (NEVER changes)
rig_location = ("Bonga Field", 3.7800, 5.6200)

# Set of known alert types (starts empty)
active_alerts = set()

# ── YOUR CODE GOES BELOW THIS LINE ───────────────────
#task 1 rig_ops

print("TASK 1 — LISTS")
print("=" * 50)

print("\nAll wells on the rig:")
for well in wells:
    print(f"  - {well['name']}")

# Print only the first 3 wells using slicing
print("\nFirst 3 wells (sliced):")
for well in wells[:3]:
    print(f"  - {well['name']}")

# Print the total number of wells using len()
print(f"\nTotal number of well currently: {len(wells)} ")

# Add new well to the end of the list using .Append()
new_well = {"name": "Agbami-05", "pressure": 3100, "temp": 195, "active": True, "engineer": "Yemi Coker"}
wells.append(new_well)
print("\nAgbami-05 has been added to the rig.")

# Remove "Bonga-07" from the list using a loop to find it, then .remove()
well_to_remove = None
for well in wells:
    if well["name"] == "Bonga-07":
        wells.remove(well)
print("Bonga-07 (inactive) has been removed from the list.")

# Print the updated list length
print(f"Updated total wells: {len(wells)}")



#Task 2
# Using the rig_location tuple:
print(rig_location)
print(rig_location[0])
print(f"longtitude: {rig_location[0]}")

# Print latitude and longitude separately with f-strings
print(f"Latitude:  {rig_location[1]}")
print(f"Longitude: {rig_location[2]}")

# Attempting to change the latitude — this will cause a TypeError
# rig_location[1] = 4.0 .

# WHY TUPLES CANNOT BE CHANGED:
# Tuples are immutable — once created, their values are locked.
# This makes them perfect for data that must NEVER be modified,
print("\n[NOTE] Tuples are immutable — rig coordinates cannot be accidentally overwritten.")

#Task 3

#alert_log = [
    #"pressure_high", "valve_leak", "pressure_high",
   # "temp_spike", "valve_leak", "pump_failure", "pressure_high"
#]

unique_alerts = {"pressure_high", "valve_leak", "pressure_high", "temp_spike", "valve_leak", "pump_failure", "pressure_high"}
print(f"\nUnique alerts (duplicates removed): {unique_alerts}")
print(f"Number of unique alert types: {len(unique_alerts)}")
#Added a new alerts to set gas_leak
unique_alerts.add("gas_leak")
print("\n'gas_leak' alert has been added.")
unique_alerts.discard("temp_spike")
print("'temp_spike' has been cleared from alerts.")

# Check whether "valve_leak" is still in the set
if "valve_leak" in unique_alerts:
    print("\nvalve_leak — ALERT ACTIVE")
else:
    print("\nvalve_leak — Alert cleared")

 #Task4
    # Dictionaries map keys to values — perfect for storing structured well profiles

well_profile = {
    "name":         "Bonga-01",
    "pressure":     3850,
    "temp":         185,
    "status":       "Active",
    "engineer":     "Emeka Eze",
    "last_checked": "2026-04-01",
}
print("\nWell Profile — Bonga-01:")
for key, value in well_profile.items():
    print(f"  {key}: {value}")
well_profile.update({"pressure":4100})
print(f"\nPressure updated to: {well_profile['pressure']} psi")
well_profile["next_service"] = "2026-05-01"
print(f"Next service date added: {well_profile['next_service']}")

# Delete the "temp" key using del
del well_profile ["temp"]
print("'temp' field removed from profile.")

# check key status exit
for x in well_profile.key():
    if x == "status":
        print(True)

else:
    print("\n'status' key NOT found in the well profile.")

# Print only the keys, then only the values
print(f"\nProfile keys:   {list(well_profile.keys())}")
print(f"Profile values: {list(well_profile.values())}")

#Task 5
#skip inactive well, loop through every well

active_well_count = 0
critical_count = 0

for well in wells:
    #step 1 skip inactive wells
    if not well["active"]:

     continue

    active_well_count+= 1
    pressure = well ["pressure"]
    temp = well["temp"]

    #classify each well
    if pressure < 1000:
        status = "Critical"
    elif pressure < 2500:
        status = "low pressure"
    elif pressure < 280:
        status = "high temp"
    else:
        status = "normal"

   # Step 3 — Track alerts: add CRITICAL or HIGH TEMP to active_alerts set
    if status in ("Critical", "high temp", "low pressure"):
     active_alerts.add(status)

    # Count CRITICAL wells
    if status == "Critical":
     critical_count += 1

    # Step 4 — Print the per-well result line
    print(f"  {well['name']:<12} | {pressure} psi  | {status:<14} | Engineer: {well['engineer']}")

# After the loop — print summary
print()
print(f"  Total active wells checked : {active_well_count}")
print(f"  Active alerts              : {active_alerts}")
print(f"  CRITICAL wells             : {critical_count}")

#Task 6 Daily Operation Report

import datetime
today = datetime.date.today()

print()
print("─" * 50)
print("   BONGAFIELD RIG — DAILY OPERATIONS REPORT")
print(f"   Date: {today}")
print("─" * 50)

# Total wells and active count
total_wells = len(wells)
print(f"\n  Total wells in system : {total_wells}")
print(f"  Total active wells    : {active_well_count}")

# List active wells with their classification
print("\n  ACTIVE WELL STATUS:")
print("  " + "─" * 46)
flagged_wells = []  # collect CRITICAL or HIGH TEMP wells for the next section

for well in wells:
    if not well["active"]:
        continue

    pressure = well["pressure"]
    temp = well["temp"]

    # classify same thing with the Task 5)
    if pressure < 1000:
        well_status = "CRITICAL"
    elif pressure < 2500:
        well_status = "LOW PRESSURE"
    elif temp > 280:
        well_status = "HIGH TEMP"
    else:
        well_status = "NORMAL"

    print(f"  {well['name']:<12} | {pressure} psi | {well_status}")

    if well_status in ("CRITICAL", "HIGH TEMP"):
        flagged_wells.append((well["name"], well_status, well["engineer"]))

# Section: wells requiring urgent attention
print()
print("  ⚠  WELLS REQUIRING IMMEDIATE ATTENTION:")
print("  " + "─" * 46)
if flagged_wells:
    for name, w_status, engineer in flagged_wells:
        print(f"  [{w_status}] {name}  — Assigned Engineer: {engineer}")
else:
    print("  No critical or high-temp wells at this time.")

# Active alerts section
print()
print("  ACTIVE ALERT TYPES:")
print("  " + "─" * 46)
if active_alerts:
    for alert in active_alerts:
        print(f"  >> {alert}")
else:
    print("  No active alerts.")

# Footer
print()
print("─" * 50)
print("  Report generated by BongaTech Rig Ops System")
print(f"  Rig: {rig_location[0]}  |  Lat: {rig_location[1]}  |  Lon: {rig_location[2]}")
print("─" * 50)
