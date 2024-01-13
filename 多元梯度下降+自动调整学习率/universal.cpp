#include<bits/stdc++.h>
#include<string>
#define LEARNINGRATE 0.0002
#define GENERATION 5000
#define G GENERATION 
using namespace std;
int M,N;
double **testcase,**theta;
double f(int g,int r);
void preset();
int main(){
	freopen("testcaseforreginal.txt","r",stdin);
	scanf("%*s");
	scanf("%d%d",&M,&N);
	preset();
	for(int i=0;i<M;i++){
		for(int j=1;j<=N;j++){
			scanf("%lf",&testcase[i][j]);
		}
		scanf("%lf",&testcase[i][0]);
	}
	freopen("reginalresult.txt","w",stdout);		
	for(int g=1;g<G;g++){
		double *derivative=new double[N+1];
		double cost=0;
		for(int i=0;i<=N;i++)
			derivative[i]=0;
		for(int i=0;i<M;i++){
			derivative[0]=f(g-1,i);
			cost+=pow(derivative[0]-testcase[i][0],2);
			for(int j=1;j<=N;j++){
				derivative[j]+=(derivative[0]-testcase[i][0])*testcase[i][j];
			}
		}
		for(int i=0;i<=N;i++){
			theta[g][i]=theta[g-1][i]-LEARNINGRATE*derivative[i];
		}
		printf("Generation %02d:{\n",g);
		printf("Cost:%.6lf\n",cost);
		for(int i=0;i<=N;i++){
			printf("theta%02d:%.6lf\n",i,theta[g][i]); 
		}
		printf("}\n");
	}
	return 0;
}
double f(int g,int r){							//Cost-Function
	double ans=theta[g][0];
	for(int i=1;i<=N;i++)
		ans+=theta[g][i]*testcase[r][i];
	return ans;
}
void preset(){
	testcase=new double*[M];
	for(int i=0;i<M;i++){
		testcase[i]=new double[N+1]();
	}
	theta=new double*[G];
	for(int i=0;i<G;i++){
		theta[i]=new double[N+1]();
	}
}
