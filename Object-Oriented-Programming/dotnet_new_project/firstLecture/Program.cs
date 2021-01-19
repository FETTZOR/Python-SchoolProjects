using System;

namespace firstLecture
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string name = "Emil";

            Console.WriteLine(name);

            int age = 34;
            double someNumber;
            someNumber = 3.23123;

            float floatVar = 3.23123f;

            bool asd = true;

            Console.WriteLine(asd);

            Console.WriteLine($"asdad {1 + 1}, {age}");

            SayHello();

            double multiplied = Multiply(2.0);
            Console.WriteLine(multiplied);
        }

        static void SayHello()
        {
            Console.WriteLine("Hello");
        }

        static double Multiply(double n)
        {
            return n * 2;
        }
    }
}
