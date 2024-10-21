score = int(input("Score? "))

file = open("testing.txt", "r+")
high_score = file.read()
if high_score == "":
    high_score = "0"
if score > int(high_score):
    file.seek(0)  # goes back to the start of the file
    file.write(str(score))  # writes new high score
    file.truncate()  # deletes anything after new high score
    print(f"High Score: {score}")

else:
    print(f"High Score: {high_score}")
