#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    #islower() is to check whether ALL letters are lowercase, not just one
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    #'c' will always return "True" (its a string)
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    #returns result of last c in s
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    #Boolean statement returns inaccurate results
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    #This function does not allow any capitalized letters 
    for c in s:
        if not c.islower():
            return False
    return True



###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print("Hello World!")


if __name__ == '__main__':
    main()
