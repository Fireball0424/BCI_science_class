#include <iostream>
using namespace std;

int main(){
    //input / output optimization
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // switch the statement
    char input;
    bool flag = false; // default open eyes
    while(true){
        cin >> input;
        if(input == 's') flag ^= true;

        if(flag){
            cout << "-----------------closed-------------------" << endl;
        }else{
            cout << "-----------------opened-------------------" << endl;
        }
    }
}