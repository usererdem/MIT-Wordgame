# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import time

wildcard = '*'
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """    
    HAND_SIZE = n    
    first_score = 0
    second_score = 0
    
    word_length = len(word)
    word = (word.lower())
    for char in word:
        for key, value in SCRABBLE_LETTER_VALUES.items(): 
            if char == key: 
                first_score += value
           
        
    if 7 * word_length - 3 * (n - word_length) >= 1:
        second_score = 7 * word_length - 3 * (n-word_length)
        n = n - word_length
    else:
        second_score = 1
        n = n - word_length
    word_score = first_score * second_score
    return word_score
    
   
    
   
    
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    
    Wildcard_dictin içine handde olan vowellar giriyor içinden random bir vowel
    seçiliyor, bu seçilen random vowel, hand dictionarynin içinde aranıp
    bulunuyor ve onun yerine wildcard yerleştiriliyor.Aynı harfi for loopta iki
    üç kere değiştirmemesi için pass veya break gerekebilir hata olursa bak.
    """
    
    hand={}
    wildcard_dict={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    for y in hand.keys():
        for z in VOWELS:
            if y == z:
                wildcard_dict[y] = wildcard_dict.get(y, 0) + 1
    a = random.choice(list(wildcard_dict))
    for b in hand.keys():
        if a == b:
            hand[a] -= 1 
            hand[wildcard] = 1
            break
            
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = (word.lower())
    new_hand = hand.copy()
    for x in word:
        for y in new_hand.keys():
            if x ==y:
                if new_hand[y] == 0:
                    pass
                else:
                    new_hand[y] -= 1
                
                
    return new_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    Kelime wordlistin içinde varsa kelimenin harfleriyle dictionary harfleri
    kıyaslanıyor ortak cıkarsa county ile handy sayıları kıyaslanıyor county 
    fazla ise false veriyor.
    
    eğer kelime wordlist içinde değilse yazılan kelime ile elindekiler uyuşuyormu
    baktıktan sonra, uyuşuyorsa wildcardın konulduğu yer hariç bütün harfleri tutan 
    bir kelime varmı kontrol ediliyor, eğer varsa, wildcardın konulduğu yer 
    herhangi bir vowel yani sesli harf ise doğru kelime olarak kabul ediliyor.
    eğer değilse yanlış kelime dönüyor.
    """
    count={}
    word = (word.lower()) 
    wildcard_index = word.find('*')
    is_valid = False
    ct = 0
    a = 0
    VOWELS = 'aeiou'
    
    for x in word:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
                 
    if word in word_list:
        for x in word:
            for y in hand.keys():
                if x == y:
                    if count[y] > hand[y]:
                        is_valid = False
                        break
                    else:
                        is_valid = True
                        ct += 1
                else:
                    is_valid = False
    
        if ct == len(word):
            is_valid = True
        else:
            is_valid = False 
    else:
        for x in word:
            if x in hand:
                if count[x] > hand[x]:
                    is_valid = False
                else:
                    is_valid = True
                    a += 1                   
            else:
                is_valid = False
        if a != len(word):
            is_valid = False
        else:
            if wildcard_index > -1:        
                s = list(word)
                for w in word_list:                    
                    if len(word) == len(w):
                        ct = 0
                        for i in range(len(w)):                                
                            if s[i] == w[i]:
                                ct += 1
                            else:
                                pass                        
                
                    if len(word) -1 == ct:
                        if w[wildcard_index] in VOWELS:
                            is_valid = True
                            break
                        else:
                            is_valid = False
                    else:
                        is_valid = False
            else:
                is_valid = False
    
    return is_valid
        
                   
                    
                        
                        
                                     
                        

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    number_of_letters = 0
    for x in hand:
        number_of_letters += hand[x]
    return number_of_letters

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    total_score = 0
    current_handlen = calculate_handlen(hand)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    while current_handlen > 0:
        # Display the hand
        
        print("Current Hand: ", end='')
        display_hand(hand)
        # Ask user for input
        player_guess = input("Enter word, or '!!' to indicate that you are finished: ")        
        # If the input is two exclamation points:
        if player_guess == "!!":                                          
                # End the game (break out of the loop)
            break 
            
        # Otherwise (the input is not two exclamation points):
        else:            
            # If the word is valid:
            if is_valid_word(player_guess,hand,word_list) == True:
                # Tell the user how many points the word earned,
                # and the updated total score
                score = get_word_score(player_guess,current_handlen)
                total_score += score
                print(player_guess, 'earned', score, 'points. Total = ', total_score, 'points \n')
                
            # Otherwise (the word is not valid):
            else:
                
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word. ')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand,player_guess)
            current_handlen = calculate_handlen(hand)
            
    # Game is over (user entered '!!' or ran out of letters),
    if current_handlen == 0:
        print('Run out of letters. Total Score: ', total_score, 'points')
    # so tell user the total score
    else:
        print('Total Score: ', total_score, 'points')
    
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
   
    x = random.choice(VOWELS)
    y = random.choice(CONSONANTS)
    z = x + y
    z = random.choice(z) 
    
    for b in hand: 
        if z == b:
            x = random.choice(VOWELS)
            y = random.choice(CONSONANTS)
            z = x + y
            z = random.choice(z)
            
        else:
            break
    
    for a in hand:
        if a == letter:
            hand[a] -= 1
            hand[z] = 1
            break
        
    return hand      
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    end_score = 0
    count_hand = 0
    # Kac el oynamak istedigini soruyorum.
    number_of_hands = input('Enter total number of hands: ')
    
    # istedigi el kadar oynamasi icin while loopa sokuyorum ileride counthand +1 olacak sonda
    while int(number_of_hands) > count_hand:
        
        # Eli dagitip handi dagitilan ele tanimladik.
        hand = deal_hand(HAND_SIZE)
        
        # Elimizdeki harfleri oyuncuya print edelim.
        print("Current Hand: ", end='')
        display_hand(hand)
        
        # Degistirmek istedigi kelime var mi diye soralim.
        is_want_change = input('Would you like to substitute a letter?(type yes or no): ')
        
        # Eger varsa substitute_hand fonksiyonunu cagiralim ve degistirmek istedigi letteri icine yollayalim.
        if is_want_change == 'yes':
            letter = input('Which letter would you like to replace: ')
            substitute_hand(hand, letter)
       
        # Artik oyuncu eli oynayabilir. play_hand fonksiyonunu cagir.
        # play_handi total_scorea esitle boylelikle ilerde kullanabilmek icin elimizde return value olsun.        
        total_score = play_hand(hand,word_list)
        
        # Tekrar oynamak istiyor musun diye sor.
        play_again = input('Would you like to replay the hand?(type yes or no): ')
        
        # istiyorsa tekrar oynat ve birebir ayni eli oynat. Bu sefer substitute hakki vermiyoruz.
        if play_again == 'yes':            
            total_score = play_hand(hand,word_list)
            
        # count_hand'i 1 arttır boylece loop 1 kere dondugunu anlasın. end_score yarat ve total scorelari orada topla.   
        count_hand += 1
        end_score += total_score
    
    # oyunun sonuna geldik. end_score bas, oynadigi ellerde aldigi tum total scorelarin toplami.    
    print('In',number_of_hands, 'amount of hands. You have made',end_score,'points.')
    print('Your EndGame score is: ', end_score)
    time.sleep(10.0)
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    