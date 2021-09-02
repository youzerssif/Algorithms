import java.security.*;
import java.util.Scanner;

// Your First Program

class Hello {
    public static void main(String[] args) {
        int addt = Addition.add();
        System.out.println("Hello, World !"); 
    }
}

class Addition{

    public static int add(){
        Scanner scanner = new Scanner(System.in);
        int cmpt = 1;
        // int a = scanner.nextInt();
        int nombre = scanner.nextInt();
        while (cmpt < 11) {
            System.out.println(nombre +" X "+ cmpt +"="+ nombre*cmpt);
            cmpt++;
        }
        
        return 0;
    }
    
}

