"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    # minimum number of pairs of letters for word to be a palindrome
    match_req = len(word)/2
    # build dic of chars in string with count as values
    letter_counts = {letter: word.count(letter) for letter in word}

    found_match = 0
    # loops through dict of letters and increments found_match for every pair
    for key in letter_counts:
            found_match += letter_counts[key]/2

    # compares found matches to required matches
    if found_match == match_req:
        return True
    else:
            return False


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
