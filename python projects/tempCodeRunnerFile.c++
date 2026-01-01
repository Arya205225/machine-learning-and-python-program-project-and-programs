#include <iostream>
using namespace std;

class testResult{
    private:
    int rollno,right,wrong,net_score;
    
    static int right_weightage,wrong_weightage;
    public:
    void setRollno(int r){ rollno=r;}
    void setRight(int ri){ right=ri;}
    void setWrong(int w){wrong=w;}
    void setNetscore(int ns){net_score=ns;}
    int getRollno(){return rollno;}
    int getRight(){return right;}
    int getWrong(){return wrong;}
    int getnet_score(){return net_score;}
    static void setRight_weightage(int rw){right_weightage=rw;}
    static void setWrong_weightage(int ww){wrong_weightage=ww;}
    static int getRight_weightage(){return right_weightage;}
    static int getWrong_weightage(){return wrong_weightage;}
};


int testResult::right_weightage=3;
int testResult::wrong_weightage=1;


void setTestResult(testResult &tr,int roll,int rig,int wro)
{
    tr.setRollno(roll);
    tr.setRight(rig);
    tr.setWrong(wro);
    
    tr.setNetscore(rig*tr.getRight_weightage()-wro*tr.getWrong_weightage());
}

void printTestResult(testResult tr)
{
   
    cout<<"\n"<<tr.getRollno()<<" "<<tr.getRight()<<" "<<tr.getWrong()<<" "<<tr.getnet_score();
}


void sorttestResult(testResult tr[],int size)
{
    int r,i;
    testResult temp;
    for(r=1;r<=size-1;r++)
    {
        for(i=0;i<=size-1-r;i++)
        {
          
            if(tr[i].getnet_score()>tr[i+1].getnet_score())
            {
                
                temp=tr[i];
                tr[i]=tr[i+1];
                tr[i+1]=temp;
            }
        }
    }
}

int main()
{
    testResult result[5];
    int i;
    
    
    setTestResult(result[0],100,50,10); 
    setTestResult(result[1],101,50,4);  
    setTestResult(result[2],102,50,30); 
    setTestResult(result[3],103,50,10); 
    setTestResult(result[4],104,50,11); 
    
    cout << "--- Initial Results ---";
    for(i=0;i<=4;i++)
        printTestResult(result[i]);
    sorttestResult(result,5);
    
    cout << "\n\n--- Sorted Results (by Net Score) ---";
    for(i=0;i<=4;i++)
        printTestResult(result[i]);
        
    return 0;
}