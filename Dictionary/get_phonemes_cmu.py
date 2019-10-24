import requests
from bs4 import BeautifulSoup

'''
Return two files, the words that are founded and the words that are still out of vocabulary, because they are not part of the dictionary.
'''
##################################
#	READ WORDS OVV TXT FILE	     #
##################################
path_file = 'oov_found.txt';
file_txt = open(path_file,'r');
file_txt_list = file_txt.readlines();
file_txt.close()

######################################
#			NEW DICTIONARY 			 #
######################################
#Create file for saving the words and their pronunciation
new_words_dictionary = open('wordsPhonemes.txt','w');

#Create file for saving words that are still out of vocabulary
wovv = open('still_oov_words.txt','w');

#Procesing the txt file
for word in file_txt_list:

	query_word = word.strip('\n').lower();
	url = 'http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in='+ query_word +'&stress=-s' #Take into account the stress of the word
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	rows = soup.find_all("tt")

	#If the row start with "http" means that word to phoneme was not found in the dictionary
	if not rows[1].get_text().startswith('http'):
		phonemes = rows[1].get_text()[:-2];
		new_words_dictionary.write(word.strip('\n').upper() + '\t' +phonemes + '\n');
	else:
		wovv.write(word);

new_words_dictionary.close()
wovv.close()

