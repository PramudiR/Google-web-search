from serpapi import GoogleSearch
import os, json

my_secret = os.environ['secret_api_key']
params = {
    "api_key": my_secret,
    "engine": "google",
    "q": "sea",
    "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
# print(results["organic_results"][0])

web_results = []

for link in results["organic_results"]:
    web_results.append({"link": link["link"]})

# print(web_results)
# result = json.dumps(web_results, indent=2)

print(web_results[0]["link"])


