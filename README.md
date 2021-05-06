# JobSearchCertifications

This project searches Google Job Search engine for mentions of IT certifications in the job postings.

## Folders
**data** 
- Contains the raw job postings retrieved from Google Job Search engine. 
- The current roles as specified in `certs.py` are [" software developer”, ”system analyst”, ”IT analyst”, ”software engineer”, ”solution  architect”,  ”project  manager”, ”product manager”, ”programmer”,  ”consultant”,  ”data  analyst”  and  ”data  scientist”].

**data_results** 
- Contains the processed computed results in json and html files.

## Scripts
**search_job_certs.py** 
- Review the results and write out the results in terminal and files (data_results folder)

**load_jobs.py** 
- Load the job postings based on Google Job Search engine. 
- You need the API key from SerpApi. You can also skip this step and review the results by running search_job_certs.py.
- Currently, the script also commented out the code to remove job duplicates. This step takes long execution time due to the comparisons required. 

**certs.py**
- This script contains the list of IT certifications to be search for exact and fuzzy matches.
- The list is writtin in a JSON format.

## Execution
1. Install and activate virtualenv
2. cd to the installation of this GitHub folder
3. run the command `pip install -r requirements.txt`
4. run the command `python search_jobs_certs.py`

Below is a sample output
```[nltk_data] Downloading package stopwords to /Users/smu/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt to /Users/smu/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
Size of data_combined_all_hascert_nodup : 1368
total jobs retrieved from Google Job Enginer : 1368
total jobs with at least one cert found : 1022
total certs mentioned in all jobs : 2108
total certs analysed : 60
....
No of jobs mention (AWS Certified Solutions Architect) - 158
No of jobs mention (AWS Certified Cloud Practitioner) - 9
No of jobs mention (AWS Certified Developer) - 133
No of jobs mention (AWS Certified Data Analytics) - 10
No of jobs mention (AWS Certified Machine Learning) - 1
No of jobs mention (Microsoft Certified Azure Solutions Architect) - 89
No of jobs mention (Microsoft Certified Azure Data Engineer) - 31
No of jobs mention (Microsoft Certified Azure AI Engineer Associate) - 36
No of jobs mention (Microsoft Certified Azure Developer Associate) - 30
No of jobs mention (Microsoft Certified Solution Developer) - 82
No of jobs mention (Microsoft Certified Solution Expert) - 31
No of jobs mention (Microsoft Certified Professional Developer) - 13
No of jobs mention (Google Associate Cloud Engineer) - 8
No of jobs mention (Google Professional Cloud Architect) - 15
No of jobs mention (Google Professional Cloud Developer) - 7
No of jobs mention (Google Professional Data Engineer) - 9
No of jobs mention (The Open Group Architecture Framework) - 59
....
```


