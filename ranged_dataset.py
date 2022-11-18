import datetime
import pickle
import pandas
import tabula

# Builds time span loop
# Configure the start time to the earliest day you wish the dataset to begin, 
# The earliest record for daily population from the IPS website is: 2015-01-01
# Note that formats from earlier years are untested, the oldest date checked within this script was 2022-01-03 : YYYY-MM-DD
# As records are not made for weekends the script will display an error but continue onto the next date

start = datetime.datetime(2022, 1, 3) # start date for earliest dataset
end = datetime.datetime(2022, 1, 7) # end date for dataset
delta = datetime.timedelta(days=1)

pdf_path='https://www.irishprisons.ie/wp-content/uploads/documents_pdf/{date1:%d-%B-%Y}.pdf'

while start < end:
    date1 = start
    date2 = start + delta
    url = pdf_path.format(date1=date1, date2=date2)


# Save list and stop loop

    start = date2  

# Extract Table from PDF availible from url

    path = url

    try:
        dfs = tabula.read_pdf(path, pages='1', lattice=True, stream=True, pandas_options={'header':None})
        new_header = dfs[0].iloc[1]
        inmate_count = dfs[0].drop(labels=0, axis=0)
        inmate_count.columns = [new_header]
        inmate_count=inmate_count.dropna(how='all').reset_index(drop=True)
        inmate_count = inmate_count.drop(labels=[0], axis=0)
        inmate_count['date'] = date1
        inmate_count.to_csv("IPS_Daily_Inmates.csv", mode='a', header=False, index=False)
        print(inmate_count)
    except  Exception:
        pass

print("Finished Collecting Ranged Dataset")