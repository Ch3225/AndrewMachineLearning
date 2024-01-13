#include<bits/stdc++.h>
#define M 100
#define X1 1
#define X2 2
#define Y 0
#define G 10000
using namespace std;
double testcase[M][3];
double theta[G][3];
int g=0;
double f(int g,double x1,double x2)
{
	return theta[g][1]*x1+theta[g][2]*x2+theta[g][0];
}
int main()
{
	freopen("testcase.txt","r",stdin);
	scanf("%*s");
	double x1temp,x2temp,ytemp,alpha=0.002;
	int m;
	for(m=0;scanf("%lf%lf%lf",&testcase[m][X1],&testcase[m][X2],&testcase[m][Y])!=EOF;m++);
	printf("Generation 0:theta0:%.6lf theta1:%.6lf theta2:%.6lf\n",theta[0][0],theta[0][1],theta[0][2]);
	for(g=1;g<G;g++)
	{
		double j=0,j0=0,j1=0,j2=0;
		for(int i=0;i<m;i++)
		{
			j+=(f(g-1,testcase[i][X1],testcase[i][X2])-testcase[i][Y])*(f(g-1,testcase[i][X1],testcase[i][X2])-testcase[i][Y]);
			j0+=(f(g-1,testcase[i][X1],testcase[i][X2])-testcase[i][Y]);
			j1+=(f(g-1,testcase[i][X1],testcase[i][X2])-testcase[i][Y])*testcase[i][X1];
			j2+=(f(g-1,testcase[i][X1],testcase[i][X2])-testcase[i][Y])*testcase[i][X2];
		}
		j0/=m,j1/=m,j2/=m;
		printf("j0:%06.6lf j1:%06.6lf j2:%06.6lf cost:%06.6lf\n",j0,j1,j2,j);
		theta[g][0]=theta[g-1][0]-alpha*j0;
		theta[g][1]=theta[g-1][1]-alpha*j1;
		theta[g][2]=theta[g-1][2]-alpha*j2;
		printf("Generation %02d:theta0:%06.6lf theta1:%06.6lf theta2:%06.6lf\n",g,theta[g][0],theta[g][1],theta[g][2]);
	}
}
