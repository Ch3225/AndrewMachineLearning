#include<bits/stdc++.h>
#include<string>
using namespace std;
int M,N;
double **X,*y,*theta,**XT;
void preset();
double **newrec(int m,int n);
double **re(double **origin);
double **tr(double **origin);
double **mul(double **origin1,double **origin2);
int main(){
	freopen("testcaseforreginal.txt","r",stdin);
	scanf("%*s");
	scanf("%d%d",&M,&N);
	preset();
	//TODO
	return 0;
}
void preset(){
	X=newrec(M,N+1);
	y=new double[M]();
	theta=new double[N+1]();
}
double** newrec(int m,int n){
	double **tmp=new double*[m];
	for(int i=0;i<m;i++){
		tmp[i]=new double[n]();
	}
	return tmp;
}
double** re(double **origin){
	//TODO
}
double** tr(double **origin){
	//TODO
}
double** mul(double **origin1,double **origin2){
	//TODO
}
