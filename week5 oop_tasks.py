import json
import re

well_data = {
    "name": "well-01 ",
    "pressure":  2450.6,
    "temperature": 70.5,
    "active": True,
    "engineer": "David oluwaseyi"
}

#converting to jason and print
json_str = json.dumps(well_data)
print(json_str)
print(json.dumps(well_data, indent=2))
print(json.dumps(well_data, sort_keys=True, indent=2))


# 1B JSON to Dict
json_str = '''
{
    "name": "Erha-02",
    "pressure": 3850,
    "temp": 185,
    "active": true,
    "engineer": "David oluwaseyi"
}
'''

well_data = json.loads(json_str)
print(well_data)

#access the engineer name directly
print(well_data['engineer'])

#updating the pressure value
well_data["pressure"] = 4200
print(well_data["pressure"])

#convert dict back to json
update_json = json.dumps(well_data, indent=2)
print(update_json)

#1C write json file
wells_json = {
     "well_01": 3200,
     "well_02": 5100,
     "well_03":  4530,
 }

y = json.dumps(wells_json)
print(y)

#2A  —  Search and Match
log_entry = 'Pressure alert triggered on well_003 at 04:32 UTC'
match = re.search("well_003", log_entry)
# Print the match object
print("Match object:")
print(match)
# print the match object using .object
print(match.group())

#2B findall matches
ops_log = '''
Erha-02 pressure normal. Bonga-01 valve checked.
Agbami-05 flagged for review. Bonga-01 cleared.
Erha-02 output at 94%. Bonga-07 offline.
'''
#Finding all well names
all_wells = re.findall(r'[A-Za-z]+-\d+', ops_log)
print("all_wells:", all_wells)

# Find unique well names
unique_wells = set(all_wells)
print("unique_wells:", unique_wells)

# Check if a specific well appears in the log
match = re.search(r'Agbami-05', ops_log)
if match:
    print("Found:", match.group())
else:
    print("Well not found")
# finding flagged wells
flagged_wells = re.findall(r'[A-Za-z]+-\d+\s+flagged for review', ops_log)
print("flagged_wells:", flagged_wells)

#find well that are offline
offline_wells = re.findall(r'[A-Za-z]+-\d+\s+offline', ops_log)
print("offline wells:", offline_wells)

#2c validate input
def validate_well_id(well_id):
    pattern = r'^[A-Za-z]{1,10}-\d{2}$'
    return bool(re.match(pattern, well_id))
print(validate_well_id('Bonga-01'))
print(validate_well_id('bonga1'))
print(validate_well_id('Erha-02'))
print(validate_well_id('well-03'))

#3A Basic error catching
def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'cannot divide by zero'
    except TypeError:
        return 'Invalid input'

    return bool(safe_divide(a,b))
print(safe_divide(100, 4))
print(safe_divide(100, 0))
print(safe_divide(100, 'x'))

#3B multiple exceptions + finally
def load_well_pressure(data, key):
    try:
        return float(data[key])
    except KeyError:
        print('Key not found in well data')
        return None
    except ValueError:
        print('pressure value cannot be converted to a number')
    finally:
        print("Pressure check complete")

#Test with valid data
well = {"pressure": "3200.5", "temperature": "85"}
load_well_pressure(well, "pressure")
print(well["pressure"])

#Missing key test
load_well_pressure(well, "depth")
print(well["pressure"])

# Test 3 — non-numeric value
well2 = {"pressure": "N/A", "temp": "85"}
load_well_pressure(well2, "pressure")


#3C raise my error
def set_pressure(value):
    if value == "N/A":
        raise ValueError("pressure cannot be negetative")
    return value

try:
    set_pressure(-500)
except ValueError as e:
    print(f"Error caught: {e}")


#4A string formating
well_name = "Bonga-01"
pressure = 3200.5
engineer = "David oluwaseyi"

# 1 — % formatting (oldest method)
print("Well: %s | Pressure: %.1f | Engineer: %s" % (well_name, pressure, engineer))

# 2 — .format() method
print("Well: {} | Pressure: {:.1f} | Engineer: {}".format(well_name, pressure, engineer))

# 3 — f-string (modern method)
print(f"Well: {well_name} | Pressure: {pressure} | Engineer: {engineer}")

print("---")

#float rounded to 2 decimal
oil_rate = 4521.67
print(f"Oil rate: {oil_rate:.2f} bbl/day")

#4B None
engineer = None
if engineer is None:
    print("no engineer assigned")
else:
    print(f"engineer: {engineer}")

print("---")

