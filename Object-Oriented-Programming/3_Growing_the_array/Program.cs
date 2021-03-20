using System;

namespace _3_Growing_the_array
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, this program asking numbers from you until it less than 0!");
            IntegersInArray();
        }
        
        private static void IntegersInArray()
        {
            // declaring static array with size that can afford one integer
            int[] myArray = new int[1];
            // counter that i will use for increasing
            int i = 0;
            // infinite while loop that I will just break when user will input number lower than 0
            while (true)
            {
                // taking user input
                var userIntInput = Convert.ToInt32(Console.ReadLine());
                // if user input greater thea zero it will be added to an array
                if (userIntInput >= 0)
                {
                    // input added to an array after checking
                    myArray[i] = userIntInput;
                    // resize by adding + 1 to an array size
                    Array.Resize(ref myArray, myArray.Length + 1);
                    // increase counter for array control
                    i++;
                }
                else
                {
                    // breaking loop when number is lower than 0
                    break;
                }
            }
            // iterating an array -1 because last number in my array is 0 so I am iterating with it
            for (int a = 0; a < myArray.Length-1; a++)
            {
                // Adding comma to each number except the last
                if (a != myArray.Length - 2)
                {
                    Console.Write($"{myArray[a]}, ");
                }
                else
                {
                    // printing last array number without comma
                    Console.Write(myArray[a]);
                }
            }
        }
    }
}
