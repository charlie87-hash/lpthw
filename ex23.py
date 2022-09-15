
#another way of importing argv from sys
import sys
#assign variables to the argv
script, input_encoding, error = sys.argv

#define  main method to get our scripted started' read one line and store it in the line variable
#reads line by line in the language file till the end and terminates.
#function calling itself, recursion ???

def main(language_file, encoding, errors):
    line = language_file.readline()

    #decision making if line has something in it, else terminates to prevent us from being in a loop
    if line:
        print_line(line,encoding,errors)
        return main(language_file, encoding, errors)

#does the actual encoding from the laguanges text file

#DBES (memorize)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(cooked_string, "<==>",raw_bytes)

languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)