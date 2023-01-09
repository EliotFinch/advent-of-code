#include <iostream>
#include <fstream>
using namespace std;

int main() {

    string input_text;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    // Use a while loop together with the getline() function to read the file line by line
    while (getline (MyReadFile, input_text)) {
    // Output the text from the file
    cout << input_text;
    }

    // Close the file
    MyReadFile.close();

}

