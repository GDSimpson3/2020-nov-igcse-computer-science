public class Q01e
{
    private static int sumOfNumbers(int listNumbers[])
		{
            int amount = 0;
            for(int x=0; x<listNumbers.length; x++)
                {
                    if (listNumbers[x] > 22 && listNumbers[x] <= 40)
                        {
                            amount = amount + listNumbers[x];
                        }
                }
            return amount;
		}

    public static void main(String[] args)
        {
            int numArray [] = {23, 22, 41, 26, 55, 27, 34, 45, 24, 40, 25, 29, 51, 28, 55};
	
            String message = "Sum of selected numbers is ";
            int total = sumOfNumbers(numArray);
            System.out.println(message + total);
        }
}