# Function using .get() returns None if key doesn't exit
def get_well_status(well):
    if 'Active' in well:
        return well.get("Active")
    else:
        return None

# different btwn NONE, zero and empty str
# None that means there is no value assigned to it(None = 0 )
# 0 that means a number was still assigned and it is zero(None == '')
# '' string was assigned but it is empty print(0== '')

#4C user input
well_name = input("Enter well name: ") #Here I used the input() function to ask the user to type in a well name and a pressure reading
try:
    pressure = int(input("Enter pressure reading: "))#the int convert from text to num
except ValueError:
    print("Invalid input")

print(f"\nwell report - Well: {well_name} | Pressure: {pressure} psi")


#Task 5 Classes
# 5A — Classes and Objects
class Well:
    def __init__(self, name, pressure, temp, active=True, engineer=None):
        self.name     = name #self refer to specific object created
        self.pressure = pressure
        self.temp     = temp
        self.active   = active
        self.engineer = engineer

    def describe(self):
        print(f"Well: {self.name} | Pressure: {self.pressure} psi | Temp: {self.temp}°C | Active: {self.active} | Engineer: {self.engineer}")

    def is_critical(self):
        return self.pressure < 1000 or self.temp > 300

    def assign_engineer(self, name):
        self.engineer = name
        print(f"Engineer '{name}' has been assigned to {self.name}")

# Create the 3 Well objects
well1 = Well("Bonga-01", pressure=3200, temp=85.5)
well2 = Well("Erha-02",  pressure=800,  temp=310.0, active=False)
well3 = Well("Agbami-05",pressure=4500, temp=120.0, engineer="David oluwaseyi")

print("=== Well Descriptions ===")
well1.describe()
well2.describe()
well3.describe()

print("\n=== Critical Status ===")
print(f"{well1.name} critical: {well1.is_critical()}")  # False
print(f"{well2.name} critical: {well2.is_critical()}")  # True  — low pressure AND high temp
print(f"{well3.name} critical: {well3.is_critical()}")  # False
print(well1.temp)
print(well1.pressure)
print("\n=== Assign Engineer ===")
well1.assign_engineer("David Oluwaseyi")
well1.describe()


#Task 6 Properties, Setters, and Class Variables

class Well:
    well_count = 0

    def __init__(self, name, pressure, temp, active=True, engineer=None):
        self.name     = name
        self._pressure = pressure    # _ means 'private by convention'
        self.temp     = temp
        self.active   = active
        self.engineer = engineer
        Well.well_count += 1


    @property
    def pressure(self):
        return self._pressure

    #  pressure setter
    @pressure.setter
    def pressure(self, value):
        if value < 0:
            raise ValueError("Pressure cannot be negative")
        self._pressure = value

    # status property
    @property
    def status(self):
        if self._pressure < 1000:
            return "CRITICAL"
        elif self._pressure < 2500:
            return "LOW"
        elif self._pressure < 4500:
            return "NORMAL"
        else:
            return "OVERPRESSURE"

    # class method
    @classmethod
    def get_well_count(cls):
        return cls.well_count

    def describe(self):
        print(f"Well: {self.name} | Pressure: {self._pressure} psi | Status: {self.status} | Engineer: {self.engineer}")

    def is_critical(self):
        return self._pressure < 1000 or self.temp > 300

    def assign_engineer(self, name):
        self.engineer = name
        print(f"Engineer '{name}' has been assigned to {self.name}")


# Create 4 Well objects (covers all 4 status values)
well1 = Well("Bonga-01",   pressure=500,  temp=85.0)
well2 = Well("Erha-02",    pressure=1800, temp=90.0)
well3 = Well("Agbami-05",  pressure=3200, temp=100.0)
well4 = Well("Forcados-03",pressure=5000, temp=110.0)
print(" Well Count ")
print(f"Total wells created: {Well.get_well_count()}")

print("\nStatus for each well ")
well1.describe()
well2.describe()
well3.describe()
well4.describe()

print("\n Try setting a negative pressure ")
try:
    well1.pressure = -300
except ValueError as e:
    print(f"Error caught: {e}")

print("\n=== Pressure unchanged after failed set ===")
well1.describe()

#7 Inheritance

