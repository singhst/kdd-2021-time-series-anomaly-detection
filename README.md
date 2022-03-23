# kdd-2021-time-series-anomaly-detection

https://www.kdd.org/kdd2021/

# Result

<img src="kdd-cup-2021-time-series/results/old 20211130 2300/anomaly-001_UCR_Anomaly_35000-212windowsize-211autoperiod__[(51743, 52054), (69140, 69369)].png"/>

<img src="kdd-cup-2021-time-series/results/old 20211130 2300/anomaly-054_UCR_Anomaly_2700-60windowsize-59autoperiod__[(2878, 2888), (3111, 3140), (5681, 5701), (5802, 5899), (5930, 5962), (6048, 6054), (6304, 6312)].png" />

# Files

The data should be downloaded and unzipped in path `../data-sets/KDD-Cup/data/` from the `.ipynb` and `loadData.py`

## Usage 

`loadData.py`: Load all `.csv` under `../data-sets/KDD-Cup/data/` into memory. Help facilitate loading data.

# Setup
1. Initialize the VirtualEnv:
	```
	$ virtualenv venv
	```
2. Activate your VirtualEnv (linux)
	```
	$ source venv/bin/activate
	```
	OR	
	```
	$ . venv/bin/activate
	```
	 Activate your VirtualEnv (windows)
	```
	$ venv\Scripts\activate.bat
	```
3. pip Install packages from “requirements.txt”
	```
	(venv) $ pip install -r requirements.txt
	```

