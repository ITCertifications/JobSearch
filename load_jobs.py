from serpapi import GoogleSearch
import json
import os
from difflib import SequenceMatcher

# load jobs from Google Jobs
def load(params):
    search = GoogleSearch(params)
    results = search.get_json()
    return results

# write to file
def writeFile(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file)

# read from file
def loadfile(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

# list of roles to search
roles = [ "software developer", "system analyst", "IT analyst", "software engineer", "solution architect", "project manager", "product manager", "programmer", "consultant", "data analyst", "data scientist"]

# parameters to send to serpapi
params = {
  "engine": "google_jobs",
  "google_domain": "google.com.sg",
  "q": "",
  "gl": "sg",
  "hl": "en",
  "location": "Singapore",
  "start": "0",
  "api_key": "<replace with your own key>"
}

# location of the data files
data_folder = os.getcwd() + os.sep + "data" + os.sep

# since serpapi only loads 10 at a time, the below code loop till 200

# update the api_key and uncomment the following codes to run
# for x in range (0, 10, 10):
    # for y in roles:
    #     params.update({"start":str(x)})
    #     params.update({"q":"("+y+") (certified | certification)"})
    #     filename = data_folder + "data(" + y + ")" + str(x) + ".json"
    #     writeFile(load(params), filename)

# This var combine all the job results into data_combined_all
data_combined_all = []

# This var further removes all jobs with no 
data_combined_all_hascert = []

# This var removes all the duplicates of jobs based on job_id
data_combined_all_hascert_nodup = []

filename_combined_all = data_folder + "data_combined_all.json"
filename_combined_all_hascert = data_folder + "data_combined_all_hascert.json"
filename_combined_all_hascert_nodup = data_folder + "data_combined_all_hascert_nodup.json"

# we first combine all job results of a role into a file and then all roles into data_combined_all
for y in roles:
    data_combined = []
    for x in range (0, 250, 10):
        filename = data_folder + "data(" + y + ")" + str(x) + ".json"
        data = loadfile(filename)
        if 'jobs_results' in data:
            data_combined = data_combined + data['jobs_results']
            data_combined_all = data_combined_all + data['jobs_results']
    filename_combined = data_folder + "data_combined(" + y + ").json"
    writeFile(data_combined, filename_combined)
    print("Size of " + filename_combined + " : " + str(len(data_combined)))

writeFile(data_combined_all,filename_combined_all)

data_combined_all = loadfile(filename_combined_all)
print("Size of data_combined_all : " + str(len(data_combined_all)))

# we check if each job has at least the words certified or certification and write into combined_all_hascert
for job in data_combined_all:
    if "certified" in job['description'].lower() or "certification" in job['description'].lower():
        data_combined_all_hascert.append(job)
writeFile(data_combined_all_hascert, filename_combined_all_hascert)

data_combined_all_hascert = loadfile(filename_combined_all_hascert)
print("Size of data_combined_all_hascert : " + str(len(data_combined_all_hascert)))

# comment out below if you wish to remove duplicates
data_combined_all_hascert_nodup = data_combined_all_hascert

# uncomment below to remove duplicates.
# we then remove duplicates of jobs and write into data_combined_all_hascert_nodup
# data_combined_all_hascert_nodup = []
# data_combined_all_hascert_nodup_temp = []
# for i in data_combined_all_hascert:
#     if i not in data_combined_all_hascert_nodup_temp:
#         data_combined_all_hascert_nodup_temp.append(i)
# print("Length of nodup temp: " + str(len(data_combined_all_hascert_nodup_temp)))        

# count = 0
# for i in data_combined_all_hascert_nodup_temp:
#     count = count + 1
#     print(count)
#     if len(data_combined_all_hascert_nodup) > 0:
#         first = i['description']
#         found = False
#         for x in data_combined_all_hascert_nodup:
#             second = x['description']
#             ratio = SequenceMatcher(None, first, second).ratio() 
#             if ratio > 0.95:
#                 found = True
#                 print("same **************" + str(ratio))
#                 break
#                 # print("first *************" + first)    
#                 # print("second *************" + second)    
#         if not found:
#                 data_combined_all_hascert_nodup.append(i)
#     else:
#         data_combined_all_hascert_nodup.append(i)

writeFile(data_combined_all_hascert_nodup, filename_combined_all_hascert_nodup)

data_combined_all_hascert_nodup = loadfile(filename_combined_all_hascert_nodup)
print("Size of data_combined_all_hascert_nodup : " + str(len(data_combined_all_hascert_nodup)))
