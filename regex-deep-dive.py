'''  
Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data. 
You will tackle a variety of real-world scenarios, applying regex to extract, validate, and transform text effectively.

Task 1: Email Extraction Enhancement

Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). 
Modify the script to extract all email addresses except those from the specified domain.

Code Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
Adapt the regex pattern to exclude email addresses from '[exclude.com]C'.

Ensure the script still extracts all other valid email addresses. 
'''

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@domain.com, user5@exclude.com"  # added 2 more emails to show that all 'exclude' emails are being filtered 

def extract_emails(text, excluded_emails):   # function to filter emails from ''text' 
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) # regex for extracting emails from text
    
    refined_emails = [email for email in emails if email not in excluded_emails]   # list of emails that are not in our list of excluded emails 
    
    return refined_emails # return list of filtered emails 

exclude_emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[exclude]+\.[A-Z|a-z]{2,}\b", text) # list of emails to exclude (any email with 'exclude') 

filtered_emails = extract_emails(text, exclude_emails) #new list that calles function to fliter through 'text' 
 
print(filtered_emails)  

