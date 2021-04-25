import os
import json
import nltk
import html
import json2html
from certs import certs
import re, string
from nltk import ngrams
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

# read from file
def loadfile(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

# write to file
def writeFile(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file)

# preprocess the job description
def preprocessJobDescription(desc):
    desc = re.sub("[^\w\s]", "", desc)
    desc.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(desc) 
    filtered_desc = [w for w in word_tokens if not w in stop_words]
    desc = ' '.join(filtered_desc)
    return desc

# insensitive replace
def insensitive_replace(data, words, replacement):
    insenstive_data = re.compile(words, re.IGNORECASE)
    data = insenstive_data.sub(replacement, data)
    return data

# load nltk packages if not yet done so
nltk.download('stopwords')
nltk.download('punkt')

# location of the data files
data_folder = os.getcwd() + os.sep + "data" + os.sep
data_results_folder = os.getcwd() + os.sep + "data_results" + os.sep

# initialize the variables
job_with_cert = []
total_cert_jobs = 0
num_of_grams = 6

# This var further removes all jobs with no 
filename_combined_all_hascert_nodup = data_folder + "data_combined_all_hascert_nodup.json"
data_combined_all_hascert_nodup = loadfile(filename_combined_all_hascert_nodup)
# data_combined_all_hascert_nodup = loadfile(data_folder + "data_test.json")
print("Size of data_combined_all_hascert_nodup : " + str(len(data_combined_all_hascert_nodup)))


# cleaning the job description data, remove stopwords and punctuation
for job in data_combined_all_hascert_nodup:
    desc = job['description'].lower()
    job['description_filtered'] = preprocessJobDescription(desc)

# for each cert, look up all the jobs.
for x in certs:
    count_jobs = 0
    desc_jobs = []
    for job in data_combined_all_hascert_nodup:
        matches = certs[x]["match"]
        desc = job['description_filtered']
        found = False

        # first look for direct exact match
        for match in matches:
            if match.lower() in desc:
                count_jobs = count_jobs + 1
                desc_jobs.append(job)
                if job not in job_with_cert:
                    job_with_cert.append(job)
                found = True
                break

        # if match, do nothing        
        # if not match, look for fuzzy match
        # within 8 grams, if there is the set of include words and not the set of exclude
        fuzzyDict = certs[x]["fuzzy"]["includeExclude"]
        if not found and len(fuzzyDict) > 0 :
            for fuzzy in fuzzyDict:
                xgrams = ngrams(desc.split(), num_of_grams)
                for grams in xgrams:
                    # print((fuzzy[0]))
                    if fuzzy[0].issubset(set(grams)) and (len(fuzzy[1]) == 0 or not fuzzy[1].issubset(set(grams))) :
                        count_jobs = count_jobs + 1
                        desc_jobs.append(job)
                        if job not in job_with_cert:
                            job_with_cert.append(job)
                        found = True
                        break
                if found: 
                    break    
    # add up all the jobs with the possibility of this cert
    # note that 1 job can match to more than 1 certs. 
    # Count is 1 if cert exact or fuzzy match job, even though the cert can be found many times.
    certs[x]["count"] = count_jobs
    certs[x]["desc_jobs"] = desc_jobs

    # sum up all the jobs found
    total_cert_jobs = total_cert_jobs + count_jobs

# If you want to know which jobs are not match at all, uncomment the following
# for job in data_combined_all_hascert_nodup:
#     if job not in job_with_cert:
#         print(job['description'] + job['job_id'])

# Summary print out
print("total jobs retrieved from Google Job Enginer : " + str(len(data_combined_all_hascert_nodup)))
print("total jobs with at least one cert found : " + str(len(job_with_cert)))
print("total certs mentioned in all jobs : " + str(total_cert_jobs))
print("total certs analysed : " + str(len(certs)))

# if you want to sort by count for printing, uncomment the following
for x in sorted(certs.items(), key=lambda k_v:k_v[1]['count'], reverse=True):
    print(str(x[0]) + " " + str(x[1]['count']))

# print out jobs per certs
# print out to html all the jobs per certs.
for x in certs:
    print("No of jobs mention (" + x +") - " + str(certs[x]["count"]))

    for job in certs[x]["desc_jobs"]:
        desc = job['description'].lower()
        desc = preprocessJobDescription(desc)
        matches = certs[x]["match"]
        for match in matches:
            desc = insensitive_replace(desc, match.lower(), '<span style="background-color:yellow;">' + match + '</span>')
        found = False
        fuzzyDict = certs[x]["fuzzy"]["includeExclude"]
        if not found and len(fuzzyDict) > 0 :
            for fuzzy in fuzzyDict:
                xgrams = ngrams(desc.split(), 8)
                for grams in xgrams:
                    if fuzzy[0].issubset(set(grams)) and (len(fuzzy[1]) == 0 or not fuzzy[1].issubset(set(grams))) :
                        desc = insensitive_replace(desc, " ".join(grams), '<span style="background-color:yellow;">' + " ".join(grams) + '</span>')            
                        found = True
                        break
                if found: 
                    break          
        job["description"] = job["description"].replace("\n", "<br>")
        job["description"] = job["description"].replace("\u2022", "*")
        job["description_filtered"] = desc
        job.pop("extensions", None)
        job.pop("location", None)
        job.pop("detected_extensions", None)
        job.pop("job_id", None)
    
    job_html = json2html.json2html.convert(certs[x]["desc_jobs"])
    job_html = job_html.replace("&gt;", ">")
    job_html = job_html.replace("&lt;", "<")
    job_html = job_html.replace("&quot;", "'")
    writeFile(job_html, data_results_folder + "data_results(" + x + ").html")
    writeFile(json.dumps(certs[x]["desc_jobs"], indent=4), data_results_folder + "data_results(" + x + ").json")

