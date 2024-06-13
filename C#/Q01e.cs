using System;

namespace Q01e_2020
{
    class Program
    {
        private static int sumOfNumbers(int [] listNumbers)
        {
            int amount = 0;
            foreach (int x in listNumbers)
            {
                if (x > 22 && x <= 40)
                {
                    amount = amount + x;
                }
            }
            return amount;
        }

        static void Main(String[] args)
        {
            int [] numArray = { 23, 22, 41, 26, 55, 27, 34, 45, 24, 40, 25, 29, 51, 28, 55 };

            int total = sumOfNumbers(numArray);
            String message = "Sum of selected numbers is " ;
            Console.WriteLine(message + Convert.ToString(total));

            Console.ReadKey();
        }
    }
}
