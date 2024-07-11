import java.util.Scanner;

public class BankBalance{

	public static void main(String[] args ){
		Scanner input = new Scanner(System.in);
		
		int deposit = 0;
		int withdraw = 0;
		int user = 0;
		int balance = 0;
		
		System.out.println("Enter amount to deposit");
		balance = input.nextInt();		

		while (user != -1){

			System.out.println("Enter 1 to deposit or enter 2 to withdraw or enter 3 to check balance or enter 0 to exit:");
			user = input.nextInt(); 
	
			if(user == 1){
				System.out.println("enter the amount to deposit:");
				deposit = input.nextInt();
				if (deposit < 0){
					System.out.println("invalid"); 
				}
				else{
					balance += deposit;
				}
			}
			else
			if(user == 2){
				System.out.println("Enter the amount to withdraw: ");
				withdraw = input.nextInt();
				if (withdraw > balance){
					System.out.println("invalid");
				}
				else {
					balance -= withdraw;
			}	}
			else
			if(user == 3){
				System.out.println(balance);
								
			
			}
			
		}


	}






}