class longestPrefix
{
  static string commonPrefixUtil(String str1,String str2)
  {
    String result="";
    int n1=str1.length(),n2=Str2.length();
    fo(int i=0,j=0;i<=n1-1&&j<=n2-1;i++,j++)
    {
      if(str1.chaeAt(i) != str2.charAt(j))
      {
      break;
      }
      result +=str1.charAt(i);
    }
    return (result);
  }
  static String commonPrefix(String arr[],int n)
  {
    String prefix=arr[0];
    for(int i=1;i<=n-1;i++)
    {
    prefix=commonPrefixUtil(prefic,arr[i]);
    }
    return(prefix);
  }
  public static void main(String[] args)
  {
    String arr[] = {"Vishal","Vidharba"};
    int n = arr.length;
    String ans = commonPrefix(arr, n);
    if (ans.length()>0)
    {
      System.out.println("the longest common prefix is -%s",ans);
    }
    else
    {
    System.out.println("There is no common prefix");
    }
  }
}
    
