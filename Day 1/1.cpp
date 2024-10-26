/////////////////////////////////////////////////////////////////
////// https://adventofcode.com/2021/day/1 //////////////////////
/////////////////////////////////////////////////////////////////

#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
namespace fs = std::filesystem;


vector<string> open_file_and_read(string file_path) {
  std::ifstream inputFile (file_path);

  vector<string> data;
  string tempStr;
  if ( inputFile.is_open() ) { // always check whether the file is open
    while (inputFile) {
      std::getline(inputFile, tempStr);
      // inputFile >> tempStr; // pipe file's content into stream
      data.push_back(tempStr);
    }
  } else {
    string errorMsg = "Couldn't open file" + file_path;
    cout << errorMsg << endl;
  }
  return data;
}

template <typename ele_typeV>
void printVector (const vector<ele_typeV> &V) {
  for (auto itr = V.cbegin(); itr != V.cend(); itr++) {
   cout << *itr << '\n';
  }
}

vector<int> turnInputStrToInt (vector<string> ip) {
  vector<int> op;
  for (string item : ip) {
    op.push_back(stoi(item));
  }
  return op;
}

void p1 (vector<int> data) {
  int increaseCount = 0;
  int lastValue = 999999;
  for (const int& i : data) {
    if (lastValue < i) {
      increaseCount++;
    }
    lastValue = i;
  }
  cout << increaseCount << endl;
} //1722

void p2 (vector<int> data) {
  int increaseCount = 0;
  int lastValue = 999999;
  int runningValue = 0;

  for (int index = 0; index < data.size(); index++) {
    if (index < 3) {
      runningValue += data[index];
    } 
    else {
      runningValue = runningValue + data[index] - data[index-3];
      if (lastValue < runningValue) {
        increaseCount++;
      }
    }
    lastValue = runningValue;
  }
  cout << increaseCount << endl;

} //1748


int main() {
  string file = "input.txt";
  string DAY_NO = "1";
  string PART = "1";

  string file_path_base = "misc/" + file;
  cout << "Current path is " << fs::current_path() << '\n'; // Just for debug

  vector<int> dataInt = turnInputStrToInt(open_file_and_read(file_path_base));

  p1(dataInt);
  p2(dataInt);

  return 0;
}