# Address-Location-Rest-API

STEP 1: After running virtual enviroonment in terminal than install requirements, change directory to \Address-Location-Rest-API .

STEP 2: Add .env file in \Address-Location-Rest-API\address_api directory and add google API key in formate:

        API_KEY=yourKey

STEP 3: For run project use command in \Address-Location-Rest-API direcctory:

        python manage.py runserver
        
# API uses

### Url: http://127.0.0.1:8000/address

### Body: {"address": "your addresss", "output_format": "xml or json only"
    
        address format: 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008
          
# Run test cases

### In same \Address-Location-Rest-API directory run command:

        python manage.py test
          
         
