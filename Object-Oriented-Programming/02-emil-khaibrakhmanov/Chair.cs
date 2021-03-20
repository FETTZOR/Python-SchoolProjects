using System;

namespace _02_emil_khaibrakhmanov
{
    public class Chair
    {
        private int _numberOfLegs = 4;
        private string _colorOfTheSeat = "blue";
        private int _maxWeightLimit;
        public bool IsSitting { set; get; }


        public int NumberOfLegs
        {
            set => _numberOfLegs = value;
            get => _numberOfLegs;
        }

        public string ColorOfTheSeat
        {
            // set => _colorOfTheSeat = value;
            get => _colorOfTheSeat;
        }

        public Chair(int maxWeightLimit)
        {
            (_maxWeightLimit) = maxWeightLimit;
        }
        
        public int GetMaxWeightLimit()
        {
            return _maxWeightLimit;
        }
    }
}