public class q04a
{
   public static void main(String[] args)
    {
        String[][] studentName = {
	{"Kevin", "Horney", "71", "55"},
	{"Tony", "Tison", "36", "50"},
	{"David", "Smith", "39", "48"},
	{"Vicky", "Bertwistle", "58", "71"},
	{"Jason", "Blashaw", "49", "80"},
	{"Louise","Smith", "81", "67"},
	{"Sara", "Acton", "37", "66"},
	{"Donna", "Alexander", "84", "86"},
	{"Michael", "Mitchelle", "65", "55" },
	{"Anthony", "Lewis", "48", "50"},
	{"Sharon", "Grant", "53", "70"},
	{"Peter", "Hughes", "82", "90"},
	{"Deborah", "Biddle", "51", "47"},
	{"Dawn", "Doens", "35", "44"},
	{"William", "Dennis", "72", "73"},
	{"Selim", "Biddle", "52", "67"},
	{"Ian", "Nadeem", "40", "36"},
	{"Jenny", "Thomson", "56", "43"},
	{"Rowena", "Moore", "50", "77"},
	{"Jane", "Murphy", "44", "48"}};
				
	String[] message = {
            "student failed both tests",
            "student failed one test",
            "student passed both with distinction",
            "student passed both tests"};
       for (String[] student : studentName)
       {
           int messageIndex = 0;
           
           String firstName = student[0];
           String lastName = student[1];
           int english = Integer.parseInt(student[2]);
           int maths = Integer.parseInt(student[3]);
           
           System.out.print(firstName + " " + lastName + ": ");
           if (  ) //student failed both tests
           {
               messageIndex = 0;
           }
           
           else if (  ) // student failed one test
           {
               messageIndex = 1;
           }
           
           else if (  ) // student passed both with distinction
           {
               messageIndex = 2;
           }
           
           else
           {
                  // student passed both tests
           }
           
           System.out.println(message[messageIndex]);
       }
    }
}
