# module docString sits at top of a file that tells dev what module is doing
"""
This is a module docString. They are not associated with a variable.
Each module should have a module docString that describes the file.
Can be considered overkill in production environment
"""

coollongvariablename = "hello everyone"
booleanvariable = True
def printtext(x):
    #  if(booleanvariable == True):
    #     print("yes")
    """
    Function docstring explains function
    """
    return f"text added is {x}"
print(printtext('Hello'))

