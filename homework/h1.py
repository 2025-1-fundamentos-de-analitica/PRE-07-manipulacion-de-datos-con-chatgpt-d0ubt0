import pandas as pd 
import matplotlib.pyplot as plt

drivers = pd.read_csv('files/input/drivers.csv')
timesheet = pd.read_csv('files/input/timesheet.csv')

timesheet_by_driver = timesheet.groupby('driverId')
mean_timesheet_by_driver = timesheet_by_driver[['hours-logged','miles-logged']].mean().reset_index()

df_merged = drivers.merge(mean_timesheet_by_driver)

#df_merged.to_csv('files/output/summary.csv', index= False)

df_merged = df_merged.sort_values('hours-logged', ascending= False)


plt.bar(df_merged['driverId'].head(10).astype(str), df_merged['hours-logged'].head(10))
plt.savefig('files/plots/top10_drivers.png', dpi=300, bbox_inches='tight')
plt.show()
