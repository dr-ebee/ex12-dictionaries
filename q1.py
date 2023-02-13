# You have been given the following list of students and their test scores:
names = ["Maria", "Nushi", "Mohammed", "Jose", "Wei"]
scores = [10, 23, 13, 18, 12]

# Write a function `make_dictionary` that takes two lists and returns a
# dictionary with the names as keys and the scores as values.
def make_dictionary(keys_list, values_list):
    """
    turn 2 lists into a dictionary

    Here are some tests. Make sure your code can handle these cases!
    >>> make_dictionary(["a", "b"], [1, 2])
    {'a': 1, 'b': 2}
    >>> make_dictionary([1, 2, 3], [5, 6, 7])
    {1: 5, 2: 6, 3: 7}
    >>> make_dictionary(["a", "b", "c", "d"], ["apple", "banana", "clementine", "date"])
    {'a': 'apple', 'b': 'banana', 'c': 'clementine', 'd': 'date'}
    >>> make_dictionary(["key"], ["value"])
    {'key': 'value'}
    """
    
    return #### YOUR CODE HERE

if __name__ == "__main__":
    # Running tests: don't change this part!
    import doctest
    print("Running tests...")
    doctest.testmod()
    print("All tests have finished!")

    # Apply `make_dictionary` to the arguments `names` and `scores`. Save the
    # result to a variable `score_dict`. Print `score_dict`.
    #### YOUR CODE HERE

    # Using `score_dict`, find and print the score for "Mohammed".
    #### YOUR CODE HERE

    # Add a score of 19 for "Yan". Print `score_dict`.
    #### YOUR CODE HERE

    # Update the score for "Wei" to be 13. Print `score_dict`.
    #### YOUR CODE HERE

    # Nushi has just dropped the class. Delete "Nushi" and their score from
    # `score_dict`. Print `score_dict`.
    #### YOUR CODE HERE


