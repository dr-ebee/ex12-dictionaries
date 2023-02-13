def pad_word_count(essay):
    """
    This function replaces any contractions (e.g. "can't", "we're", "they've",
    "that's") and replaces them with the full words (e.g. "cannot", "we are",
    "they have", "that is").

    For the purpose of this exercise, ignore the fact that sometimes we use "'s"
    to mean "is" and other times we use "'s" as a possessive marker. Assume
    every time we see "'s", it's a contraction of "is"
    """
    new_essay = essay

    # INSTRUCTIONS
    # Here's an answer to a quiz question.
    # There's a lot of repetition here.
    # Use a dictionary and a loop to change this so we only have one line of
    # code that uses the `.replace()` method.

    #### START REPLACING HERE
    # Cannot is an exception to the usual rule, since it's all one word
    new_essay = new_essay.replace("can't", "cannot")
    new_essay = new_essay.replace("Can't", "Cannot")

    # The rest of the words have a regular pattern
    new_essay = new_essay.replace("n't", " not")
    new_essay = new_essay.replace("'s", " is")
    new_essay = new_essay.replace("'re", " are")
    new_essay = new_essay.replace("'ve", " have")
    #### STOP REPLACING HERE

    return new_essay

# Here's the function call.
# Don't change this.
print(pad_word_count(
"""
Cats are cute.
They've been pets for thousands of years.
They're playful and cuddly but they don't need as much attention as dogs.
It's clear that they're silly and they can't resist knocking things over.
It isn't possible to see a cat and not want to cuddle it.
That's all I have to say about cats.
"""
))


