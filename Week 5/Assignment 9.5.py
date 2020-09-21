# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#Read file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = {}

#Look for From  lines and take second word
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    
#create python dict for no of times mail appeears
    counts[words[1]] = counts.get(words[1], 0) + 1
    
#Find the most profilic value
bigcount = None
bigkey = None
for key in counts:
    if bigcount is None or bigcount < counts[key]:
        bigcount = counts[key]
        bigkey = key
        
print(bigkey, bigcount)
    
