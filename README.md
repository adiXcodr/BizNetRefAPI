# REFERRAL API

## Technologies Used
* Python
* MongoDB
* Flask

## Github Steps:
* Fork the repository to your Github account
* Copy the link (ends with a .git) of your forked repository
* In a folder of your choice in your local machine, run git clone thelinkyoujustcopied.git
* ```cd referralAPI```

## Steps to run the API:
* ```cd referralAPI```
* Create a virtual environment ```py -3 -m venv venv```
* Activate virtual environment ```venv\Scripts\activate``` (for Windows) and ```venv\bin\activate``` (for Mac)
* ```pip install -r requirements.txt```(only for the first time after clonning)

## Testing the API:
* Locally
* Test the API with POSTMAN

Example for POST request :
* Set the URL to ```http://localhost:3434/run_model/add_user``` to add a user.<br><br>

    Sample JSON Data to contact route:
    ```json
   {
    "ref_username":"debo_leen",
    "username":"jdoe123",
    "name":"John Doe",
    "dob":"01/01/2000"
   }
    ```
    <br>

