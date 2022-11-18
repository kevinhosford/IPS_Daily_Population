import datetime
import pickle
import pandas
import tabula as tb

# This is intended to be set as a daily scheduled download script.
# Preferably using a small linux based computer such as a Raspberry Pi,
# However, it can be run using any Python3 based runtime and required packages loaded. 

date1 = datetime.date.today()
pdf_path='https://www.irishprisons.ie/wp-content/uploads/documents_pdf/{date1:%d-%B-%Y}.pdf'
url = pdf_path.format(date1=date1)
print(url)

# Extract Table from PDF availible from url

path = url

# Make the most recent addition to the IPS_Daily_Inmates.csv, intended to be run each day,
# The below script should be designed to work through potential errors,
# But ideally the following Cronjob script should be used in Linux to satisfy scheduling.
# 30 20 * * 1-5 python3 /home/USER/IPS_Daily_Inmates/scheduled_update.py
# It's also recommended that you use Cronitor to monitor the job remotely


try:
        dfs = tb.read_pdf(path, pages='1', lattice=True, stream=True, pandas_options={'header':None})
        new_header = dfs[0].iloc[1]
        inmate_count = dfs[0].drop(labels=0, axis=0)
        inmate_count.columns = [new_header]
        inmate_count=inmate_count.dropna(how='all').reset_index(drop=True)
        inmate_count = inmate_count.drop(labels=[0], axis=0)

        inmate_count['date'] = pandasto_datetime('today').strftime("%d-%B-%Y")
        inmate_count.to_csv("IPS_Daily_Inmates.csv", mode='a', header=False, index=False)
        print(inmate_count)
except  Exception:
        pass

print("Finished")
