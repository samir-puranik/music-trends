# DSS Music Trends
This project will be assessing how song trends have changed in specific genres over time. It will use the following components:

 - Spotify APIs (https://developer.spotify.com/documentation/web-api/reference/)
	 - We will mainly interact with Spotify only to receive access tokens and credentials which will be put into .gitignore. We will use SpotiPy to use interact with the actual Spotify APIs in Python
 - Spotipy (https://spotipy.readthedocs.io/en/latest/)
	 - Wrapper for Spotify APIs
 - Billboard API (https://github.com/guoguo12/billboard-charts)
	 - We will use this API to gather the song titles/artists that we will analyze and separate them by genre

## Refreshing the Access Token for Spotify APIs
If errors show that the Spotify credentials are not working, try refreshing the access token for the Spotify APIs.
Use the following video if you need additional help with this: https://www.youtube.com/watch?v=m3YpkqhHKdk

 1. cd into the web-api-auth-examples-master
 2. From here, cd into authorization_code
 3. Run the command: node app.js
 4. This will start up an authentication server on localhost.
 5. Use the browser to navigate the localhost port that it says: localhost:\<port\>
 6. Log in to Spotify using Facebook.
 7. Click on refresh access token.
 8. Remember to exit the server. You are finished!

 You can run spotipy-example.py in dss-files to make sure that the token was refreshed as well.
 
### Files that have been placed into .gitignore
credentials.py
