#include<iostream>
using std::cout;
using std::endl;

int count(int,int);
void setchessboard();
int findmin();
int findminadd();
int putqueen(int,int,int,int);
int setblock(int,int);
void printchessboard();
void removequeen(int,int);
void resetchessboard();
int chessboard[8][8];
int countsolnumber=1;

int main()
{
     resetchessboard();
     int x1,x2,x3,x4,x5,x6,x7,x8;
     int y1,y2,y3,y4,y5,y6,y7,y8;
     int z1,z2,z3,z4,z5,z6,z7,z8;
     for(x1=0;x1<=7;x1++)
      for(y1=0;y1<=7;y1++)
       {z1=putqueen(x1,y1,0,0);
        if(z1==2)
         {for(x2=0;x2<=7;x2++)
           for(y2=0;y2<=7;y2++)
            {z2=putqueen(x2,y2,x1,y1);
              if(z2==2)
               {for(x3=0;x3<=7;x3++)
                 for(y3=0;y3<=7;y3++)
                  {z3=putqueen(x3,y3,x2,y2);
                   if(z3==2)
                    {for(x4=0;x4<=7;x4++)
                      for(y4=0;y4<=7;y4++)
                       {z4=putqueen(x4,y4,x3,y3);
                         if(z4==2)
                          {for(x5=0;x5<=7;x5++)
                            for(y5=0;y5<=7;y5++)
                             {z5=putqueen(x5,y5,x4,y4);
                               if(z5==2)
                                {for(x6=0;x6<=7;x6++)
                                  for(y6=0;y6<=7;y6++)
                                   {z6=putqueen(x6,y6,x5,y5);
                                     if(z6==2)
                                      {for(x7=0;x7<=7;x7++)
                                        for(y7=0;y7<=7;y7++)
                                         {z7=putqueen(x7,y7,x6,y6);
                                           if(z7==2)
                                            {for(x8=0;x8<=7;x8++)
                                              for(y8=0;y8<=7;y8++)
                                               {z8=putqueen(x8,y8,x7,y7);
                                                 if(z8==3)
                                                  continue;
                                                 else
                                                  continue;
                                               }
                                            }
                                           else
                                            continue;}
                                      }
                                     else
                                      continue;}
                                }
                               else
                                continue;}
                          }
                         else
                          continue;}
                    }
                   else
                    continue;}
               }
              else
               continue;}
         }
        else
         continue;}


    getchar();
    return 0;
}

int count(int i,int j)
{
    int a,b,c=0,d;
    for(a=0;a<=7;a++)
      for(b=0;b<=7;b++)
      {
        for(d=1;d<=8;d++)

{if((chessboard[a][b]!=1)&&(chessboard[a][b]!=100)&&(a==i-d)&&(b==j-d))
            c+=1;
           else
if((chessboard[a][b]!=1)&&(chessboard[a][b]!=100)&&(a==i+d)&&(b==j-d))
            c+=1;
           else
if((chessboard[a][b]!=1)&&(chessboard[a][b]!=100)&&(a==i-d)&&(b==j+d))
            c+=1;
           else
if((chessboard[a][b]!=1)&&(chessboard[a][b]!=100)&&(a==i+d)&&(b==j+d))
            c+=1;
           else
            continue;
          }
        if((chessboard[a][b]!=1)&&(chessboard[a][b]!=100)&&((a==i)||(b==j)))
          c+=1;
        else
         continue;
      }

      return c;
}


int findmin()
{
    int e,f,min=1000;
     for(e=0;e<=7;e++)
      for(f=0;f<=7;f++)

{if((chessboard[e][f]!=1)&&(chessboard[e][f]!=0)&&(chessboard[e][f]<min))
        min=chessboard[e][f];
       else
        continue;
       }

    if(min==1000)
     return -1;
    else
     return min;
}

int findminadd()
{
    int g,h,k=0;
    if(findmin()!=-1)
     {for(g=0;g<=7;g++)
       for(h=0;h<=7;h++)
        {if(chessboard[g][h]==findmin())
           k+=1;
         else
          continue;
        }
      return k;
      }
    else
      return -1;
}

