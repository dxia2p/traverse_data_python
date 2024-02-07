# Read the survey-results.txt

file = open("traverse_data/survey-results.txt", 'r') # open the text file
content = file.readlines() # take all the lines in the file and load it into an array
yesNum = 0
noNum = 0
maybeNum = 0
for str in content: # process the data
    if "Yes" in str:
        yesNum += 1
    elif "No" in str:
        noNum += 1
    elif "Maybe" in str:
        maybeNum += 1
    else:
        print("ERROR NOT A VALID ANSWER")
print(f"Yes({yesNum}), No({noNum}), Maybe({maybeNum})")
file.close()

# rEAD THE AGE-DATA.TXT

file = open("traverse_data/age-data.txt", 'r') # read the data
content = file.readlines() # load it into an array
under18 = 0
between18and35 = 0
between36and65 = 0
over65 = 0
for str in content: # process the data
    if int(str) < 18:
        under18 += 1
    elif int(str) <= 35:
        between18and35 += 1
    elif int(str) <= 65:
        between36and65 += 1
    else:
        over65 += 1
print(f"Under 18 ({under18}), 18 to 35 ({between18and35}), 36 to 65 ({between36and65}), Above 65 ({over65})")

# Read number-data.txt

file = open("traverse_data/number-data.txt", 'r') # read the data
content = file.readlines() # load it into an array
even = 0
odd = 0
for str in content: # check if the number is even or odd
    if int(str) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even ({even}), Odd({odd})")