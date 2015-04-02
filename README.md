# dirtyreader
Convert innocent words into profanity, and optionally insert brand new profanity randomly

Usage:

    ./dirtyreader.py [insertionrate] < textfile

If supplied, insertionrate is the inverse of the frequency at which profanity is simply inserted. If insertionrate is 2, profanity will be inserted (on average) every two words.

Additionally, innocent words that have profane equivalents will be replaced by them, and profane words will be replaced with semantically similar profane words.