int setblock(int s1,int s2)
{
    int sb1,sb2,sb3;
    for(sb1=0;sb1<=7;sb1++)
     for(sb2=0;sb2<=7;sb2++)
      {if(chessboard[sb1][sb2]!=100)
        {chessboard[s1][sb2]=1;
         chessboard[sb1][s2]=1;}
        for(sb3=1;sb3<=8;sb3++)
         {
          if(((sb1-sb3)>=0)&&((sb2-sb3)>=0))
             chessboard[(sb1-sb3)][(sb2-sb3)]=1;
          else if(((sb1+sb3)<=7)&&((sb2-sb3)>=0))
             chessboard[(sb1+sb3)][(sb2-sb3)]=1;
          else if(((sb1-sb3)>=0)&&((sb2+sb3)<=7))
             chessboard[(sb1-sb3)][(sb2+sb3)]=1;
          else if(((sb1+sb3)<=7)&&((sb2+sb3)<=7))
             chessboard[(sb1+sb3)][(sb2+sb3)]=1;
          else
            continue;
         }
      }
     return 0;
}

int putqueen(int pq1,int pq2,int pq3,int pq4)
{
    static int queen=0;
    int k=findminadd();
      if((k>=(8-queen))&&(queen<8))
       { chessboard[pq1][pq2]=100;
         setblock(pq1,pq2);
         queen+=1;
         return 2;}
      if(queen==8)
       {printchessboard();
        countsolnumber+=1;
        queen=0;
        return 3;}
      if((k<queen)&&(queen!=8))
       { removequeen(pq3,pq4);
         queen-=1;
        return 4;}


}

void removequeen(int rq1,int rq2)
{
   chessboard[rq1][rq2]=0;
   int m,n,o;
    for(m=0;m<=7;m++)
     for(n=0;n<=7;n++)
      {  chessboard[rq1][m]=0;
         chessboard[n][rq2]=0;
        for(o=1;o<=8;o++)
         {
           if(((rq1-o)>=0)&&((rq2-o)>=0))
             chessboard[(rq1-o)][(rq2-o)]=0;
           else if(((rq1+o)<=7)&&((rq2-o)>=0))
             chessboard[(rq1+o)][(rq2-o)]=0;
           else if(((rq1-o)>=0)&&((rq2+o)<=7))
             chessboard[(rq1-o)][(rq2+o)]=0;
           else if(((rq1+o)<=7)&&((rq2+o)<=7))
             chessboard[(rq1+o)][(rq2+o)]=0;
           else
            continue;
         }
      }
       setchessboard();


}
void printchessboard()
{
    cout<<"--"<<endl;
    cout<<"第"<<countsolnumber<<"組解\n\n";
    cout<<"皇后的位置\n"<<"1.以坐標表示為:"<<endl;
     int p0,p1,p2,p3;
     for(p1=0;p1<=7;p1++)
      for(p2=0;p2<=7;p2++)
      {
        if(chessboard[p1][p2]==100)
         cout<<"<"<<p1<<","<<p2<<">\t";
      }
     cout<<endl;
     cout<<"2.以圖形表示:"<<endl;
     cout<<"  ";
     for(p0=0;p0<=7;p0++)
      {cout<<p0<<" ";
      }
     cout<<endl;
     for(p1=0;p1<=7;p1++)
      for(p2=0;p2<=7;p2++)
      {
       if((p2==0)&&(p2!=7)&&(chessboard[p1][7]!=100))
        cout<<p1<<"  ";
       else if(((p2==0)&&p2!=7)&&(chessboard[p1][7]==100))
        cout<<p1<<" Q ";
       else if ((p2!=0)&&(p2==7)&&(chessboard[p1][7]!=100))
        cout<<"  "<<endl;
       else if ((p2!=0)&&(p2==7)&&(chessboard[p1][7]==100))
        cout<<"Q"<<endl;
       else if ((p2!=0)&&(p2!=7)&&(chessboard[p1][7]==100))
        cout<<"Q ";
       else
        cout<<" ";
      }
}

void resetchessboard()
{
    int re1,re2;
     for(re1=0;re1<=7;re1++)
      for(re2=0;re2<=7;re2++)
       {chessboard[re1][re2]=0;
       }

    setchessboard();
}

void setchessboard()
{
   int set1,set2;
     for(set1=0;set1<=7;set1++)
      for(set2=0;set2<=7;set2++)
       {chessboard[set1][set2]=count(set1,set2);
       }
}
