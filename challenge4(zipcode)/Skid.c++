#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isZip(int zipp){
    string zip = to_string(zipp);
    int cnt = 0;
    int y = zip.size();
    for(int x=0;x<y;x++){
        if(!isdigit(zip[x])){
            cnt++;
        }
        
    }
    if(y != 5 || !cnt ==0){
        return false;
    }
    else for(int j=0;j<y;j++){
            if(zip[j]==zip[j+2]||zip[j]==zip[j+1]){
                return false;
                break;
            }
            else if(zip[j]!=zip[j+2]||zip[j]!=zip[j+1]){
                    j++;
                    if(j==y){
                        return true;
                    }
                }      
    }
    return 0;
}
void validate(int num){
    if(isZip(num)==1){
        cout<<"True"<<endl;
    }
    else{
        cout<<"False"<<endl;
    }
}
int main() {
    validate(11789);
    validate(10178);
    validate(12314);
    return 0;
}