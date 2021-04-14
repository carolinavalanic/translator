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

# Treat the text so it can be ready to translate
text_splitted = re.split('(\W+)',data_text[0])

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
    count = 0 
    text_copy = text
    for word in text:
        text_copy[count] = test_word_in_dict(word,lol_dict)
        count = count + 1
    return ''.join(text_copy)

# Save the result in the 
save = open(text_path.split('.')[0]+'_lolcat.'+text_path.split('.')[1],'w').write(translator(text_splitted)) 

if save > 0:
    print("That's all, check your folder and find the file "+ text_path.split('.')[0] +'_lolcat.'+text_path.split('.')[1]+" :)")
else:
    print("Oh no, something went wrong!")
