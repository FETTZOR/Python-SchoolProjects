using System;
using System.Reflection.Metadata;

namespace PersonExample
{
    /*
    - first name
    - last name 
    - full name (first name + last name)
    (- address)
    */
   class Person {
        internal string lastName = "Doe";
        
        internal string firstName = "John";

        public string FirstName
        {
            get => firstName;
            set => firstName = value;
        }

        public string GetFirstName()
        {
            return firstName;
        }
        
        
        public string GetFullName()
        {
            return firstName + " " + lastName;
        }
        
        public Person(){   }

        public Person(string firstName, string lastName)
        {
            this.firstName = firstName;
            this.lastName = lastName;   
        }

        public Person(string firstName)
        {
            this.firstName = firstName;
        }

        // ~Person() eto destructor
        // {
        //     System.Console.WriteLine("Person destructor");
        // } 
   }
}