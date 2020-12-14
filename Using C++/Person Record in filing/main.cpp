
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Person
{
  int personID;
  string personName, personAddr; 

public:
  void setpersonID(int);
  void setpersonName(string);
  void setpersonAddr(string);

  int getpersonID();
  string getpersonName();
  string getpersonAddr();

  void input();       //take Person ID and Person Name 
  void writedata();   // write in file  
  void display();     //  display whole record of file on the screen. 
  void verify();      //  verify the existance of file. 
  void searchdata();  // search person record

};

void Person::setpersonID(int id)
{
  personID = id;
}

void Person::setpersonName(string name)
{
  personName = name;
}

void Person::setpersonAddr(string addr)
{
  personAddr = addr;
}

int Person::getpersonID()
{
   return personID; 
}

string Person::getpersonName()
{
  return personName;
}

string Person::getpersonAddr()
{
  return personAddr;
}

void Person::input()
{
  Person per;
  string name,addr;
  int id;

  cout<<"Enter name of person: ";
  getline(cin,name);
  cout<<"Enter id number of person: ";
  cin>>id;
  cout<<"Enter address of person: ";
  getline(cin,addr);

  per.setpersonName(name);
  per.setpersonID(id);
  per.setpersonAddr(addr);
        
}

void Person::writedata()
{
  Person per;
  string name,addr;
  int id;

  cout<<"Enter name of person: ";
  cin>>name;
  cout<<"Enter id of person: ";
  cin>>id;
  cout<<"Enter address of person: ";
  cin>>addr;

  per.setpersonName(name);
  per.setpersonAddr(addr);
  per.setpersonID(id);

  ofstream myfile;
  myfile.open("Data.txt", ios::app);

  if(!myfile)
  {
    cout<<"Error while opening file"<<endl;
  }

  else
    {
        // myfile<<per;
        myfile<<name;
        myfile<<id;
        myfile<<addr;
    }
    
  myfile.close();  

}

void Person::display()
{
  // display whole record 

  ifstream readfile;
  readfile.open("Data.txt",ios::in);

  if(!readfile)
  {
    cout<<"Error in opening file"<<endl;
  }

  else
  {
    while(!readfile.eof())
    {
      cout<< readfile.get();
    }

  }
  readfile.close();

}

void Person::verify()
{
  ifstream verify;
  verify.open("Data.txt",ios::in);

  if(verify)
  {
    cout<<"File exist"<<endl;
    verify.close();
  }

  else
  {
    cout<<"File not exist"<<endl;
  }

}

void Person::searchdata()
{
  int choice, id;
  string empName;
  Person p;

  cout<<"Enter 1 to search by name"<<endl;
  cout<<"Enter 2 to search by id"<<endl;
  cout<<"Enter your choice: ";
  cin>>choice;

  if(choice == 1)
  {
      cout<<"Enter name of employee: ";
      cin>>empName;

      ifstream check;
      check.open("Data.txt", ios::in);

      while(!check.eof())
      {
        if(check.read((char*)&p,sizeof(p)))
        {
          if(p.getpersonName() == empName)
          {
              cout<<"Record found"<<endl;
              cout<<"Name of employee is: "<<p.getpersonName()<<endl;
              cout<<"ID of employee is: "<<p.getpersonID()<<endl;
              cout<<"Address of employee is: "<<p.getpersonAddr()<<endl;;
          }

        }
        
      }
       check.close();
  }

  else if(choice == 2)
  {
      cout<<"Enter id number of employee: ";
      cin>>id;

      ifstream check;
      check.open("Data.txt", ios::in);

      while(!check.eof())
      {
        if(check.read((char*)&p,sizeof(p)))
        {
          if(p.getpersonID() == id)
          {
              cout<<"Record found"<<endl;
              cout<<"Name of employee is: "<<p.getpersonName()<<endl;
              cout<<"ID of employee is: "<<p.getpersonID()<<endl;
              cout<<"Address of employee is: "<<p.getpersonAddr()<<endl;;
          }

        }
        
      }
      check.close();
  }

  else
    cout<<"Invalid choice";

}

int menu()
{
  int choice;

  cout<<"\nEnter 1 for input() "<<endl;
  cout<<"Enter 2 for writedata() [write data in file]"<<endl;
  cout<<"Enter 3 for display() [display all record] "<<endl;
  cout<<"Enter 4 for verify() [verify whether file exist or not]"<<endl;
  cout<<"Enter 5 for searchdata() [search data of specific person]"<<endl;
  cout<<"Enter 6 to exit program\n"<<endl;
  cout<<"Enter your choice: ";
  cin>>choice;

  return choice;

}


int main()
{
  Person per;
  string name,addr;
  int id;

  while(true)
  {
    switch(menu())
    {
      case 1:
          per.input();
          break;

      case 2:
          per.writedata();
          break;

      case 3:
          per.display();
          break;

      case 4:
          per.verify();
          break;

      case 5:
          per.searchdata();
          break;

      case 6:
          exit(0);

      default:
          cout<<"Invalid choice"<<endl;
    }

  }
  


}







