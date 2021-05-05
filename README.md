# VaccineChecker-India
This is an automated Vaccine availability tracker that sends continuous messages at some predefined interval written in Python. 

## Background
This script will be helpful for the people who are unable to regularly check up for their vaccination slots. It is written in Python and uses some of the APIs provided by the COWIN and Telegram Messenger. Please do refer to the entire set of APIs here - [COWIN](https://apisetu.gov.in/public/api/cowin) & [Telegram](https://core.telegram.org/).

## Setup
1. Install Python (>3.5) in your system.
2. Run the following to install all the dependencies:
```
pip install -r requirements.txt
```
3. Please fill up the inputs as per your requirement (explained in the next section)

## Inputs
The inputs to the script is given at the beginning of the script and can be edited directly. The following are the details of the input parameters:
- "pin_codes" : Pin codes you would want to search for (Python list)
- "vaccine" : Vaccine name(s) you are looking for (Python list)
- "telegramToken" : Telegram HTTP API token for Bot (Python string). Please refer to this [YouTube video](https://www.youtube.com/watch?v=ps1yeWwd6iA) in order to fetch the values for your setup)
- "chat_id" : Telegram chat ID of the group (Python String). Refer to the above video for fetching this value.  
- "days" : No of days from today you want the data for (Python int)
- "sleep_time" : Message interval in seconds (Python int)
- "age" : Age bracket you are looking for (Python int). The script will display data for ages < age

### Caveats/Caution
- This script uses an infinite loop in python. 
- Be careful when you change the sleep_time interval. Reducing it to a very small value may make the program malfunction or the COWIN/Telegram servers to reject your frequent API requests.
- This is a POC script. Please use at your own risk. Of course it can be improved which will be done in due time.
- Please excuse my coding standards.
