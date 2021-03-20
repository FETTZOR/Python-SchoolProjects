using System;

namespace _02_emil_khaibrakhmanov
{
    class Program
    {
        static void Main(string[] args)
        {
            
            ChairMethod();
            
            
            
            SuperHeroMethod();
            
            
            
            EnemyInGameMethod();
            
        }
        
        
        static void ChairMethod()
        {
            Console.WriteLine("Chair started\n");
            
            Chair ch1 = new Chair(400);
            
            Console.WriteLine($"Chair legs number: {ch1.NumberOfLegs}");
            
            Console.WriteLine($"Chair color: {ch1.ColorOfTheSeat}");
            
            // output 400
            Console.WriteLine($"Max weight limit: {ch1.GetMaxWeightLimit()}");

            // will output false
            Console.WriteLine($"Default value of bool isSitting: {ch1.IsSitting}");
            ch1.IsSitting = true;
            // value changed
            Console.WriteLine($"Value of bool isSitting after change: {ch1.IsSitting}");
            
            Console.WriteLine("\nChair ended\n");
        }

        static void SuperHeroMethod()
        {
            Console.WriteLine("SuperHero started\n");
            
            SuperHero s1 = new SuperHero(true);
            
            // Name can be changed
            Console.WriteLine($"Name of superhero: {s1.TheNameOfSuperHero}");
            s1.TheNameOfSuperHero = "Superman";
            Console.WriteLine($"Name of superhero after change: {s1.TheNameOfSuperHero}");
            
            // Special ability also can be changed
            Console.WriteLine($"Special ability: {s1.SpecialAbility}");
            
            // Is human or not(can not be changed)
            Console.WriteLine($"Is human? {s1.GetHumanOrNot()}");

            // Age (Can be changed)
            Console.WriteLine($"Age: {s1.AgeOfSuperhero} years");
            
            Console.WriteLine("\nSuperHero ended\n");
        }

        static void EnemyInGameMethod()
        {
            Console.WriteLine("EnemyInGame started\n");
            
            EnemyInGame e1 = new EnemyInGame(300);
            
            // Enemy name 
            Console.WriteLine(e1.TheNameOfEnemy);
            
            // Enemy Health Points
            Console.WriteLine($"Enemy HP: {e1.GetHealthPoints()}");
            
            // Checking is Enemy alive Or Not
            Console.WriteLine($"Is enemy alive by default: {e1.IsEnemyALive}");
            
            // using hit method
            e1.Hit(150);
            e1.Hit(200);
            Console.WriteLine($"Enemy after 2 hits is Alive? {e1.IsEnemyALive}");
            
            Console.WriteLine("\nEnemyInGame ended\n");
        }
    }
}
            
