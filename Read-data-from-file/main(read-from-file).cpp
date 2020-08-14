#include <iostream>
#include <fstream>
using namespace  std;

int main()
{

  int A[10];

  ifstream inData;

  inData.open("example.txt");

  if(!inData)
  {
    cout<<"File not open "<<endl;
    exit(0);
  }

for(int i=0;i<10;i++)
{
  inData>>A[i];
}

for (int j=0;j<10;j++)
    cout<<A[j]<<endl;
  
  
}