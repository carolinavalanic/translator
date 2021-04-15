# Import libraries
import json
import requests
import re

# Read dictionary from github
data = requests.get("https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json")
lol_dict = json.loads(data.text)

# Ask user what the file path is 
text_path = input("What is the path for your text? Please, notice that your file should have .txt extension. Path:  ")

# Read the text from the path given
read_text = open(text_path)
data_text = read_text.readlines()

# Remove the line breaks (\n)
data_text_adjusted = []
for item in data_text:
    text_item = item.replace("\n","")
    data_text_adjusted.append(text_item) 

# Create function to split text
data_text_splitted = data_text_adjusted
count = 0
for item in data_text_adjusted:
    data_text_splitted[count] = re.split('(\W+)',item)
    count = count + 1

# Create function to test if the word exists in the dictionary and save it in a object
def test_word_in_dict(word, dictionary):
    """
    From a given word this function will try to find it in the dictionary. If it finds the word, it will 
    save the translated word in an object, otherwise it will save the inputed word.
    
    Inputs:
    word - A single string 
    dictionary - A dictionary in which the key is the word in the same language as the input, and the result 
    is the translated word.
    
    Outputs: 
    There are no outputs.
    """
    if word in list(dictionary):
        result = dictionary[word]
    else:
        result = word
    return result

# Create function to translate the text
def translator(text):
    """
    From a text in english, this function will translate it to the language existing in the dictionary available. 
    
    Inputs:
    text - A full text
    dictionary - A dictionary in which the key is the word in the same language as the input, and the result 
    is the translated word.
    
    Outputs: 
    There are no outputs.
    """
     
    text_copy = []
    for text_list in text:
        count = 0
        for word in text_list:
            text_list[count] = ((test_word_in_dict(word.casefold(),lol_dict)[0].upper() + test_word_in_dict(word.casefold(),lol_dict)[1:]) if len(word) > 1 and word[0].isupper() else test_word_in_dict(word.casefold(),lol_dict))
            count = count + 1
        agg = ''.join(text_list)
        text_copy.append(agg)
    return text_copy

#Apply function to the treated text
final_text = translator(data_text_splitted)

# Save the output in a new file
save_file = open(text_path.split('.')[0]+'_lolcat.'+text_path.split('.')[1],'w')
for lines in final_text:
    row = lines+'\n'
    save_file.write(row)
save_file.close()  


if len(open(text_path.split('.')[0]+'_lolcat.'+text_path.split('.')[1],'r').readlines()) > 0:
    print("That's all, check your folder and find the file "+ text_path.split('.')[0] +'_lolcat.'+text_path.split('.')[1]+" :)")
else:
    print("Oh no, something went wrong!")
