using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MidtermExam
{
    class Circle : Shape
    {
        private int radius;
        public int Radius
        {
            get { return radius; }
            set
            {
                if (radius >= 0)
                    radius = value;
                else
                    radius = 0;
            }
        }

        public Circle()
        {
            radius = 0;
        }

        public Circle(int _radius, int _x, int _y, int _width, int _height)
           : base(_x, _y, _width, _height)
        {
            radius = _radius;
        }

        public Circle(int _radius)
        {
            radius = _radius;
        }

        ~Circle()
        {
            // Console.WriteLine("Call Circle destructor");
        }

        public override void Draw()
        {
            // base.Draw();
            Console.WriteLine("Draw Circle");
        }

    }
}
