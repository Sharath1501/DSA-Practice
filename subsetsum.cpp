#include<iostream>
using namespace std;
int i,j;
bool subset(int set[],int n,int sum){
    bool dp[n+1][sum+1];
    for(i=0;i<=n;i++)
    dp[i][0]=true;
    for(j=0;j<=n;j++)
    dp[0][j]=false;

    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            if(set[i-1]<=j){
                dp[i][j]=dp[i-1][j]||dp[i-1][j-set[i-1]];
            }
            else
            dp[i][j]=dp[i-1][j];
        }
    }
    cout<<sum<<endl;
    
}
int main(){
    int set[]={3,4,5,3,2,3};
    int sum =8;
    int n=sizeof(set)/sizeof(set[0]);
    if(subset(set,n,sum))
    cout<<"Found subset"<<endl;
    else
    cout<<"Not Found";

}