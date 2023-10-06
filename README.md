# test_just_eat


The script get restaurants by postcode in the UK using the Just Eat API. 
It works by first prompting the user to enter a UK postcode. 
If the user enters a valid postcode, the script then makes a GET request to the Just Eat API to get the restaurants for that postcode.

If the request is successful, the script then parses the JSON response and writes the restaurant data to a JSON file called restaurants.json.


```shell
git clone https://github.com/evgenijmartynuk07/test_just_eat.git
cd test_just_eat

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

run: python main.py
```