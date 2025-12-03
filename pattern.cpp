#include<bits/stdc++.h>
using namespace std;



void pattern(int n){
    int i,j;
    for(i=0;i<n;i++){
        
        for(j=0;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
int main(){
    int n;
    cin>>n;
    pattern(n);

    return 0;
}
