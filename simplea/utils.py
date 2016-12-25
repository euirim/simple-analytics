def add_suffix(txt, suffix):
    """add the given to every element in given comma separated list
    
    Example:
    add_suffix("hello,john", "ga:") -> "ga:hello,ga:john"
    """

    elements = txt.split(",")
    elements = [suffix + e for e in elements]
    
    return "".join(elements)
