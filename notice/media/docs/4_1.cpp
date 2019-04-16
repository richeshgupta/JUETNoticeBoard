/*This program is written by Satyam Upadhyay-181B186*/
#include<iostream>
#include<limits>
#include<cstdio>
using namespace std;
static int hmarks,roll_hgh;
class db{
	int rno,s1,s2,s3;
	string name;
	public:
		friend void getd(db &);
		void pd();
		void hm();
		int tm();

};
void getd(db &a)
{
	cout<<"\nEnter roll number= ";
	cin>>a.rno;
	cout<<"\nEnter name= ";
	cin>>a.name;
	cout<<"\nEnter number of Subject 1= ";
	cin>>a.s1;
	cout<<"\nEnter number of subject 2= ";
	cin>>a.s2;
	cout<<"\nEnter number of subject 3= ";
	cin>>a.s3;
}
void db:: pd()
{
		int l = tm();
		cout<<"\nTotal number are= "<<l;
}
int db::tm()
{
	int r = s1+s2+s3;
	return r;
}

int main()
{
	int n;
	cout<<"Enter number of students= ";
	cin>> n;
	db a[n];
	int i;
	for(i=0;i<n;i++)
	{
		getd(a[i]);
		a[i].pd();
	}
	return 0;
}
