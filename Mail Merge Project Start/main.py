#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter_template = None
with open("Input/Letters/starting_letter.txt",mode="r") as letter:
    letter_template= letter.read()


guest_list = []
with open("Input/Names/invited_names.txt") as guest_names:
    guest_list = guest_names.read().splitlines()

for name in guest_list:
    file_name = name+"_invitation.txt"
    with open("Output/ReadyToSend/"+file_name,"w") as invitation:
        content = letter_template.replace("[name]",name)
        invitation.write(content)

