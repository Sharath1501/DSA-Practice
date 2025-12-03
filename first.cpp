#include <iostream>

int r = 2;

void area();
class myclass{
public:
int a;
void display(){
    std::cout<<"inside class"<<std::endl;
}
};
int main(){
    myclass m;
    m.a  =90;
    m.display();
    area();
    std::cout<<"Hello world from main secction"<<std::endl;
    std::cout<<m.a<<std::endl;
    return 0;
}
#define PI 3.14
void area(){
    
    float area;
    area = PI*r*r;
    std::cout<<area<<std::endl;
}
