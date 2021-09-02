// import java.security.*;
// import java.util.Scanner;


// Your First Program

class Hello {

    String ma_cahine;
    Hello(String ma_cahine){
        this.ma_cahine = ma_cahine;
        System.out.println("Welcome Constructor"+ this);
    }    
    public static void main(String[] args) {
        int addt = Addition.add();
        // ma_classe.add();
        System.out.println("Hello"+ addt); 
         
    }
}

class Addition{

    public static int add(){
        Object ma_classe = new Hello("Bonjour");
        System.out.println(ma_classe instanceof Hello);
        System.out.println("Constructor spell! "+ ma_classe);
        int[] numbers = {3, 9, 5, -5};
        // System.out.println(numbers[0]);
        int sum = 0;
        for( int numb : numbers){
            sum += numb;

        }
        // System.out.println("Ok on affiche "+ sum);
        
        return sum;
    }
    
}

