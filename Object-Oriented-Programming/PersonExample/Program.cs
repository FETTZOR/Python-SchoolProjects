using System;

namespace PersonExample
{
    class Program
    {
        static void Main(string[] args)
        {
            Person p1 = new Person();

            // p1->firstname
            Console.WriteLine(p1.firstName);
            Console.WriteLine(p1.lastName);

            p1.firstName = "Matt";
            Console.WriteLine(p1.firstName);

            Person p2 = new Person("John", "Smith");
            Console.WriteLine(p2.GetFullName());
            
        }
    }
}
