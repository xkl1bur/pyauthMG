from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  '''
  The get_user method makes a GET request to the Microsoft Graph /me endpoint to get the user's profile, 
  using the access token you acquired previously.

  @Return {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
      "businessPhones": [
          "+1 412 555 0109"
      ],
      "displayName": "Megan Bowen",
      "givenName": "Megan",
      "jobTitle": "Auditor",
      "mail": "MeganB@M365x214355.onmicrosoft.com",
      "mobilePhone": null,
      "officeLocation": "12/1110",
      "preferredLanguage": "en-US",
      "surname": "Bowen",
      "userPrincipalName": "MeganB@M365x214355.onmicrosoft.com",
      "id": "48d31887-5fad-4d73-a9f5-3c356e68a038"
  }
  '''

  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get(f'{graph_url}/me')
  # Return the JSON result
  return user.json()