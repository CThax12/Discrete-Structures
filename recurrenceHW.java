package recurrence;

import java.util.ArrayList;

public class recurrenceHW {

	public static void main(String[] args) {
		problemA();
		problemB();
		problemC();
		problemD();
		problemE();
	}
	
	private static void problemE() {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(1);
		nums.add(2);
		nums.add(0);
		
		
		for (int i = 3; i <= 4; ++i) {
			nums.add(nums.get(i-1) + nums.get(i - 3));
		}
		System.out.println("Problem E:");

		for (Integer num: nums) {
			System.out.println(num);
		}
	}
	
	private static void problemD() {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(1);
		nums.add(1);
		
		for (int i = 2; i <= 4; ++i) {
			nums.add((int) (i*nums.get(i-1) + (Math.pow(i, 2) * nums.get(i - 2))));
		}
		System.out.println("Problem D:");

		for (Integer num: nums) {
			System.out.println(num);
		}
	}

	private static void problemC() {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(1);
		nums.add(2);
		
		for (int i = 2; i <= 4; ++i) {
			nums.add(nums.get(i-1) + (3 * nums.get(i-2)));
		}
		System.out.println("Problem C:");

		for (Integer num: nums) {
			System.out.println(num);
		}
	}
	
	private static void problemB() {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(2);
		
		for (int i = 1; i <= 4; ++i) {
			nums.add((int) Math.pow(nums.get(i-1), 2));
		}
		System.out.println("Problem B:");

		for (Integer num: nums) {
			System.out.println(num);
		}
	}

	private static void problemA() {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(2);
		
		for (int i = 1; i <= 4; ++i) {
			nums.add((6*nums.get(i-1)));
		}
		System.out.println("Problem A:");
		for (Integer num: nums) {
			System.out.println(num);
		}
	
		
	}

}
