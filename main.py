
import requests
import os
BASE_URL = "https://search.mls2.de";

# URL for the Keycloak Login Server
LOGIN_SERVER_URL = "https://develop-login.mls2.de";
REALM = "nws"; # One Server can have multiple Realms

# The ID of the Keycloak-Client we are using and its key
CLIENT_ID = "mls2-search";
CLIENT_SECRET = os.getenv('CLIENT_SECRET'); # replace with actual keycloak client secret

# User Data for our user with the SEARCH-ROLE
USERNAME = "SEARCH";
PASSWORD = os.environ.get('SEARCH_USER_PASSWORD')

LOGIN_PAYLOAD = {
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "username": USERNAME,
  "password": PASSWORD,
  "grant_type": "password",
};

def main():
  login_response = requests.post(LOGIN_SERVER_URL + "/realms/" + REALM + "/protocol/openid-connect/token",
    data = LOGIN_PAYLOAD,
    headers =  {
      "Content-Type": "application/x-www-form-urlencoded",
    }
  )
  print(login_response)
  access_token = login_response.json()["access_token"]

  tasks_response = requests.get(BASE_URL + "/mls-api/tasks.jsonld",
      headers =  {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
      }
    )

  page_index = 1

  while "hydra:next" in tasks_response.json()["hydra:view"]:

    print("=== Page: " + str(page_index) + " === \n")

    tasks_response = requests.get(BASE_URL + "/mls-api/tasks.jsonld?pagination=true&page=" + str(page_index),
      headers =  {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
      }
    )

    for task in tasks_response.json()["hydra:member"]:
      print(task["title"])

      task_steps_response = requests.get(BASE_URL + "/mls-api/task-steps?task=" + task["@id"],
        headers =  {
          "Authorization": "Bearer " + access_token,
          "Content-Type": "application/json"
        }
      )

      for task_step in task_steps_response.json()["hydra:member"]:
        print("- " + task_step["title"] )
    
      print("")
    
    page_index += 1

if __name__ == "__main__":
  main();