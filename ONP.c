#include<stdio.h>
int getPre(char x)
{
 switch(x)
 {
 case '^': return 4;
 case '*':
 case '/': return 3;
 case '+':
 case '-': return 2;
 case '(': return 1;
 }
 return 0;
}
main()
{
 int N, i=-1,s_ptr=-1,o_ptr=-1;
 char expr[403];
 char out[403]={0};
 char stack[300]={0};
 scanf("%d%*c",&N);
 while(N)
 {
 o_ptr=s_ptr=-1;
 scanf("%s", expr);
 for(i=0;expr[i]!='\0'; i++)
 {

 if(expr[i]=='(')
 {
 s_ptr++;
 stack[s_ptr]='(';
 }
 else if(expr[i]==')')
 {
 while(stack[s_ptr]!='(')
 {
 o_ptr++;
 out[o_ptr]=stack[s_ptr];
 s_ptr--;
 }
 s_ptr--;
 }
 else if(expr[i]=='+' || expr[i]=='-' || expr[i]=='/' || expr[i]=='*' || expr[i]=='^')
 {
 while(getPre(stack[s_ptr])>=getPre(expr[i]))
 {
 o_ptr++;
 out[o_ptr]=stack[s_ptr];
 s_ptr--;
 }
 s_ptr++;
 stack[s_ptr]=expr[i];
 }
 else
 {
 o_ptr++;
 out[o_ptr]=expr[i];
 }
 }
 out[o_ptr+1]='\0';
 printf("%s\n",out);
 N--;
 }
 return 0;
}
