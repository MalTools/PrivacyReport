# Examination & Improvements for iOS App Privacy Report

This repository contains the first systematical study of the usability and effectiveness of the iOS App Privacy Report in real-world settings.
Our research follows a clear and logical workflow: 
1) We organized a focus group discussion to explore users' experiences, perceptions,
attitudes, and expectations regarding the App Privacy Report. The findings revealed practical deficiencies of the feature, 
primarily the lack of clarity in data access purposes and domain name descriptions. 
2) Based on user feedback, we developed methods to address these two main concerns. 
3) We conducted experiments to evaluate the performance and usability of our proposed improvements.

In this repository, we provide the key data and code used in our study.

## Fold Structure

```
.
├── README.md
├── data
│   ├── Weibo-description.txt
│   ├── Weibo-segmented.txt
│   └── domain_list.txt
├── result
│   ├── Weibo_pp_log.txt
│   ├── domain_desc_log.txt
│   ├── functionality_log.txt
│   └── inference_res.xlsx
├── src
│   ├── cot_reasoning.py
│   ├── extract_description.py
│   ├── extract_domain_info.py
│   ├── extract_privacy_policy.py
│   ├── hook_sensitive_api.js
│   ├── input_privacy_policy.py
│   ├── lib.py
│   └── process_privacy_policy.py
└── userstudy
    ├── Slides_FocusGroup.pdf
    └── Slides_ThinkAloud.pdf
```
***Note:*** This tree includes only main files. 

## Description
Below we describe each main file in our folder. The improvements include two aspects: purpose inference and domain clarification. 
The ```src``` directory contains the main code implementation scripts, 
and the ```data``` and ```result``` directories contain examples of the data used by the scripts and the results generated.

#### For Purpose Inference:
```*_privacy_policy.py```:  These scripts handle privacy policies, including crawling, slicing, and key information extraction.
```extract_description.py```: This script is used to extract the main functionalities of the app from its description in the App Store.
```hook_sensitive_api.js```: This script can track sensitive API invocations and get call stack traces.
```cot_reasoning.py```: This script uses the chain-of-thought method to infer purpose using LLM. It takes as input the 
app functionalities, the triple statements from the privacy policy, and the call stack traces.

#### For Domain Clarification:
```extract_domain_info.py```: This script uses LLM to identify information about a domain name.

#### User Study:
```Slides_*.pdf```: The key presentations we use when launching user studies such as focus group discussions and Think Aloud study.