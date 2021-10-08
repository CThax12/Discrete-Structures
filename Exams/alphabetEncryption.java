import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class alphabetEncryption {
    static ArrayList<Character> letters = new ArrayList<Character>();
    public static void main(String[] args) {
        String alpha = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i < alpha.length(); ++i) {
            letters.add(alpha.charAt(i));
        }
        
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number to choose what to do. \n"
                + "1: Encrypt \n"
                + "2: Decrypt \n"
                + "3: Quit");
        int choice = scan.nextInt();
        boolean stop = false;
        
        while(stop == false) {
            

            if (choice == 1) {
                System.out.println("Enter phrase to encrypt.");
                scan.nextLine();
                String word = scan.nextLine();
                System.out.println("What is p?");
                int p = scan.nextInt();
                System.out.println("What number to add?");
                int add = scan.nextInt();
                encrypt(word.toLowerCase(), p, add);
                
                System.out.println("Enter a number to choose what to do. \n"
                        + "1: Encrypt \n"
                        + "2: Decrypt \n"
                        + "3: Quit");
                choice = scan.nextInt();
            }
            
            if (choice == 2) {
                System.out.println("Enter phrase to decrypt.");
                scan.nextLine();
                String word = scan.nextLine();
                decrypt(word.toLowerCase());

                System.out.println("Enter a number to choose what to do. \n"
                        + "1: Encrypt \n"
                        + "2: Decrypt \n"
                        + "3: Quit");
                choice = scan.nextInt();
            }
            
            if (choice == 3) {
                stop = true;
            }
            

        }
        
        
        
    }
    
    public static void encrypt(String word, int p, int add) {
        List<Integer> encryptedNums = new ArrayList<Integer>();
        for (int i = 0; i < word.length(); ++i) {
            for (int j = 0; j < letters.size(); ++j) {
                if (word.charAt(i) == letters.get(j)) {
                    encryptedNums.add(j);
                }
            }
        }
        
        for (Integer num : encryptedNums) {
            num = ((num * p + add)) % 26;
            
            if (num < 0) num = num * -1;
            System.out.print(letters.get(num));
            
        }
        System.out.println();
    }
    
    public static void decrypt(String code) {
        List<Integer> encryptedNums = new ArrayList<Integer>();

        for (int i = 0; i < code.length(); ++i) {
            for (int j = 0; j < letters.size(); ++j) {
                if(code.charAt(i) == letters.get(j)) {
                    encryptedNums.add(j);
                    
                }
            }
        }
        
        for (Integer num : encryptedNums) {
            
            System.out.println(letters.get(num-3));
            
        }
        
        System.out.println();

    }
    

}