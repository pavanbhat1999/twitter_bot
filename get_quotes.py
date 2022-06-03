from random import randint
import requests;

#generate a random number between 1 to 100
def get_random_number():
    random = randint(1,100);
    return random;

#get the quote from the API
def get_quotes():
    print("Getting quotes...");
    request_url = "https://programming-quotes-api.herokuapp.com/Quotes?count=0"
    response = requests.get(request_url);
    response_json = response.json();
    id = get_random_number();
    #print(response_json[id]["en"]);
    #print("--",response_json[id]["author"]);
    return response_json[id]["en"];