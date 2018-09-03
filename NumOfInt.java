import java.io.*;
import java.util.*;
class NumOfInt
{
public static void main(String[] args)
{
int a=0;
Scanner sc= new Scanner(System.in);
int b=sc.nextInt();
while(b!=0)
{
b=b/10;
a++;
}
System.out.println(a);
}
}
