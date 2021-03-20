using System;
using System.Collections.Generic;
using System.Linq;

namespace _2_Command_line_app_with_flags
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                if (args[3].Length != 0)
                {
                    Console.WriteLine("You specified more then 3 arguments!");
                }
            }
            catch (Exception)
            {
                try
                {
                    // checking if arguments contains all max requirements
                    if (args.Contains("-v") && args.Contains("-f") && args[0].Length != 0 && args[1].Length != 0 && args[2].Length != 0)
                    {
                        // declaring a list to store a 1 word is not -v and -f (our argument)
                        List<string> callMass = new List<string>();
                        foreach  (string word in args)
                        {
                            // drop arguments -f and -v
                            if (word != "-f" && word != "-v")
                            {
                                // adding word to list
                                callMass.Add(word);
                            }
                        }
                        // split word on letters
                        foreach (char letter in callMass[0])
                        {
                            // drop everything after .
                            if (letter != '.')
                            {
                                Console.Write(letter);
                            }
                            // breaking after .
                            else
                            {
                                Console.Write("\n");
                                break;
                            }
                        }
                    }
                    // if not contains -v and have 2 args filename and -f
                    else if(args.Contains("-f") && args[0].Length != 0 && args[1].Length != 0)
                    {
                        // printing all word
                        foreach  (string word in args)
                        {
                            // dropping words -f and -v
                            if (word != "-f" && word != "-v")
                            {
                                // printing entered word
                                Console.WriteLine(word);
                            }
                        }
                    }
                    // if no -f argument
                    else if (!args.Contains("-f"))
                    {
                        Console.WriteLine("No file specified! (use the -f argument)");
                    }
                }
                // if some exception raised
                catch (Exception)
                {
                    Console.WriteLine("Some exception, sorry!");
                }
            }
        }
    }
}