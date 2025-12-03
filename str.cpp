#include <bits/stdc++.h>
using namespace std;

int main() {
    int num;
    cin >> num;
    if(num ==1){
            cout<<1<<endl;
            return 0;
    }
    if(num == 2){
            cout<<1<<endl;
            return 0;
    }
    int f[num+1];
    f[0]=1;
    f[1]=1;
    for(int i=2;i<=num;i++){
            f[i]= f[i-1]+f[i-2];
            
    }
    for(int i=0;i<sizeof(num);i++)
    cout<<f[i]<<endl;
    cout<<"Final answer"<<endl;
    cout<<f[num-1]<<endl;
    return 0;
}
