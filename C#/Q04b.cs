using System;

namespace Q04b_2020
{
    class Program
    {
        // Write subprogram for Option 1 here

        // Write subprogram for Option 2 here

        static void Main(string[] args)
        {
            string[,] pupilAttendance = {
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

            int option = 0;

            Console.WriteLine("Attendance Menu Options");
            Console.WriteLine("1 - Display names of low attendance");
            Console.WriteLine("2 - Display number of high attendance");
            Console.Write("Choose option: ");
            option = Convert.ToInt16(Console.ReadLine());

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
                Console.WriteLine("Program complete");
            }

            Console.ReadKey();
        }
    }
}

