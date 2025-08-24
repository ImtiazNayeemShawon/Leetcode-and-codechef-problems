#include <iostream>
#include <string>

using namespace std;

class Teacher{
string name;
string dept;
string subject;
double salary;

void changeDept(string newdept){
    dept = newdept;
};
};

int main(){
Teacher t1;

return 0;
}