class Well:
    well_count = 0

    def __init__(self, name, pressure, temp, active=True, engineer=None):
        self.name      = name
        self._pressure = pressure
        self.temp      = temp
        self.active    = active
        self.engineer  = engineer
        Well.well_count += 1

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        if value < 0:
            raise ValueError("Pressure cannot be negative")
        self._pressure = value

    @property
    def status(self):
        if self._pressure < 1000:
            return "CRITICAL"
        elif self._pressure < 2500:
            return "LOW"
        elif self._pressure < 4500:
            return "NORMAL"
        else:
            return "OVERPRESSURE"

    @classmethod
    def get_well_count(cls):
        return cls.well_count

    def describe(self):
        print(f"Well: {self.name} | Pressure: {self._pressure} psi | Status: {self.status} | Engineer: {self.engineer}")

    def is_critical(self):
        return self._pressure < 1000 or self.temp > 300

    def assign_engineer(self, name):
        self.engineer = name
        print(f"Engineer '{name}' has been assigned to {self.name}")


# Child class 1
class OffshoreWell(Well):
    def __init__(self, name, pressure, temp, water_depth, platform_type, active=True, engineer=None):
        super().__init__(name, pressure, temp, active, engineer)  # inherit parent __init__
        self.water_depth   = water_depth
        self.platform_type = platform_type

    def describe(self):
        print(f"[OFFSHORE] Well: {self.name} | Pressure: {self._pressure} psi | Status: {self.status} | "
              f"Depth: {self.water_depth}m | Platform: {self.platform_type} | Engineer: {self.engineer}")

    def depth_rating(self):
        if self.water_depth > 1500:
            return "Ultra Deep"
        elif self.water_depth > 500:
            return "Deep"
        else:
            return "Shallow"


# Child class 2
class OnshoreWell(Well):
    def __init__(self, name, pressure, temp, region, site_manager, active=True, engineer=None):
        super().__init__(name, pressure, temp, active, engineer)  # inherit parent __init__
        self.region       = region
        self.site_manager = site_manager

    def describe(self):
        print(f"[ONSHORE]  Well: {self.name} | Pressure: {self._pressure} psi | Status: {self.status} | "
              f"Region: {self.region} | Site Manager: {self.site_manager}")

    def is_remote(self):
        return "Delta" in self.region or "Basin" in self.region


# Creating objects
off1 = OffshoreWell("Bonga-01",    pressure=3200, temp=85.0,  water_depth=1800, platform_type="FPSO")
off2 = OffshoreWell("Erha-02",     pressure=800,  temp=90.0,  water_depth=400,  platform_type="Fixed Jacket")
ons1 = OnshoreWell("Forcados-03",  pressure=1500, temp=75.0,  region="Niger Delta",   site_manager="Emeka Eze")
ons2 = OnshoreWell("Agbami-05",    pressure=5200, temp=310.0, region="Benue Plateau",  site_manager="Aisha Musa")

print("=" * 60)
print("WELL DESCRIPTIONS")
print("=" * 60)
off1.describe()
off2.describe()
ons1.describe()
ons2.describe()

print("\n" + "=" * 60)
print("IS CRITICAL (inherited from Well)")
print("=" * 60)
print(f"{off1.name} critical: {off1.is_critical()}")
print(f"{off2.name} critical: {off2.is_critical()}")
print(f"{ons1.name} critical: {ons1.is_critical()}")
print(f"{ons2.name} critical: {ons2.is_critical()}")

print("\n" + "=" * 60)

#Task 8 Polymorphism

# Validator
def validate_well_id(well_id):
    pattern = r'^[A-Za-z]{1,10}-\d{2}$'
    return bool(re.match(pattern, well_id))

# Parent Class
class Well:
    well_count = 0

    def __init__(self, name, pressure, temp, active=True, engineer=None):
        self.name      = name
        self._pressure = pressure
        self.temp      = temp
        self.active    = active
        self.engineer  = engineer
        Well.well_count += 1

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        if value < 0:
            raise ValueError("Pressure cannot be negative")
        self._pressure = value

    @property
    def status(self):
        if self._pressure < 1000:   return "CRITICAL"
        elif self._pressure < 2500: return "LOW"
        elif self._pressure < 4500: return "NORMAL"
        else:                       return "OVERPRESSURE"

    @classmethod
    def get_well_count(cls):
        return cls.well_count

    def describe(self):
        print(f"[WELL]     Well: {self.name} | Pressure: {self._pressure} psi | "
              f"Status: {self.status} | Engineer: {self.engineer}")

    def is_critical(self):
        return self._pressure < 1000 or self.temp > 300


#  Child Class 1
class OffshoreWell(Well):
    def __init__(self, name, pressure, temp, water_depth, platform_type, active=True, engineer=None):
        super().__init__(name, pressure, temp, active, engineer)
        self.water_depth   = water_depth
        self.platform_type = platform_type

    def describe(self):
        print(f"[OFFSHORE] Well: {self.name} | Pressure: {self._pressure} psi | "
              f"Status: {self.status} | Depth: {self.water_depth}m | Platform: {self.platform_type}")

    def depth_rating(self):
        if self.water_depth > 1500: return "Ultra Deep"
        elif self.water_depth > 500: return "Deep"
        else: return "Shallow"


