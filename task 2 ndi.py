 #Welcome NDI Task 1

def greet_engineer(name):
    print(f"Good morning, {name} Ready to monitor the rig?")

greet_engineer("Emeka")
greet_engineer("David")

#A2
def rig_status(well_name, is_Active):
    if is_Active:
     print(f"{well_name} Is ONLINE")
    else:
     print(f"{well_name} Is OFFLINE maintainace required")
rig_status("Well burna-1", True)
rig_status("Well sly-7", False)
rig_status("Well David-2", True)

#A3
def calculate_daily_output(flow_rate, Hours_active):
    return flow_rate * Hours_active
print(f":daily_output{calculate_daily_output(flow_rate=45, Hours_active=56)}barrels")

print(calculate_daily_output(70, 16))
print(calculate_daily_output(80, 12))
print(calculate_daily_output(100, 22))
#task B
def classify_pressure(pressure):
    if pressure > 1000:
        return "CRITICAL"
    elif 1000 <=pressure<2500:
        return "LOW"
    elif 2500 <=pressure<4500:
        return "NORMAL"
    elif pressure >=4500:
        return "OVERPRESSURE"
    else:
        return "INACTIVE"

print(classify_pressure(100))
print(classify_pressure(3000))
print(classify_pressure(4700))
print(classify_pressure(7000))

#Task B2
def maintenance_due(days_since_service):
    if days_since_service > 90:
        return "OVERDUE"
    elif days_since_service > 60:
        return "DUE SOON"
    else:
        return "OKAY"

print(maintenance_due(50))
print(maintenance_due(20))
print(maintenance_due(98))

#Task B3
def access_level(role):
    match role:
        case "supervisor":
            return "full access"
        case "engineer":
            return "Operational access"
        case "contactor":
            return "limited access"
        case _:
            return "No access"

print(access_level("supervisor"))
print(access_level("engineer"))
print(access_level("contactor"))
print(access_level("aphla"))

#Task C
wells = [
        {"name": "Bonga-01", "pressure": 3850},
        {"name": "Bonga-03", "pressure": 820},
        {"name": "Erha-02", "pressure": 4600},
        {"name": "Erha-05", "pressure": 3200},
        {"name": "Agbami-02", "pressure": 650},
    ]
def check_all_wells(wells):
    for well in wells:
        status = classify_pressure(well["pressure"])
        print(well["name"], "|", well["pressure"], "| psi", status)

check_all_wells(wells)

def count_critical(wells):
        count = 0
        for well in wells:
            if well["pressure"] < 1000:
                count += 1
        return count

critical_total = count_critical(wells)
print(count_critical(wells), "well(s) are in CRITICAL condition")

#C3 pressure monitor

def pressure_monitor():
    while True:
        operator = input("Enter pressure reading (or 0 to quit): ")
        pressure = int(operator)
        if pressure == 0:
            print("Monitoring stopped.")
            break
        status = classify_pressure(pressure)
        print("status:", status)



print(pressure_monitor())

#Task D
def run_daily_check(wells):
        wells = [
            {"name": "Bonga-01", "pressure": 3850},
            {"name": "Bonga-03", "pressure": 820},
            {"name": "Erha-02", "pressure": 4600},
            {"name": "Erha-05", "pressure": 3200},
            {"name": "Agbami-02", "pressure": 650},
        ]
        for well in wells:
            if well["pressure"] == 0:
                continue
            maintenance_due(45)
            print(f"{well} maintenance due {maintenance_due(45)}")
print(run_daily_check("wells"))

print(f"critical_total: {critical_total} maintenance_due: {maintenance_due(45)}")
