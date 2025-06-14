#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string s1 = "9999999991";
    stringstream stream;
    stream << s1;
    int num;
    stream >> num;
    cout << num;
}