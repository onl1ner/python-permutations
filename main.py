# Formatting an input to prevent
# wrong input format, such as
# empty symbols.
def _format(symbols):
    # Stripping symbols to remove 
    # leading and trailing spaces.
    formatted = [symbol.strip() for symbol in symbols]

    # Removing empty symbols.
    filtered  = filter(lambda symbol: symbol, formatted)

    return list(filtered)

# Returns list of items
# that were separated by comma.
def input_list():
    str_input = input("Enter symbols (separated by comma):")

    # Splitting entered string
    # by comma as separator.
    sym_array = str_input.split(',')
    
    return _format(sym_array)

def permute_recursively(symbols):
    # Converting input into plain string 
    # with entered symbols.
    symbols = ''.join(symbols)

    # Base case for recursion.
    if len(symbols) == 1:
         return [symbols]

    # All possible permutations of given symbols.
    permutations = []

    # Looping through each symbol in string.
    for symbol in symbols:
        # Creating permutations recursively for symbol
        # by removing it from the resulting string.
        for permutation in permute_recursively(symbols.replace(symbol, '', 1)):
            # Adding new permuted string with the symbol
            # that was removed from the string.
            permutations.append(symbol + permutation)

    return permutations

symbols = input_list()
print("Permutations: ", permute_recursively(symbols))