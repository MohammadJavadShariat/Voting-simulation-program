National_codes = set()
saeed , bagher , masoud = 0 , 0 , 0
Invalid_vote = 0
len_person = 0

while(True):
    try:
       
        #Receive national code
        National_code1 = input("Enter Exit to exit.\nEnter your national code:")
        
        #Exit the program
        if National_code1 == "Exit" :
            break
        
        #Convert national code to number
        National_code = int(National_code1) 
        
        # Adding the national code to the national codes
        National_codes.add(National_code) 
        
        # If the number of national codes is more than the 
        #number of people, add the vote to the candidate
        if len(National_codes) > len_person :  
            vote = input("Enter exit to exit.\nWrite your vote:")
            if vote == "saeed" :
                saeed += 1
            elif vote == "bagher" :
                bagher += 1
            elif vote == "masoud" :
                masoud += 1
            elif vote == "Exit" :
                National_codes.remove(National_code)
                break
            else:
                Invalid_vote += 1
        else:#Warn if the code is entered again
            print("Dear friend, don't cheat! Did you think we don't understand?")
        
        #People should be equal to co-nationals
        len_person = len(National_codes) 
    except:#Warn if there is a word
        print("Please enter the correct national code.")

#If the national code is empty, show a sentence
if National_codes == set() :
    National_codes = ["There is no national code."]

print(f"\n******voting result******\n\nSaeed's vote:{saeed}")
print(f"vote Masoud: {masoud}")
print(f"vote Bagher: {bagher}")
print(f"Invalid vote: {Invalid_vote}")
print(National_codes)