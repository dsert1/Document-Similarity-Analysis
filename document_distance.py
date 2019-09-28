# 6.0001 Fall 2019
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Deniz Sert
# Collaborators: Tim from office hours, Olivia Tao, more people from Office Hours
# Time Spent: 5 hrs
# Late Days Used: 0

import string

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other 


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    #print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text
    """
    return(input_text.split())

### Problem 1: Find Bigrams ###
def find_bigrams(single_words):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
    Returns:
        list of bigrams from input text list
        :type single_words: object
    """
    list = []
    #creates pairs of words (bigrams) in list of single words
    for x in range(len(single_words)-1):
        list.append(single_words[x] + " " + single_words[x + 1])
    return list

### Problem 2: Word Frequency ###
def get_frequencies(words):
    """
    Args:
        words: list of words (or bigrams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string 
        is a word (or bigram) in words and the corresponding int 
        is the frequency of the word (or bigram) in words
    """
    dict = {}
    #iterates through words in given word list
    for w in words:
        if w in dict:
            dict[w]+=1
        else:
            dict[w]=1
    return dict

### Problem 3: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary of words or bigrams for one text
        dict2: frequency dictionary of words or bigrams for another text
    Returns:
        float, a number between 0 and 1, inclusive 
        representing how similar the texts are to each other
        
        The difference in text frequencies = DIFF sums words 
        from these three scenarios: 
        * If a word or bigram occurs in dict1 and dict2 then 
          get the difference in frequencies
        * If a word or bigram occurs only in dict1 then take the 
          frequency from dict1
        * If a word or bigram occurs only in dict2 then take the 
          frequency from dict2
         The total frequencies = ALL is calculated by summing 
         all frequencies in both dict1 and dict2. 
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    DIFF = 0
    ALL = 0
    #calculates ALL frequencies (sum of dict1 and dict2)
    for x in dict1:
        ALL += dict1.get(x)
        if x in dict2:
            DIFF += abs((dict1.get(x)-dict2.get(x)))
        else:
            DIFF += dict1.get(x)
    for y in dict2:
        ALL += dict2.get(y)
        if y not in dict1:
            DIFF += dict2.get(y)
    if ALL != 0:
        return round(1 - (DIFF/ALL), 2)
    else:
        return 0.0

    # PREVIOUS ATTEMPTS
    # if dict1.get_frequencies()
    #
    #
    #  for x in range len(dict1):
    #      word = list(my_dict.keys())[x]
    #         if word == dict1.get_frequencies(word)
    #
    #
    # # min = 0
    # # max = dict1.get(0)
    # # if dict1




    # DIFF = 0.0
    # ALL = 0.0
    # print("Dict 1: ", dict1)
    # print("Dict 2: ", dict2)
    # if len(dict1.keys()) == 0:
    #     return 0.0
    # for x in dict1.keys():
    #     ALL += dict1.get(x)
    #     for y in dict2.keys():
    #         if y in dict1:
    #             DIFF += abs(dict1.get(x) - (dict2.get(y)))
    #
    #
    #         ALL += dict2.get(y)
    #     if x not in dict2:
    #         DIFF += dict1.get(x)
    #
    #
    #
    #
    #

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries
    
    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency. 
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2. 
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    dict3 = {}
    l = []

    #goes through each word in dict1 and sees if it is in dict2
    for w in dict1:
        if w in dict2:
            dict3[w] = dict1[w] + dict2[w]
        else:
            dict3[w] = dict1[w]


    for w in dict2:
        if w not in dict1:
            dict3[w] = dict2[w]

    max_dict = 0
    max_dict = max(dict3.values())

    #finds the key that corresponds to the highest value
    for w in dict3:
        if dict3[w] == max_dict:
            l.append(w)
    return l


    #PREVIOUS ATTEMPTS
    # for w in dict2:
    #     if w in dict3:
    #         dict3[w]+=1
    #     else:
    #         pass

    #max = max(dict3.values())

    # l = list(dict3.keys())
    # l.sort()
    # return max






    # l = []
    # max1 = max(dict1.values())
    #
    # for i in dict1:
    #     if dict1[i] == max1:
    #         w1 = i
    #
    # max2 = max(dict2.values())
    #
    # for i in dict2:
    #     if dict2[i] == max2:
    #         w2 = i
    #
    #
    # for x in dict1:
    #     if len(dict1) == 0:
    #         max1 = dict2.get(0)
    #     elif dict1[x]>max1:
    #         max1 = dict1.get(x)
    #         #print(max)
    # list.append(max1)
    #
    #
    # for y in dict2:
    #     if dict2[y]>max2:
    #         max2 = dict2.[y]
    #        # print(max)
    # list.append(max2)
    #
    # #checks on maxs
    # if max1==max2:
    #     if w1<w2:
    #         list[0] = w1
    #         list[1] = w2
    # elif max1>max2:
    #     l[0] = w1
    #     list[1] = w2
    # else:
    #     l[0] = w2
    #     l[1] = w1
    #
    # return l


