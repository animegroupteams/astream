# run this to get the new anime.json
# Google Collab is your best choice when running
# running this code .
# when you are done running this code in Google Collab create a 
# new cell and execute this code 

# from google.colab import files
# files.download('anime.json')
# the end num can be changed to whatever number 
#  you want to use 

import requests
import json

url_template = "https://animetize-api-orcin.vercel.app/anime-list?page={}"
start_num = 1
end_num = 91
animelist = []

for num in range(start_num, end_num + 1):
    url = url_template.format(num)
    print("Getting data for page", num)
    response = requests.get(url)
    data = response.json()
    
    # Check if the 'results' key exists in the response data
    if 'results' in data:
        for item in data['results']:
            # Map the new structure to the desired format
            anime_entry = {
                "name": item.get("title"),
                "url": item.get("id")
            }
            animelist.append(anime_entry)
    else:
        print(f"No 'results' key in the response for page {num}")

filename = 'anime.json'
with open(filename, 'w') as f:
    json.dump(animelist, f, indent=2)  # Added indent for better readability

with open(filename, 'r') as f:
    count = json.load(f)

num_objects = len(count)

print("Done! Saved as", filename)
print("Total Anime:", num_objects)
