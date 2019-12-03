def tests() -> None:
    """
    This function is to test the countdown program functions.

    Each function is tested with a single test case and the result is printed
    to the user in the stdout.
    """
    #check the data entry returns data correctly
    assert select_characters(True) == "testdatas","select_characters test: FAILED"
    #check that the standard word.txt file is being read correctly
    assert len(read_dictionary("words.txt")) == 235887, "read_dictionary test: FAILED"
    #check that the lookup can find anagrams
    assert "rat" in word_lookup("tar"), "word_lookup test: FAILED"
