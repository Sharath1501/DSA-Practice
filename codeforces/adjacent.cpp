#include<bits/stdc++.h>
#include<stdio
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int x,y;
        cin>>x>>y;
        int d = x-y+1;
        int a = (x-y+1)%9;
        if(d>=&&a==0) cout<<"YES"<<endl;
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;

}