#  Child Class 2
class OnshoreWell(Well):
    def __init__(self, name, pressure, temp, region, site_manager, active=True, engineer=None):
        super().__init__(name, pressure, temp, active, engineer)
        self.region       = region
        self.site_manager = site_manager

    def describe(self):
        print(f"[ONSHORE]  Well: {self.name} | Pressure: {self._pressure} psi | "
              f"Status: {self.status} | Region: {self.region} | Manager: {self.site_manager}")

    def is_remote(self):
        return "Delta" in self.region or "Basin" in self.region


# Child Class 3 — SubseaWell inherits from OffshoreWell
class SubseaWell(OffshoreWell):
    def __init__(self, name, pressure, temp, water_depth, platform_type, umbilical_length, active=True, engineer=None):
        super().__init__(name, pressure, temp, water_depth, platform_type, active, engineer)
        self.umbilical_length = umbilical_length  # extra attribute

    def describe(self):
        print(f"[SUBSEA]   Well: {self.name} | Pressure: {self._pressure} psi | "
              f"Status: {self.status} | Depth: {self.water_depth}m | Umbilical: {self.umbilical_length}m")


#  run_inspection function
def run_inspection(wells):
    print("=" * 65)
    print("RUNNING INSPECTION")
    print("=" * 65)
    for well in wells:
        well.describe()                        # polymorphism — each calls its own describe()
        if well.is_critical():
            print(f"  ⚠️  WARNING: {well.name} is CRITICAL!")
        if isinstance(well, OffshoreWell):     # True for Offshore AND Subsea
            print(f"  Depth Rating: {well.depth_rating()}")
        print()


#  Wells list
wells = [
    OffshoreWell("Bonga-01",   pressure=3200, temp=85.0,  water_depth=1800, platform_type="FPSO"),
    OffshoreWell("Erha-02",    pressure=800,  temp=90.0,  water_depth=400,  platform_type="Fixed Jacket"),
    OnshoreWell("Forcados-03", pressure=1500, temp=75.0,  region="Niger Delta",   site_manager="Emeka Eze"),
    OnshoreWell("Agbami-05",   pressure=5200, temp=310.0, region="Benue Plateau", site_manager="Aisha Musa"),
    Well("Testwell-01",        pressure=950,  temp=60.0),
]

print("── FIRST RUN (5 wells) ──\n")
run_inspection(wells)

# ── Add SubseaWell and run again — run_inspection() unchanged ─
wells.append(
    SubseaWell("Perdido-01", pressure=4800, temp=95.0,
               water_depth=2400, platform_type="Subsea Tree", umbilical_length=3200)
)

print("\n── SECOND RUN (SubseaWell added) ──\n")
run_inspection(wells)

print(f"Total wells created: {Well.get_well_count()}")


#Tasks 9

# task 9
#Creates a list of four well objects using three different classes
task9_wells = [
    OffshoreWell("Bonga-01", 3850, 185, 1200, "FPSO"),
    OnshoreWell("Delta-01", 820, 165, "Niger Delta", "Tunde Adeyemi"),
    SubseaWell("Subsea-01", 3500, 185, 1600, "FPSO", 2500),
    OnshoreWell("Basin-02", 2100, 175, "Benin Basin", "Ngozi Okafor"),
]

# convert well objects to dictionaries
#Starts with an empty list, then loops through each well object.
# For each one, it pulls out four attributes
wells_as_dicts = []
for well in task9_wells:
    wells_as_dicts.append({
        "name": well.name,
        "pressure": well.pressure,
        "temp": well.temp,
        "status": well.status
    })

# write to json file
with open("inspection_report.json", "w") as file:
    json.dump(wells_as_dicts, file, indent=2) #serialize list of dict
print("File written successfully.")

# validate IDs
for well in task9_wells:
    if validate_well_id(well.name):
        print(well.name, "— valid ID")
    else:
        print(well.name, "— INVALID ID")

# read back from file
with open("inspection_report.json", "r") as file:
    loaded_data = json.load(file)

# print formatted output
print()
for w in loaded_data:
    print(f"Well: {w['name']:<12} | Pressure: {w['pressure']:>8} psi | Status: {w['status']}")

# run final inspection
print("final_inspection")
run_inspection(task9_wells)