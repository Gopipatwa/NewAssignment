python -m venv myvenv

cd myvenv\Scripts\activate  --Enter

- pip install -r requirements.txt --Enter
- python manage.py runserver


Excel Data Must have column name  *Address*

After click on submit button now it will generate new excel file with latitude and logitude with name *response.xlsx*

module use in this app
- Django  -- For Creating application
- geopy  -- For getting address latitude and logitude
- pandas -- Manupulation Excel data to add new two columns
- openpyxl -- For read Excel file


