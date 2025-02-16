import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
# TODO Set up regex
# TODO Find links using regex, save in list called 'matches'
matches = []
with open(f"{filename}", "r", encoding='utf-8', newline="\n") as html_file:
  for line in html_file:
    # 169 - complete matches
    link_ex = r"[h][t]{2}[p][s]?[:\/\/][^\" \',]+"
    # 170 - incomplete matches
    # link_ex = r"[h][t]{2}[p][:|/|-|.|?|=|0-9|@|#|_|a-z|A-Z]*[^ ]"
    link = re.findall(link_ex, line)
    if len(link) > 0:
      matches.append(link[0])
  html_file.close()
# Check matches, print results
if matches:
  print(f"Matches: {matches}\n\n")

# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'
answer_data = []
with open("answers.txt", "r") as csvfile:
  readCSV = csv.reader(csvfile, delimiter=",")
  for answers in readCSV:
    for index in answers:
      answer_data.append(index)
  csvfile.close()

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )