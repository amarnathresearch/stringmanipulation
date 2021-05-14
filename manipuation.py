# Template for Matching using NLP
import re
str = "It's easier for users to understand opencv-python than cv2 and It makes It easier to find the package with search engines. cv2 (old interface in old OpenCV versions was named as cv) is the name that OpenCV developers chose when they created the binding generators. This is kept as the import name to be consistent with different kind of tutorials around the internet. Changing the import name or behaviour would be also confusing to experienced users who are accustomed."

# print(str)

key = "It"
key = key.lower()
# Key is capitalized / Title case,

strsplit = str.split()

print(strsplit)
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
count = 0
for word in strsplit:
    # Case sensitivity

    word = word.lower() 
    if regex.search(word) != None:
        count += 1
        # divide into sub list
    # Special Characters // Regex
     
    if word == key:
        # Graph Edit distance: / how much similar the words could be
        #  Percentage of match -> Threshold >70
        count += 1
        print("matching", count)

        # Capital letters -> It is failing to matching
        # 's causing problems

        # Lowercase all the letters in the sentence, then you can match

# Regex -> Regular expression -> Check for special characters - > Then how will you solve this problems


# Problems:
# 1. Case Sensitive
# 2. Special characters
# 3. Spelling mistakes

# Extension of the Problems
    #  Semantic Relationship

    Key = "good" Synonyms
        = "fine"
        
        # OCR -> Optical Character Recognition (Image Processing) -> NLP -> Meaningful extraction
        