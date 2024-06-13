import java.util.Scanner;

public class q04b
{
    // write subprogram for option 1 here
    
    
    // write subprogram for option 2 here
    
    
    public static void main(String[] args)
    {
        String [][] pupilAttendance = {
	{"Faroukh" , "Salah" , "70"},
	{"Kelvin", "Glintode" , "85"},
	{"Lara" , "Godfrey" , "90"},
	{"Amara" , "Grzinski" , "70"},
	{"Aaron" , "Grimshaw" , "90"},
	{"Farihaa" , "Mohan" , "95"},
	{"Taz" , "Grimstow" , "60"},
	{"Ali" , "Aisha" , "95"},
	{"Charlene" , "Hall" ,"85"},
	{"Asra" , "Ashiq" , "90"},
    {"Sadia" , "Bhatti" , "65"},
	{"Ria" , "Hall" , "90"},
	{"Fernado" , "Askabat" , "60"},
	{"Richard" , "Hawkins" , "80"},
	{"Siyao" , "Wang" , "60"},
	{"Marketta" , "Hosier" , "100"}
	};

		int option;
		Scanner input = new Scanner(System.in);
			
		System.out.println("Attendance Menu Options");
		System.out.println("1 - Display names of low attendance");
		System.out.println("2 - Display number of high attendance");
		System.out.print("Choose option: ");
		option = Integer.parseInt(input.next());
			
		if (option == 1)
		{
                // complete the if statement
	
        }

		else if (option == 2)
		{
				// complete the else if statement
            
		}
	
		else
		{
            System.out.println("Program complete");
		}
    }
}