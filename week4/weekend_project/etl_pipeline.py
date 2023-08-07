'''
Disney API Project
'''




def disneywrangle(filepath):

    #import statements
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import requests, json
    import numpy as np
    from numpy import asarray
    from PIL import Image
    from io import BytesIO
    

    
    #url here for backup
    url = 'https://api.disneyapi.dev/character'

    #getting response from the api

    response = requests.get(filepath)
    response.json()

    #Assigning the targeted response to a variable
    infodict = response.json()['data']


    # Function for organizing the data into a new dictionary

    def infofilter(infodict):
        
            #Finding the data from the api
            name = [infodict[x]['name'] for x in range(len(infodict))]
            films = [infodict[x]['films'] for x in range(len(infodict))]
            short_films = [infodict[x]['shortFilms'] for x in range(len(infodict))]
            tv_shows = [infodict[x]['tvShows'] for x in range(len(infodict))]
            allies = [infodict[x]['allies'] for x in range(len(infodict))]
            enemies = [infodict[x]['enemies'] for x in range(len(infodict))]
            park_attractions = [infodict[x]['parkAttractions'] for x in range(len(infodict))]

            #Assigning the new dictionary

            character_data = {
                    'name': name,
                    'films': films,
                    'short_films':short_films,
                    'tv_shows':tv_shows,
                    'allies':allies,
                    'enemies':enemies,
                    'park_attractions':park_attractions

            }
            #Deleting the columns with no data
            del character_data['short_films']
            del character_data['allies']
            del character_data['enemies']

            return character_data


    filtered_character_list = infofilter(infodict)
    df = pd.DataFrame(data = filtered_character_list)

    #populating the images
    #I Tried. I really tried so hard :( 

#    def populate():
#        for x in range(len(infodict)):
#            image_str = infodict[x]['imageUrl']
#            imgresponse = requests.get(image_str)
#            image = Image.open(BytesIO(imgresponse.content))
#            new_image = image.resize((60,60))
#            numpydata = asarray(new_image)
#            df.insert(0,'pic',df.loc[x].append(numpydata))
#    populate()
                

    #function to search for specific character info

    def findcharacter():
        checker = filtered_character_list['name']
        search = input('Enter the character you want to retrieve info for').title()
        if search in checker:
            idnum = df[df['name'] == search].index
            return df.loc[idnum]
        else:
            return 'Character not found'
    #Enter 'findcharacter() and run to begin search

    #save file to csv
    df.to_csv('Disney_api_data.csv')

    #save file to SQL

    sql_url = "postgres://vaymjdmh:LWqqhDkKAWaIqjHg1lhfgwD7Sx3nMJca@batyr.db.elephantsql.com/vaymjdmh"
    df.to_sql('disney_data', sql_url)
    return df


disneywrangle('https://api.disneyapi.dev/character')
#findcharacter()