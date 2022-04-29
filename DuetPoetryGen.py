# DUET takes two files froma list, and randomly interleaves lines from them together.
# Script by Sagan Yee, 2022

import random
import re

files = []

# Replace the .txt filenames with your own files. Make sure they're in the same folder as your script.
file1 = open('testfile1.txt', errors='ignore').read()
file2 = open('testfile2.txt', errors='ignore').read()
finalpoem = ''

# Turns the texts into Python lists by splitting them at the period.
split1 = file1.split('.')
split2 = file2.split('.')

# Gets rid of whitespace.
text1 = [x.strip() for x in split1]
text2 = [x.strip() for x in split2]

poem_bucket = []

# Randomly picks lines from both texts and puts them in a single list called Poem Bucket, i times.
i = 15 # Change this number to determine how long the final poem will be.
while i > 0:
    random1 = random.choice(text1)
    random2 = random.choice(text2)
    poem_bucket.append(random1)
    poem_bucket.append(random2)
    i -= 1

# Replaces punctation with line breaks, or gets rid of them entirely.
for line in poem_bucket:
    line = line.replace(',','\n')
    line = line.replace('.','\n')
    line = line.replace('; ','\n')
    line = line.replace(':','\n')
    line = line.replace('!','\n')
    line = line.replace('?','\n')
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace(' and ','\n')
    line = line.replace('"','')
    line = line.replace('“','')
    line = line.replace('”','\n')
    line = line.replace("'",'\n')
    line = line.strip(' ')
    # If the character length of the line is greater than a number and less than a number, make it lowercase and add it to the Final Poem.
    if len(line) >= 10 and len(line) <= 50:
        rline = " ".join(line.split())
        finalpoem += rline.lower() + '\n'

# Randomly picks a line from the Poem Bucket. If it's less than 50 characters, it will make it the final line of the poem and put line breaks between every word.
lastline = random.choice(poem_bucket)
while len(lastline) > 50:
    lastline = random.choice(poem_bucket)
else:
    splitline = lastline.split()
    for line in splitline:
        finalpoem += line.lower() + '\n'

# Writes the final poem to a text file in your project folder.
# Running the script again will overwrite the file, so save your favs!
with open('_FinalPoem.txt', 'w', encoding='utf8') as f:
    f.write(finalpoem)

print("Finished!")


