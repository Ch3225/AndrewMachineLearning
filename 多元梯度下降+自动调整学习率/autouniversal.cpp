#include<bits/stdc++.h>
#include<string>
#define GENERATION 5000
#define G GENERATION 
using namespace std;
int M,N;
double **testcase,**theta;
double learningrate; 
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
	learningrate=10000;
	freopen("reginalresult,autoresetlearningrate.txt","w",stdout);
	printf("Now learning rate:%.6lf\n",learningrate);
	double *cost=new double[G];
	int lock=10;
	for(int g=1;g<G;g++){
		double *forecast=new double[N+1];
		for(int i=0;i<=N;i++)
			forecast[i]=0;
		for(int i=0;i<M;i++){
			double temp=f(g-1,i);
			forecast[0]+=temp;
			cost[g-1]+=pow(temp-testcase[i][0],2);
			for(int j=1;j<=N;j++){
				forecast[j]+=(temp-testcase[i][0])*testcase[i][j];
			}
		}
		for(int i=0;i<=N;i++){
			theta[g][i]=theta[g-1][i]-learningrate*forecast[i];
		}
		if(g>1&&(cost[g-1]>cost[g-2]||cost[g-1]>1e20)){
			if(lock>0){
				printf("Error:\n");
				printf("cost[%d]:%.6lf\n",g-1,cost[g-1]);
				printf("cost[%d]:%.6lf\n",g-2,cost[g-2]);
				lock--;
			}
			else{
				learningrate*=0.7;
				lock=10;
				for(int i=0;i<G;i++)
					cost[i]=0;
				printf("-----------------failed in generation:%d------------------\n",g);
				g=0;
				printf("Now learning rate:%.6lf\n",learningrate);
			}
			continue;
		}
		printf("Generation %02d:{\n",g);
		printf("Cost:%.6lf\n",cost[g-1]);
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
