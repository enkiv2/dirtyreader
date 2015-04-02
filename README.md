# dirtyreader
Convert innocent words into profanity, and optionally insert brand new profanity randomly

Usage:

    ./dirtyreader.py [insertionrate] [+slurs] < textfile

If supplied, insertionrate is the inverse of the frequency at which profanity is simply inserted. If insertionrate is 2, profanity will be inserted (on average) every two words. If not supplied, profanity will not be inserted; only the swapping behavior will occur (so the word count will remain constant).

Additionally, innocent words that have profane equivalents will be replaced by them, and profane words will be replaced with semantically similar profane words.

If the second argument is supplied and is equal to '+slurs', then slurs are added to the general profanity list. They are off by default. While you cannot enable slurs without setting an insertion rate, an insertion rate of 0 is equivalent to the default behavior.
