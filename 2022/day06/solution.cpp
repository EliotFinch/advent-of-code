#include <fstream>
#include <string>
#include <iostream>
#include <set>

int main()
{
  std::ifstream input("input.txt");

  // Read the first line from the file
  std::string data;
  std::getline(input, data);

  input.close();

  int distinct_chars = 14;

  // Iterate through the characters in the string
  for (int i = 0; i < (data.length()-(distinct_chars-1)); i++) {

    // Extract a substring from the string
    std::string subString = data.substr(i, distinct_chars);

    // Create a set to store the unique characters
    std::set<char> uniqueChars;

    // Iterate through the characters in the substring
    for (int j = 0; j < subString.length(); j++) {
        // Add the current character to the set
        uniqueChars.insert(subString[j]);
    }

    // Get the number of elements in the set
    unsigned int numElements = uniqueChars.size();

    if (numElements == distinct_chars) {
        std::cout << i + distinct_chars << std::endl;
        break;
    }
    
  }
}