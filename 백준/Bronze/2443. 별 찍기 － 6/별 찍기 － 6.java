import java.util.*;
class Main {
    public static void main(String[] args) {
       		 Scanner sc = new Scanner(System.in);
      		 int s = sc.nextInt();
		//int s =5;
		 for(int i = 0;i<s;i++){//layer
			 for(int k = s-i+1; k <= s; k++) {//blank
				 System.out.print(" ");
			 }
			 
			 for(int j = 0;  j < 2*(s-i)-1; j++){//star
				 System.out.print("*");   
			 
             }
			 System.out.println();
		}
    }
}