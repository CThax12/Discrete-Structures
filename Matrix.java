package Matrix;

import java.util.Scanner;

public class Matrix {

	public static void main(String[] args) {
		
		System.out.println("Matrix 1 rows:");
		Scanner scan = new Scanner(System.in);
		int one_rows = scan.nextInt();
		System.out.println("Matrix 1 columns:");
		int one_columns = scan.nextInt();
		System.out.println("Matrix 2 rows:");
		int two_rows = scan.nextInt();
		System.out.println("Matrix 2 columns:");
		int two_columns = scan.nextInt();
		
		int matrix_one[][] = new int[one_rows][one_columns];
		int matrix_two[][] = new int[two_rows][two_columns];
		
		int result_matrix[][] = new int[one_rows][two_columns];
		int i, j, k;
		
		for (i = 0; i < one_rows; i++) {
            for (j = 0; j < one_columns; j++) {
                    matrix_one[i][j] += scan.nextInt();
            }
        }
		
		for (i = 0; i < two_rows; i++) {
            for (j = 0; j < two_columns; j++) {
                    matrix_two[i][j] += scan.nextInt();
            }
        }
		
		 for (i = 0; i < one_rows; i++) {
	            for (j = 0; j < two_columns; j++) {
	                for (k = 0; k < two_rows; k++)
	                    result_matrix[i][j] += matrix_one[i][k] * matrix_two[k][j];
	            }
	        }
		 
		 System.out.println("\nResultant Matrix:");
	        printMatrix(result_matrix, one_rows, two_columns);
	}
	
	 static void printMatrix(int answer_matrix[][], int rowSize, int colSize) {
		 	for (int i = 0; i < rowSize; i++) {
		 		for (int j = 0; j < colSize; j++)
		 			System.out.print(answer_matrix[i][j] + " ");

		 			System.out.println();
		 		}
	 	}

}


