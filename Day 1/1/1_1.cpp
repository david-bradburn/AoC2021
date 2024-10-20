/////////////////////////////////////////////////////////////////
////// https://adventofcode.com/2021/day/1 ///////////////////////
/////////////////////////////////////////////////////////////////

#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>
using namespace std;
namespace fs = std::filesystem;


// Need to rethink how we read the file in C++

string open_file(string file_path) {
  std::ifstream myfile (file_path);

  string mystring;
  if ( myfile.is_open() ) { // always check whether the file is open
    myfile >> mystring; // pipe file's content into stream
    cout << mystring;
  }
  return mystring;
}


int main() {
  string file = "input.txt";
  string DAY_NO = "1";
  string PART = "1";

  string file_path_base = "../misc/" + file;
  cout << "Current path is " << fs::current_path() << '\n';
  open_file(file_path_base);

  // cout << "Hello World!";
  return 0;
}