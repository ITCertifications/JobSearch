# Dictionary of certs and organizations
certs = {
        # Organizations
        #     'PMI Certified': {
        #         "count": 0,
        #         "match": ['PMI Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'pmi', 'certification'}, set()],
        #             [{'pmi', 'certified'}, set()],
        #             [{'pmp', 'certification'}, set()],
        #             [{'pmp', 'certified'}, set()],]
        #         }
        #     },
        #     'AWS Certified': {
        #         "count": 0,
        #         "match": ['AWS Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'aws', 'certification'}, set()],
        #             [{'aws', 'certified'}, set()]]
        #         }
        #     },
        #   'Microsoft Certified': {
        #         "count": 0,
        #         "match": ['Microsoft Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'microsoft', 'certification'}, set()],
        #             [{'microsoft', 'certified'}, set()]]
        #         }
        #   },
        #   'Google Certified': {
        #         "count": 0,
        #         "match": ['Google Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'google', 'certification'}, set()],
        #             [{'google', 'certified'}, set()]]
        #         }
        #   },
        #   'Cisco Certified': {
        #         "count": 0,
        #         "match": ['Cisco Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'cisco', 'certified'}, set()],
        #             [{'cisco', 'certification'}, set()]]
        #         }
        #   },
        #   'Salesforce Certified': {
        #         "count": 0,
        #         "match": ['Salesforce Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'salesforce', 'certification'}, set()],
        #             [{'salesforce', 'certifications'}, set()],
        #             [{'salesforce', 'certified'}, set()]]
        #         }
        #   },
        #   'Oracle Certified': {
        #         "count": 0,
        #         "match": ['Oracle Certified'],
        #         "fuzzy": {
        #             "includeExclude": [[{'oracle', 'certification'}, set()],
        #             [{'oracle', 'certifications'}, set()],
        #             [{'oracle', 'certified'}, set()]]
        #         }
        #   },
          
          # Specific Cloud, Design and Development Certs
          'AWS Certified Solutions Architect': {
                "count": 0,
                "match": ['AWS Certified Solutions Architect', 'AWS Solutions Architect', 'AWS Certified Solution Architect', 'Amazon Solutions Architect'],
                "fuzzy": {
                    "includeExclude": [[{'aws', 'certification'}, {'developer'}],
                    [{'aws', 'certified', 'architect'}, set()],
                    [{'aws', 'certified'}, {'developer'}],
                    [{'certified', 'solution', 'architect'}, {'developer', 'azure', 'google'}],
                    [{'certified', 'cloud'}, {'azure', 'google'}]]
                }
            },
          'AWS Certified Cloud Practitioner': {
                "count": 0,
                "match": ['AWS Certified Cloud Practitioner'],
                "fuzzy": {
                    "includeExclude": [[{'aws', 'practitioner', 'certification'}, set()],
                    [{'aws', 'certified', 'practitioner'}, set()]]
                }
            },
            'AWS Certified Developer': {
                "count": 0,
                "match": ['AWS Certified Developer', 'AWS Developer', 'Amazon Developer'],
                "fuzzy": {
                    "includeExclude": [[{'aws', 'certification'}, {'architect'}],
                    [{'aws', 'certified', 'developer'}, {'architect'}],
                    [{'aws', 'certified'}, {'architect'}]]
                }
            },
          'AWS Certified Data Analytics': {
                "count": 0,
                "match": ['AWS Certified Data Analytics', 'AWS Data Analytics', 'Amazon Data Analytics'],
                "fuzzy": {
                    "includeExclude": [[{'aws', 'data', 'certification'}, {'architect'}],
                    [{'aws', 'data', 'certified'}, {'architect'}]]
                }
            },
          'AWS Certified Machine Learning': {
                "count": 0,
                "match": ['AWS Certified Machine Learning', 'AWS Machine Learning'],
                "fuzzy": {
                    "includeExclude": [[{'aws', 'ML', 'certification'}, set()],
                    [{'aws', 'ML', 'certified'}, set()],
                    [{'aws', 'machine', 'certification'}, set()],
                    [{'aws', 'machine', 'certified'}, set()]]
                }
            },
          'Microsoft Certified Azure Solutions Architect': {
                "count": 0,
                "match": ['Microsoft Certified Azure Solutions Architect', 'Azure Solutions Architect'],
                "fuzzy": {
                    "includeExclude": [[{'azure', 'architect', 'certification'}, {'engineer', 'developer'}],
                    [{'azure', 'certified', 'architect'}, {'engineer', 'developer'}],
                    [{'certified', 'solution', 'architect'}, {'engineer', 'aws', 'google'}],
                    [{'azure', 'certified'}, {'engineer'}],
                    [{'certified', 'cloud'}, {'aws', 'google'}]]
                }
          },
          'Microsoft Certified Azure Data Engineer': {
                "count": 0,
                "match": ['Microsoft Certified Azure Data Engineer', 'Certified Azure Data Engineer'],
                "fuzzy": {
                    "includeExclude": [[{'azure', 'certification', 'data'}, {'architect', 'developer'}],
                    [{'azure', 'certified', 'data'}, {'architect'}],
                    [{'azure', 'certified'}, {'architect'}]]
                }
          },
          'Microsoft Certified Azure AI Engineer Associate': {
                "count": 0,
                "match": ['Microsoft Certified Azure AI Engineer Associate', 'Certified Azure AI Engineer'],
                "fuzzy": {
                    "includeExclude": [[{'azure', 'certification', 'AI'}, {'architect', 'developer'}],
                    [{'azure', 'certified', 'AI'}, {'architect'}],
                    [{'azure', 'certified'}, {'architect', 'data', 'developer'}]]
                }
          },
          'Microsoft Certified Azure Developer Associate': {
                "count": 0,
                "match": ['Microsoft Certified AzureDeveloper Associate', 'Certified Azure Developer'],
                "fuzzy": {
                    "includeExclude": [[{'azure', 'certification', 'developer'}, {'architect', 'engineer'}],
                    [{'azure', 'certified', 'developer'}, {'architect', 'engineer'}],
                    [{'azure', 'certified'}, {'architect'}]]
                }
          },
          'Microsoft Certified Solution Developer': {
                "count": 0,
                "match": ['Microsoft Certified Solution Developer', 'MCSD'],
                "fuzzy": {
                    "includeExclude": [[{'microsoft', 'certification'}, {'azure', 'expert'}],
                    [{'microsoft', 'certified'}, {'azure', 'expert'}]]
                }
          },
          'Microsoft Certified Solution Expert': {
                "count": 0,
                "match": ['Microsoft Certified Solution expert', 'MCSE'],
                "fuzzy": {
                    "includeExclude": [[{'microsoft', 'certification', 'expert'}, {'azure', 'developer'}],
                    [{'microsoft', 'certified', 'expert'}, {'azure', 'developer'}]]
                }
          },
          'Microsoft Certified Professional Developer': {
                "count": 0,
                "match": ['Microsoft Certified Professional Developer', 'MCPD'],
                "fuzzy": {
                    "includeExclude": [[{'microsoft', 'certification', 'developer'}, {'azure', 'solution'}],
                    [{'microsoft', 'certified', 'developer'}, {'azure', 'solution'}]]
                }
          },
          'Google Associate Cloud Engineer': {
                "count": 0,
                "match": ['Associate Cloud Engineer'],
                "fuzzy": {
                    "includeExclude": [[{'google', 'associate', 'certification'}, set()],
                    [{'google', 'associate', 'engineer'}, set()],
                    [{'gcp', 'certification'}, {'architect', 'engineer', 'developer'}],
                    [{'gcp', 'certified'}, {'architect', 'engineer', 'developer'}]] 
                }
          },
          'Google Professional Cloud Architect': {
                "count": 0,
                "match": ['Professional Cloud Architect'],
                "fuzzy": {
                    "includeExclude": [[{'google', 'architect', 'certification'}, set()],
                    [{'google', 'architect', 'certified'}, set()],
                    [{'gcp', 'certification'}, {'associate', 'engineer', 'developer'}],
                    [{'gcp', 'certified'}, {'associate', 'engineer', 'developer'}]]
                }
          },          
          'Google Professional Cloud Developer': {
                "count": 0,
                "match": ['Professional Cloud Developer'],
                "fuzzy": {
                    "includeExclude": [[{'google', 'developer', 'certification'}, set()],
                    [{'google', 'developer', 'certified'}, set()],
                    [{'gcp', 'certification'}, {'associate', 'engineer', 'architect'}],
                    [{'gcp', 'certified'}, {'associate', 'engineer', 'architect'}]]
                }
          },
          'Google Professional Data Engineer': {
                "count": 0,
                "match": ['Professional Data Engineer'],
                "fuzzy": {
                    "includeExclude": [[{'google', 'data', 'certification'}, set()],
                    [{'google', 'data', 'certified'}, set()],
                    [{'gcp', 'certification'}, {'associate', 'developer', 'architect'}],
                    [{'gcp', 'certified'}, {'associate', 'developer', 'architect'}]]
                }
          },
          'The Open Group Architecture Framework': {
                "count": 0,
                "match": ['The Open Group Architecture Framework', 'TOGAF'],
                "fuzzy": {
                    "includeExclude": [[{'enterprise', 'architecture', 'certification'}, set()],
                    [{'enterprise', 'architect', 'certified'}, set()]]
                }
          },
          'Salesforce Certified Administrator': {
                "count": 0,
                "match": ['Salesforce Certified Administrator'],
                "fuzzy": {
                    "includeExclude": [[{'salesforce', 'administrator', 'certification'}, set()],
                    [{'salesforce', 'administrator', 'certifications'}, set()],
                    [{'salesforce', 'administrator', 'certified'}, set()]]
                }
          },
          'Salesforce Certified Platform Developer and App Builder': {
                "count": 0,
                "match": ['Salesforce Certified Platform App', 'Salesforce Certified Platform Developer'],
                "fuzzy": {
                    "includeExclude": [[{'salesforce', 'platform', 'certification'}, set()],
                    [{'salesforce', 'platform', 'certifications'}, set()],
                    [{'salesforce', 'platform', 'certified'}, set()]]
                }
          },
          'Oracle Certified Professional': {
                "count": 0,
                "match": ['Oracle Certified Professional', 'OCP'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'oracle', 'professional'}, set()],
                    [{'certification', 'oracle', 'professional'}, set()]]
                }
          },
          'Oracle Certified Java Programmer': {
                "count": 0,
                "match": ['Certified Java Programmer'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'java', 'programmer'}, set()],
                    [{'certification', 'java', 'programmer'}, set()]]
                }
          },
          'Oracle Certified Java Developer': {
                "count": 0,
                "match": ['Certified Java Developer'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'java', 'developer'}, set()],
                    [{'certification', 'java', 'developer'}, set()],
                    [{'certified', 'j2ee'}, set()],
                    [{'certification', 'javaee'}, set()]]
                }
          },
          'Oracle Certified Java Architect': {
                "count": 0,
                "match": ['Certified Java Developer'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'java', 'architect'}, set()],
                    [{'certification', 'java', 'architect'}, set()]]
                }
          },
          'Certified Agile Developer': {
                "count": 0,
                "match": ['Certified Agile Developer'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'agile', 'developer'}, set()],
                    [{'certification', 'agile', 'developer'}, set()],
                    [{'certified', 'agile'}, set()],
                    [{'certification', 'agile'}, set()]]
                }
          },

          # Project Management and Business Analysis
          'Project Management Professional': {
                "count": 0,
                "match": ['Project Management Professional', 'PMP'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'project', 'management'}, set()],
                    [{'certified', 'project', 'manager'}, set()],
                    [{'certification', 'project', 'management'}, set()],
                    [{'certification', 'project', 'manager'}, set()]]
                }
          },
          'Certified IT Project Management': {
                "count": 0,
                "match": ['Certified IT Project Management', 'CITPM'],
                "fuzzy": {
                    "includeExclude": []
                }
          },
          'Certified Business Analysis Professional': {
                "count": 0,
                "match": ['Certified Business Analysis Professional', 'CBAP'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'business', 'analysis'}, set()],
                    [{'certified', 'business', 'analyst'}, set()],
                    [{'certification', 'business', 'analysis'}, set()],
                    [{'certification', 'business', 'analyst'}, set()], ]
                }
          },

        # Process Related Certifications
          'IT Infrastructure Library ITIL': {
                "count": 0,
                "match": ['IT Infrastructure Library', 'ITIL'],
                "fuzzy": {
                    "includeExclude": []
                }
          },
          'ISO CMMI Certified': {
                "count": 0,
                "match": ['ISO CMMI Certified'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'iso'}, set()],
                    [{'certification', 'iso'}, set()],
                    [{'certified', 'cmmi'}, set()],
                    [{'certification', 'cmmi'}, set()]]
                }
          },          
          'Certified Scrum Master': {
                "count": 0,
                "match": ['Certified Scrum Master'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'scrum'}, set()],
                    [{'certified', 'scrummaster'}, set()],
                    [{'certification', 'scrum'}, set()],
                    [{'certification', 'scrummaster'}, set()]]
                }
          },          
          'Certified Agile Product Owner': {
                "count": 0,
                "match": ['Certified Agile Product Owner', 'CSPO'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'product'}, set()],
                    [{'certification', 'product'}, set()]]
                }
          },  

        # Security Related Certifications
          'Certified Information Systems Security Professional': {
                "count": 0,
                "match": ['Certified Information Systems Security Professional', 'CISSP'],
                "fuzzy": {
                    "includeExclude": []
                }
          },
          'Certified Secure Software Lifecycle Professional': {
                "count": 0,
                "match": ['Certified Secure Software Lifecycle Professional', 'CSSLP'],
                "fuzzy": {
                    "includeExclude": [[{'csslp', 'certified'}, set()],
                    [{'csslp', 'certification'}, set()]]
                }
          },
          'Certified Information Systems Auditor': {
                "count": 0,
                "match": ['Certified Information Systems Auditor', 'CISA'],
                "fuzzy": {
                    "includeExclude": [],
                    "exclude": []
                }
          },
          'Certified Cloud Security Professional (CCSP)': {
                "count": 0,
                "match": ['Certified Cloud Security Professional', 'CCSP'],
                "fuzzy": {
                    "includeExclude": []
                }
          },
          'CREST Certified': {
                "count": 0,
                "match": ['CREST Certified'],
                "fuzzy": {
                    "includeExclude": [[{'crest', 'certified'}, set()]]
                }
          },
          'Offensive Security Certified Professional': {
                "count": 0,
                "match": ['Offensive Security Certified Professional', 'OSCP'],
                "fuzzy": {
                    "includeExclude": []
                }
          },        
          'Certified Ethical Hacker': {
                "count": 0,
                "match": ['Certified Ethical Hacker', 'CEH'],
                "fuzzy": {
                    "includeExclude": [[{'ethical', 'hacker', 'certified'}, set()],
                    [{'certificaion', 'ethical', 'hacker'}, set()]]
                }
          },

        # Network Related Certifications
          'Cisco Certified Network Associate': {
                "count": 0,
                "match": ['Cisco Certified Network Associate', 'CCNA'],
                "fuzzy": {
                    "includeExclude": [[{'ccnp', 'certified'}, set()],
                    [{'ccnp', 'certification'}, set()]]
                }
          },
          'Cisco Certified Internetwork Expert': {
                "count": 0,
                "match": ['Cisco Certified Internetwork Expert', 'CCIE'],
                "fuzzy": {
                    "includeExclude": [[{'cisco', 'certified'}, set()],
                    [{'cisco', 'certification'}, set()]]
                }
          },  
        # Product or Technology Specific Certifications
          'Microsoft SharePoint Certified': {
                "count": 0,
                "match": ['SharePoint Certified'],
                "fuzzy": {
                    "includeExclude": [[{'sharepoint', 'certification'}, set()],
                    [{'sharepoint', 'certified'}, set()]]
                }
          },
        'LotusNotes Certified': {
                "count": 0,
                "match": ['LotusNotes Certified'],
                "fuzzy": {
                    "includeExclude": [[{'lotus', 'certification'}, set()],
                    [{'lotus', 'certified'}, set()]]
                }
          },
          'UIPath Certified': {
                "count": 0,
                "match": ['UIPath Certified'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'uipath'}, set()],
                    [{'certification', 'uipath'}, set()]]
                }
          },
          'Kubernetes Certified': {
                "count": 0,
                "match": ['Kubernetes Certified'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'kubernetes'}, set()],
                    [{'certification', 'kubernetes'}, set()]]
                }
          },
          'Microsoft Power BI Certified': {
                "count": 0,
                "match": ['Microsoft Power BI Certified'],
                "fuzzy": {
                    "includeExclude": []
                }
          },
          'Certified Data Scientist': {
                "count": 0,
                "match": ['Certified Data Scientist'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'data', 'scientist'}, set()]]
                }
          },         
          'SAP Certified Application': {
                "count": 0,
                "match": ['SAP Certified Application'],
                "fuzzy": {
                    "includeExclude": [[{'sap', 'certified'}, set()],
                    [{'sap', 'certification'}, set()]]
                }
          },
          'PEGA Certified': {
                "count": 0,
                "match": ['PEGA Certified'],
                "fuzzy": {
                    "includeExclude": [[{'pega', 'certified'}, set()],
                    [{'pega', 'certification'}, set()]]
                }
          },
          'Cloudera Certified': {
                "count": 0,
                "match": ['Cloudera Certified'],
                "fuzzy": {
                    "includeExclude": [[{'cloudera', 'certified'}, set()],
                    [{'cloudera', 'certification'}, set()]]
                }
          },
          'RedHat Certified': {
                "count": 0,
                "match": ['RedHat Certified'],
                "fuzzy": {
                    "includeExclude": [[{'redhat', 'certified'}, set()],
                    [{'redhat', 'certification'}, set()]]
                }
          },
          'Mulesoft Certified': {
                "count": 0,
                "match": ['Mulesoft Certified'],
                "fuzzy": {
                    "includeExclude": [[{'mulesoft', 'certified'}, set()],
                    [{'mulesoft', 'certification'}, set()]]
                }
          },
          'Tableau Certified': {
                "count": 0,
                "match": ['Tableau Certified'],
                "fuzzy": {
                    "includeExclude": [[{'tableau', 'certified'}, set()],
                    [{'tableau', 'certification'}, set()]]
                }
          },
          'Lean Certified': {
                "count": 0,
                "match": ['Lean Certified'],
                "fuzzy": {
                    "includeExclude": [[{'lean', 'certified'}, set()],
                    [{'lean', 'certification'}, set()]]
                }
          },
          'Workday Certified': {
                "count": 0,
                "match": ['Workday Certified'],
                "fuzzy": {
                    "includeExclude": [[{'workday', 'certified'}, set()],
                    [{'workday', 'certification'}, set()]]
                }
          },
          'SuccessFactors Certified': {
                "count": 0,
                "match": ['SuccessFactors Certified'],
                "fuzzy": {
                    "includeExclude": [[{'successfactors', 'certified'}, set()],
                    [{'successfactors', 'certification'}, set()]]
                }
          },
          'Qlik Certified': {
                "count": 0,
                "match": ['Qlik Certified'],
                "fuzzy": {
                    "includeExclude": [[{'qlik', 'certified'}, set()],
                    [{'qlik', 'certification'}, set()]]
                }
          },
          'Certified Software Quality Testing Engineer': {
                "count": 0,
                "match": ['Certified Software Quality Engineer', 'CCQE'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'quality'}, set()],
                    [{'certification', 'quality'}, set()],
                    [{'certified', 'testing'}, set()],
                    [{'certification', 'testing'}, set()], ]
                }
          },
          'Certified Forensic Examiner': {
                "count": 0,
                "match": ['Certified Forensic', 'GCFE', 'GCFA', 'GNFA'],
                "fuzzy": {
                    "includeExclude": [[{'certified', 'forensic'}, set()],
                    [{'certification', 'forensic'}, set()],
                    [{'certified', 'examiner'}, set()],
                    [{'certification', 'examiner'}, set()], ]
                }
          },

          # Others
        'Data Science Analytics Engineering Analyst Certified': {
                "count": 0,
                "match": ['Data Science Certified', 'Data Engineering Certified'],
                "fuzzy": {
                    "includeExclude": [[{'data', 'science', 'certified'}, set()],
                    [{'data', 'science', 'certification'}, set()],
                    [{'data', 'engineering', 'certified'}, set()],
                    [{'data', 'engineering', 'certification'}, set()],
                    [{'big', 'data', 'certified'}, set()],
                    [{'big', 'data', 'certification'}, set()],
                    [{'data', 'analytics', 'certified'}, set()],
                    [{'data', 'analytics', 'certification'}, set()]]
                }
          }, 
          'CEI Certified': {
                "count": 0,
                "match": ['CEI Certified'],
                "fuzzy": {
                    "includeExclude": [[{'cei', 'certified'}, set()],
                    [{'cei', 'certification'}, set()]]
                }
          }
        }
