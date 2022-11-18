# Irish Prison Service - Daily Population Dataset Generator
 Not affiliated with the Irish Prison Service, created to generate a dataset of daily prison populations within Irish prisons from official published PDF records.

The following scripts are used to create a single database derived from the daily PDF outputs of population numbers made available by the Irish Prison Service (see: [Daily Prisoner Population - Irish Prison Service](https://www.irishprisons.ie/information-centre/statistics-information/2015-daily-prisoner-population/)).

The best means to use these scripts is to firstly create a base database using the ranged_dataset.py followed by setting up a scheduled task either using Crontab, Windows Task Scheduler, or Automator to run the script ideally at 8:30 pm from Monday to Friday.

## Requirements
[Python 3](https://www.python.org/downloads/)

[JAVA](https://www.java.com/en/)

## Python Packages

[pandas](https://pandas.pydata.org/)

[pickle](https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy.)

[tabula](https://pypi.org/project/tabula-py/)

