import java.util.*;
import java.util.*;
import java.util.*;
import java.util.*;
import java.util.*;
import java.util.*;
import java.util.*;

// Lab Task 1.1


public class Lab1 {

      public static void main(String args[]) {

            int number;

            Scanner in = new Scanner(System.in);

            System.out.println("Enter any number between 0 and five");

            number = in.nextInt();

            if (number == 0)
                  System.out.println("Zero");
            else if (number == 1)
                  System.out.println("One");
            else if (number == 2)
                  System.out.println("Two");
            else if (number == 3)
                  System.out.println("Three");
            else if (number == 4)
                  System.out.println("Four");
            else if (number == 5)
                  System.out.println("Five");
            else if (number == 6)
                  System.out.println("Zero");
            else if (number == 7)
                  System.out.println("Seven");
            else if (number == 8)
                  System.out.println("Eight");
            else if (number == 9)
                  System.out.println("Nine");
            else
                  System.out.println("not a valid number");

            in.close();

      }
}


// Lab Task 1.2


public class Lab2 {

      public static void main(String args[]) {

            int[] number = new int[5];

            int max = 0;

            Scanner in = new Scanner(System.in);

            System.out.println("Enter five numbers");

            for (int i = 0; i < 5; i++) {

                  number[i] = in.nextInt();

                  if (number[i] > max)
                        max = number[i];

            }

            System.out.println("largest number is " + max);

            in.close();

      }
}

// Lab Task 1.3


public class Lab3 {

      public static void main(String args[]) {

            double investment = 1000.0;

            System.out.println("year Amount on deposit");

            for (int i = 0; i < 10; i++) {

                  System.out.println(i + " " + Math.round(investment));

                  investment = investment + (0.05 * investment);

            }

      }
}

// Lab Task 1.4


public class Lab4 {

      public static void main(String args[]) {

            double average = 0, sum = 0, number = 0, count = 0;

            Scanner in = new Scanner(System.in);

            while (number != -999) {

                  sum = sum + number;

                  count++;

                  System.out.println("Enter numbers and -999 to exit");

                  number = in.nextInt();

            }

            average = sum / count;

            System.out.println("Sum = " + sum);

            System.out.println("Average = " + average);

            in.close();

      }
}

// Lab Task 1.5


public class Lab5 {

      public static void main(String args[]) {

            Scanner in = new Scanner(System.in);

            double Operand1 = 0, Operand2 = 0, result = 0;

            char Operator;

            System.out.println("Enter Operand 1: ");

            Operand1 = in.nextInt();

            System.out.println("Enter Operand 2: ");

            Operand2 = in.nextInt();

            System.out.println("Choose an operator: +, -, *, or /");

            Operator = in.next().charAt(0);

            switch (Operator) {

                  // performs addition between numbers
                  case '+':
                        result = Operand1 + Operand2;
                        System.out.println(Operand1 + " + " + Operand2 + " = " + result);

                  // performs subtraction between numbers
                  case '-':
                        result = Operand1 - Operand2;
                        System.out.println(Operand1 + " - " + Operand2 + " = " + result);
                        break;

                  // performs multiplication between numbers
                  case '*':
                        result = Operand1 * Operand2;
                        System.out.println(Operand1 + " * " + Operand2 + " = " + result);
                        break;

                  // performs division between numbers
                  case '/':
                        result = Operand1 / Operand2;
                        System.out.println(Operand1 + " / " + Operand2 + " = " + result);
                        break;

                  default:
                        System.out.println("Invalid operator!");
                        break;

            }

            in.close();

      }
}


//Lab Task 1.6


public class Lab6 {

      public static void main(String args[]) {

            int[] number = new int[100];

            int[] count = new int[10];

            int times = 100;

            Scanner in = new Scanner(System.in);

            System.out.println("Enter 100 numbers");

            for (int i = 0; i < times; i++) {

                  number[i] = in.nextInt();

                  if (number[i] == 0)
                        count[0]++;
                  else if (number[i] == 1)
                        count[1]++;
                  else if (number[i] == 2)
                        count[2]++;
                  else if (number[i] == 3)
                        count[3]++;
                  else if (number[i] == 4)
                        count[4]++;
                  else if (number[i] == 5)
                        count[5]++;
                  else if (number[i] == 6)
                        count[6]++;
                  else if (number[i] == 7)
                        count[7]++;
                  else if (number[i] == 8)
                        count[8]++;
                  else if (number[i] == 9)
                        count[9]++;
                  else {
                        System.out.println("Enter a single digit number");
                        i--;
                  }

            }

            for (int i = 0; i < times; i++) {

                  System.out.println("number " + i + " is present " + count[i] + " times");

            }

            in.close();

      }
}


//Lab Task 1.7


public class Lab7 {

      public static void main(String args[]) {

            Scanner in = new Scanner(System.in);

            int num, dec = 0, i = 0, rem, bin = 0;

            // Binary to Decimal
            System.out.println("Enter a binary number:");
            num = in.nextInt();

            int temp = num;

            while (temp != 0) {

                  rem = temp % 10;

                  temp /= 10;

                  dec += rem * Math.pow(2, i);

                  ++i;

            }

            System.out.println("Decimal Equivalent of " + num + " is " + dec);

            // Decimal to Binary
            System.out.println("Enter a Decimal number now:");
            num = in.nextInt();

            temp = num;

            i = 1;

            while (temp != 0) {

                  rem = temp % 2;

                  temp /= 2;

                  bin += rem * i;

                  i *= 10;

            }

            System.out.println("Binary Equivalent of " + num + " is " + bin);

            in.close();

      }
}
