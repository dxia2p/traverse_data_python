# Read the survey-results.txt

file = open("traverse_data/survey-results.txt", 'r')
content = file.readlines()
yesNum = 0
noNum = 0
maybeNum = 0
for str in content:
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

file = open("traverse_data/age-data.txt", 'r')
content = file.readlines()
under18 = 0
between18and35 = 0
between36and65 = 0
over65 = 0
for str in content:
    if int(str) < 18:
        under18 += 1
    elif int(str) <= 35:
        between18and35 += 1
    elif int(str) <= 65:
        between36and65 += 1
    else:
        over65 += 1
