#include<bits/stdc++.h>
#define M 100
#define X 0
#define Y 1
#define G 1000
using namespace std;
double testcase[M][2];
double theta[G][2];
int g=0;
double f(int g,double x)
{
	return theta[g][1]*x+theta[g][0];
}
int main()
{
	freopen("testcase.txt","r",stdin);
	scanf("%*s");
	double xtemp,ytemp,alpha=0.007;
	int m;
	for(m=0;scanf("%lf%lf",&testcase[m][X],&testcase[m][Y])!=EOF;m++);
//	for(int i=0;i<m;i++)
//		printf("(%.0lf,%.0lf)\n",testcase[i][X],testcase[i][Y]);
	printf("Generation 0:theta0:%.6lf theta1:%.6lf\n",theta[0][0],theta[0][1]);
	for(g=1;g<G;g++)
	{
		double j0=0,j1=0,j=0;
		for(int i=0;i<m;i++)
		{
			j+=(f(g-1,testcase[i][X])-testcase[i][Y])*(f(g-1,testcase[i][X])-testcase[i][Y]);
			j0+=(f(g-1,testcase[i][X])-testcase[i][Y]);
			j1+=(f(g-1,testcase[i][X])-testcase[i][Y])*testcase[i][X];
		}
		j0/=m,j1/=m;
		printf("j0:%06.6lf j1:%06.6lf cost:%06.6lf ",j0,j1,j);
		theta[g][0]=theta[g-1][0]-alpha*j0;
		theta[g][1]=theta[g-1][1]-alpha*j1;
		printf("Generation %02d:theta0:%06.6lf theta1:%06.6lf\n",g,theta[g][0],theta[g][1]);
	}
}
