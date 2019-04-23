using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MidtermExam
{
    // 부모가 될 클래스
    class Shape
    {
        private int x;
        private int y;
        private int width;
        private int height;

        public int X
        {
            get { return x; }
            set
            {
                if (x >= 0)
                    x = value;
                else
                    x = 0;
            }
        }

        public int Y
        {
            get { return y; }
            set
            {
                if (y >= 0)
                    y = value;
                else
                    y = 0;
            }
        }

        public int Width
        {
            get { return width; }
            set
            {
                if (width >= 0)
                    width = value;
                else
                    width = 0;
            }
        }

        public int Height
        {
            get { return height; }
            set
            {
                if (height >= 0)
                    height = value;
                else
                    height = 0;
            }
        }

        public Shape()
        {
            x = 0;
            y = 0;
            width = 0;
            height = 0;
        }

        public Shape(int _x, int _y, int _width, int _height)
        {
            x = _x;
            y = _y;
            width = _width;
            height = _height;
        }

        ~Shape()
        {
            // Console.WriteLine("Call Shape destructor");
        }

        // 오버라이드 할 함수
        public virtual void Draw()
        {
            Console.WriteLine("Shape class Draw");
        }

    }

}
