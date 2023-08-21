import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = "data/death_valley_2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,hights,lows = [],[],[]

    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        try:
            hight = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            hights.append(hight)
            lows.append(low)

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(dates,hights,c="red",alpha = 0.5)
ax.plot(dates,lows, c = "blue",alpha = 0.5)
ax.fill_between(dates,hights,lows,facecolor = "yellow",alpha = 0.3)

plt.title("Daily hights temperatures, 2021 year\n Death valley, CA",fontsize = 24)
plt.xlabel("",fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temp (F)",fontsize = 16)
plt.tick_params(axis="both", which = "major", labelsize = 16)

plt.show()
