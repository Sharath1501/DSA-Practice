#include<iostream>
#include<iomanip>
#include<limits>
#include<limits.h>
using namespace std;
long int a= 12000;
int main(){
    
    cout<<setprecision(15);
    cout<<"Size of long int"<<sizeof(long int)<<endl;
    double e = 4.1234567891012879;
    cout<<"printing..."<<e<<endl;
    cout<<numeric_limits<long double>::digits10<<endl;
    char ch =128;
    cout<<(int)ch<<endl;
    wchar_t chi =L'f';
    if((chi == 116)==true)
    cout<<"nanu nandini"<<endl;
    cout<<chi<<endl;

    bool b = true;
    cout<<b<<endl;
    
    void *ptr;
    int x = 10;
    bool p =45;
    ptr = &x;
    cout<<*(int*)ptr<<endl;
    cout<<p<<endl;
    return 0;
}