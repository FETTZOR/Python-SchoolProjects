using System;
using System.Collections.Generic;
using System.Linq;

namespace _1_Multiply_an_array_with_itself
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Hello, Please specify how much integers you want to write. For example write: 3");
            // declare a size of an array
            int howMuchIntegers = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Please write {howMuchIntegers} integers below(1 integer per Enter): ");
            // here I used static array, because we know size thanks to the user input
            var userIntegerInputArray = new int[howMuchIntegers];
            // add integers in array, iteration number == howMuchIntegers value
            for (int i = 0; i < howMuchIntegers; i++)
            {
                // ask user to input a value each iteration time and store in myArray
                userIntegerInputArray[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.WriteLine("\nThanks for your input!\n");
            
            MultiplyAndSort(userIntegerInputArray);
        }


        public static void MultiplyAndSort(int[] userIntegerInputArray)
        {
            /*
             -------------------------different way----------------
            this variable I declared for number of iteration counting that will help me to add an integers to an array
            int d = 0;
            static array to store the result
            int[] resultArray = new int[userIntegerInputArray.Length * userIntegerInputArray.Length];
             */  

            
            // dynamic list I like it more here, because I am not actually sure about the size,
            // but both of them were working perfect during my tests
            var resultList = new List<dynamic>();

            Console.WriteLine("Here is result of multiplication:\n");
            // iterate b value
            for (int b = 0; b < userIntegerInputArray.Length; b++)
            {
                //second for loop that iterates a value
                for (int a = 0; a < userIntegerInputArray.Length; a++)
                {
                    // declaring an variable for a * b values result
                    int c = userIntegerInputArray[b] * userIntegerInputArray[a];
                    // check if answer not already printed
                    if (!resultList.Contains(c))
                    {
                        Console.WriteLine($"{userIntegerInputArray[b]} * {userIntegerInputArray[a]} = {c}");
                    }
                    
                    /*
                     -------------------------different way----------------
                    adding c value to an array for checking if result already contains
                    list[d] = c;
                    d += 1; 
                    */  

                    
                    // adding a value to the list for checking if result already contains
                    resultList.Add(c);
                }
            }
        }
    }
}
