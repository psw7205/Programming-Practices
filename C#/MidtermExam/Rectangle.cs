using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MidtermExam
{
    class Rectangle : Shape
    {
        private int fill;
        public int Fill
        {
            get { return fill; }
            set { fill = value; }
        }

        public Rectangle()
        {
            fill = 0;
        }

        public Rectangle(int _fill, int _x, int _y, int _width, int _height)
           : base(_x, _y, _width, _height)
        {
            fill = _fill;
        }

        public Rectangle(int _fill)
        {
            fill = _fill;
        }

        ~Rectangle()
        {
            // Console.WriteLine("Call Rectangle destructor");
        }

        public override void Draw()
        {
            // base.Draw();
            Console.WriteLine("Draw Rectangle");
        }
    }
}
