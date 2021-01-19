using System;

namespace exercises_01
{
    class Program
    {
        static void Main(string[] args)
        {
            string myName = "Emil";

            int myAge = 24;

            double PI = 3.14;

            Console.WriteLine($"{myName} \n{myAge} \n{PI} \n");

            UsefulFunction();

            int multiplier = MultiplyByTwo(3);
            Console.WriteLine(multiplier);
        }

        static void UsefulFunction()
        {
            Console.WriteLine("Function executed!");
        }

        static int MultiplyByTwo(int n)
        {
            return n * 2;
        }
    }
}
