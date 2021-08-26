package exam1;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;


public class GuessTheNumber {
	
	static Random rand = new Random();

	public static void main(String[] args) {
		System.out.println("This is a game to guess the 5th number of a sequence.\n"
				+ "You are given 4 numbers with a random sequence.\n"
				+ "The program will give you the rule and tell \nyou if you were "
				+ "correct or not at the end.");
		
		int rule =(rand.nextInt(4)+1);

		Scanner scan = new Scanner(System.in);
		int userGuess = 0;
		int correctAnswer = 0;

		if(rule == 1) {
			correctAnswer = Arithmetic();
			System.out.println("What is the next number in this sequence?");
			userGuess = scan.nextInt();
			
			if (userGuess == correctAnswer) System.out.println("Good job!\nThis was an arithmetic sequence.");
			else System.out.println("Nope, the correct answer is: " + correctAnswer + "\n This was an arithmetic sequence.");
			
			
		}
		
		if(rule == 2) {
			correctAnswer = Geometric();
			System.out.println("What is the next number in this sequence?");
			userGuess = scan.nextInt();
			
			if (userGuess == correctAnswer) System.out.println("Good job!\n This was a geometric sequence.");
			else System.out.println("Nope, the correct answer is: " + correctAnswer + "\n This was a geometric sequence.");
		}
		
		if(rule == 3) {
			correctAnswer = Fibonacci();
			System.out.println("What is the next number in this sequence?");
			userGuess = scan.nextInt();
			
			if (userGuess == correctAnswer) System.out.println("Good job!\n This was a fibonacci sequence.");
			else System.out.println("Nope, the correct answer is: " + correctAnswer + "\n This was a fibonacci sequence.");
		}
		
		if(rule == 4) {
			correctAnswer = Double();
			System.out.println("What is the next number in this sequence?");
			userGuess = scan.nextInt();
			
			if (userGuess == correctAnswer) System.out.println("Good job!\n This is a sequence to double each number.");
			else System.out.println("Nope, the correct answer is: " + correctAnswer + "\n This is a sequence to double each number.");
		}
		
		
		

	}

	private static Integer Double() {
		int firstNumber = rand.nextInt(20) + 1;
		
		
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(firstNumber);
		for (int i = 1; i <= 4; ++i) {
			nums.add(nums.get(i-1) * 2);
			
			if (i != 5) {
				System.out.println(nums.get(i-1));
			}
		}
		
		return nums.get(4);
	}

	private static Integer Fibonacci() {
		int firstNumber = rand.nextInt(10) + 1;
		int secondNumber = firstNumber;
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(firstNumber);
		nums.add(secondNumber);
		for (int i = 2; i <= 4; ++i) {
			nums.add(nums.get(i-2) + nums.get(i-1));
		}
		for (int i = 0; i < 4; ++i) {
			System.out.println(nums.get(i));
		}
		
		return nums.get(4);
	}

	private static Integer Geometric() {
		int firstNumber = rand.nextInt(10) + 1;
		int ratio = rand.nextInt(5) + 1;
		
		ArrayList<Integer> nums = new ArrayList<Integer>();
		
		for (int i = 0; i <= 4; ++i) {
			nums.add((int) (firstNumber * Math.pow(ratio, i)));
			
			if (i != 4) {
				System.out.println(nums.get(i));
			}
		}
		
		return nums.get(4);
		
	}

	private static Integer Arithmetic() {
		int firstNumber = rand.nextInt(20) + 1;
		int addedNumber = rand.nextInt(10) + 1;
		
		ArrayList<Integer> nums = new ArrayList<Integer>();
		
		for (int i = 0; i <= 4; ++i) {
			nums.add(firstNumber + addedNumber * i);
			
			if (i != 4) {
				System.out.println(nums.get(i));
			}
		}
		
		return nums.get(4);
		
	}

}
