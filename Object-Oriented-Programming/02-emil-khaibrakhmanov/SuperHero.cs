namespace _02_emil_khaibrakhmanov
{
    public class SuperHero
    {
        
        private string _theNameOfSuperHero = "Batman";
        private string _specialAbility = "flying";
        private bool _humanOrNot;
        private int _ageOfSuperHero = 228;
        
        public string TheNameOfSuperHero   // property
        {
            get { return _theNameOfSuperHero; }   // get method
            set { _theNameOfSuperHero = value; }  // set method
        }
        
        public string SpecialAbility   // property
        {
            get { return _specialAbility; }   // get method
            set { _specialAbility = value; }  // set method
        }
        
        public int AgeOfSuperhero   // property
        {
            get { return _ageOfSuperHero; }   // get method
            set { _ageOfSuperHero = value; }  // set method
        }


        public SuperHero(bool humanOrNot)
        {   
            _humanOrNot = humanOrNot;
        }
        
        public bool GetHumanOrNot()
        {
            return _humanOrNot;
        }


    }
}