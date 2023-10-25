import datetime

MercuryYr = 88
VenusYr = 225
EarthYr = 365
MarsYr = 687
JupiterYr = 4333
SaturnYr = 10759
UranusYr = 30687
NeptuneYr = 60190

MercuryDay = 1408
VenusDay = 5832
EarthDay = 24
MarsDay = 25
JupiterDay = 10
SaturnDay = 11
UranusDay = 17
NeptuneDay = 16

planetAbbrv = ['m', 'v', 'm', 'ma', 'j', 's', 'u', 'n']


def Input():
    global PlanetInp
    global ageInp
    PlanetInp = input("Please enter the first letter of the planet in case of it being Mars please enter Ma (case insensitive):")
    PlanetInp = PlanetInp.lower()

    for pos, abbrv in enumerate(planetAbbrv):
        check = False
        if (PlanetInp == abbrv):
            check = True
            break
    if (check == False):
        print("Please enter a valid input!")
        Input()

    ageInp = input("Please enter your birthdate in this format MM.DD.YYYY : ")
    Month = int(ageInp[0:2])
    Day = int(ageInp[3:5])
    if (Month > 12 or Day > 31 or Month < 1 or Day < 1):
        print("Please enter a valid input!")
        Input()

Input()

MonthInp = int(ageInp[0:2])
DayInp = int(ageInp[3:5])
YearInp = int(ageInp[6:])

today = datetime.date.today()
birthday = datetime.date(month = MonthInp, day = DayInp, year=YearInp)
diff = birthday - today
negDays= diff.days
EDaysAlv= -negDays

EHoursAlv = EDaysAlv * EarthDay


def findAge(EHours, Planet):
    match Planet:
        case 'm':
            days = EHours // MercuryDay
            years = days // MercuryYr
            inDays = days % MercuryYr
            print(f"You would be {years} years old, and {inDays} days old on Mercury, in Mercury days.")
        case 'v':
            days = EHours // VenusDay
            years = days // VenusYr
            inDays = days % VenusYr
            print(f"You would be {years} years old, and {inDays} days old on Venus, in Venus days.")
        case 'e':
            days = EHours // EarthDay
            years = days // EarthYr
            inDays = days % EarthYr
            print(f"You would be {years} years old, and {inDays} days old on Earth, in Earth days.")
        case 'ma':
            days = EHours // MarsDay
            years = days // MarsYr
            inDays = days % MarsYr
            print(f"You would be {years} years old, and {inDays} days old on Mars, in Mars days.")
        case 'j':
            days = EHours // JupiterDay
            years = days // JupiterYr
            inDays = days % JupiterYr
            print(f"You would be {years} years old, and {inDays} days old on Jupiter, in Jupiter days.")
        case 's':
            days = EHours // SaturnDay
            years = days // SaturnYr
            inDays = days % SaturnYr
            print(f"You would be {years} years old, and {inDays} days old on Saturn, in Saturn days.")
        case 'u':
            days = EHours // UranusDay
            years = days // UranusYr
            inDays = days % UranusYr
            print(f"You would be {years} years old, and {inDays} days old on Uranus, in Uranus days.")
        case 'n':
            days = EHours // NeptuneDay
            years = days // NeptuneYr
            inDays = days % NeptuneYr
            print(f"You would be {years} years old, and {inDays} days old on Neptune, in Neptune days.")

findAge(EHoursAlv, PlanetInp)