### Problem 5: Finding closest artist ###
def find_closest_artist(artist_to_songfiles, mystery_lyrics, bigrams = False):
    """
    Args:
        artist_to_songfiles: 
            dictionary that maps string:list of strings 
            where each string key is an artist name
            and the corresponding list is a list of filenames (including the extension),
            each holding lyrics to a song by that artist
        mystery_lyrics: string of lyrics 
            Can be more than one or two words (can also be an empty string)
            assume the string is made of lowercase characters
        bigrams: boolean, optional parameter. Default set to False.
            If it is True, bigrams of text in files 
            and bigrams of mystery_lyrics should be used in analysis.
    Returns:
        list of artists (in alphabetical order) that best match the mystery lyrics

    The best match is defined as the artist(s) whose songs have the highest average
    similarity score with the mystery lyrics. If there is only one such artist, then
    this function should return a singleton list containing only that artist. However,
    if all artists have an average similarity score of zero with respect to the
    mystery_lyrics, then this function should return an empty list. When no artists 
    are included in the artist_to_songfiles, this function returns an empty list.
    """
    #prepping data
    new_dict_artists = {}
    new_dict_mystery = {}
    l = []
    dict_avg = {}

    #for e in artist_to_songfiles:
    if len(artist_to_songfiles) == 0:
        return []

    if bigrams:
        mystery_freq = get_frequencies(find_bigrams(prep_data(mystery_lyrics)))
    else:
        mystery_freq = get_frequencies(prep_data(mystery_lyrics))



    for artists in artist_to_songfiles.keys():
        tot_sim = 0


        for songs in artist_to_songfiles[artists]:
            l1 = prep_data(load_file(songs))

            #checks to see if there are bigrams
            if bigrams:
                dict_a = get_frequencies(find_bigrams(l1))
                tot_sim = calculate_similarity_score(dict_a, mystery_freq)
            #no bigram, continue like normal
            else:
                dict_a = get_frequencies(l1)
                tot_sim = calculate_similarity_score(dict_a, mystery_freq)

        avg_sim = tot_sim / len(artist_to_songfiles[artists])
        dict_avg[artists] = avg_sim

    #determine the largest avg similarity score
    max_avg = max(dict_avg.values())
    if max_avg < 1e-9:
        return []
    for a in dict_avg:
        if abs(max_avg - dict_avg[a]) < 1e-9:
            l.append(a)
    #return list of highest frequency score artists
    return l
















    

if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    ## Tests Problem 0: Prep Data
    #test_directory = "tests/student_tests/" 
    #hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt') 
    #world, friend = prep_data(hello_world), prep_data(hello_friend)
    #print(world) ## should print ['hello', 'world', 'hello']
    #print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Find Bigrams
    #world_bigrams, friend_bigrams = find_bigrams(world), find_bigrams(friend)
    #print(world_bigrams) ## should print ['hello world', 'world hello']
    #print(friend_bigrams) ## should print ['hello friends']

    ## Tests Problem 2: Get frequency
    #world_word_freq, world_bigram_freq = get_frequencies(world), get_frequencies(world_bigrams)
    #friend_word_freq, friend_bigram_freq = get_frequencies(friend), get_frequencies(friend_bigrams)
    #print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    #print(world_bigram_freq) ## should print {'hello world': 1, 'world hello': 1}
    #print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    #print(friend_bigram_freq) ## should print {'hello friends': 1}

    ## Tests Problem 3: Similarity
    #word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    #bigram_similarity = calculate_similarity_score(world_bigram_freq, friend_bigram_freq)
    #print(word_similarity) ## should print 0.4
    #print(bigram_similarity) ## should print 0.0

    ## Tests Problem 4: Most Frequent Word(s)
    #freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    #most_frequent = get_most_frequent_words(freq1, freq2)
    #print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find closest matching artist
    #test_directory = "tests/student_tests/" 
    #artist_to_songfiles_map = {
    #"artist_1": [test_directory + "artist_1/song_1.txt", test_directory + "artist_1/song_2.txt", test_directory + "artist_1/song_3.txt"],
    #"artist_2": [test_directory + "artist_2/song_1.txt", test_directory + "artist_2/song_2.txt", test_directory + "artist_2/song_3.txt"],
    #}
    #mystery_lyrics = load_file(test_directory + "mystery_lyrics/mystery_1.txt") # change which number mystery lyrics (1-5)
    #print(find_closest_artist(artist_to_songfiles_map, mystery_lyrics)) # should print ['artist_1']
