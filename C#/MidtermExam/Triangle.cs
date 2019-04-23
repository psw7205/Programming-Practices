using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MidtermExam
{
    class Triangle : Shape
    {
        private int fill;
        public int Fill
        {
            get { return fill; }
            set { fill = value; }
        }

        public Triangle()
        {
            fill = 0;
        }

        public Triangle(int _fill, int _x, int _y, int _width, int _height)
            : base(_x, _y, _width, _height)
        {
            fill = _fill;
        }

        public Triangle(int _fill)
        {
            fill = _fill;
        }

        ~Triangle()
        {
            // Console.WriteLine("Call Triangle destructor");
        }

        public override void Draw()
        {
            // base.Draw();
            Console.WriteLine("Draw Triangle");
        }
    }
}
