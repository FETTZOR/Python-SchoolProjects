using System;

namespace _02_emil_khaibrakhmanov
{
    public class EnemyInGame
    {
        private string _theNameOfEnemy = "Joker";
        private int _healthPointsEnemy;
        private bool _isEnemyAlive = true;
        
        public string TheNameOfEnemy   // property
        {
            get { return _theNameOfEnemy; }   // get method
        }

        
        public bool IsEnemyALive   // property
        {
            get { return _isEnemyAlive; }   // get method
            set { _isEnemyAlive = value; }  // set method
        }


        public EnemyInGame(int healthPoints)
        {   
            _healthPointsEnemy = healthPoints;
        }
        
        public int GetHealthPoints()
        {
            return _healthPointsEnemy;
        }

        public int Hit(int damageToEnemy)
        {
            _healthPointsEnemy = _healthPointsEnemy - damageToEnemy;

            if (_healthPointsEnemy <=0)
            {
                _isEnemyAlive = false;
            }
            return _healthPointsEnemy;
        }
    }
}