def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if(type(s)!=str):
        return("Not a valid input");
    return s[::-1]
    """val="";
    for x in range(len(s),0,-1):
        val=val + s[x-1];
        return val;
        """
    
    
    


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World"));
print(string_reverse("Python"));
print(string_reverse(123));