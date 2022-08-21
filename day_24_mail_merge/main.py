# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("day_24_mail_merge\Input\Letters\starting_letter.txt") as f:
    content = f.read()
    with open("day_24_mail_merge\\Input\\Names\\invited_names.txt") as n:
        for line in n:
            line = line.strip()
            new_content = content.replace("[name]", line)
            l = open(f"day_24_mail_merge\Output\ReadyToSend\{line}.txt", "w")
            l.write(new_content)
            l.close()
