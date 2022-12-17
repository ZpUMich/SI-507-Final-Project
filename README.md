# SI-507-Final-Project
In order to run the code without the JSON files, the following packages are needed:

  import requests
  
  import json 

  import webbrowser
  
  from twarc import Twarc2, expansions
  
  import datetime
  
Program interaction: The command prompt will ask the user for interests they want to want to find a recommendation for. At each prompt you will be asked if you want to search a phrase or word. Then the code will search the tweet level of the tree for phrases, and the word level of the tree for words. It will keep track of the occurrences for each park, of each interest, until the user resets their search. After providing an interest, the code gives the user the new top 5 recommendations, and links to the parks’ websites. The recommendation is based on which parks are the most occurrences of all interests in their tree.
  
Data and Datastructure:

For API keys, you can use your own, or they are provided in the Canvas PDF submission.

the 'NPSAll' data file is all of the data on each of the 468 United States parks, that are a part of the National Parks System, API.

Each Park will have its own tree, with the tweets being branches, and the words being leaves.
The first level of park to tweet, is created when the twitter data is read offline. Then the tweets are passed over creating their word leaves.
