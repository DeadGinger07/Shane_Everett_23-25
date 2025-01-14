import sys




def total_weight():
    total_weight = 90
for year in range(1, 20):
    total_weight = 90 * 0.25 
    print('Year %s = %s' % (year, total_weight))


def moon_weight(earth, increase, year):
    return earth + increase + year
earth = input('Please enter your current Earth weight ')
increase = input('Please enter the amount that your weight might increase each year ')
year = input('Please enter the number of years ')
print(moon_weight(earth, increase, year))
sys.stdin.readline()
