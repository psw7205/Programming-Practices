using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MidtermExam
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Shape> shape = new List<Shape>();

            Random random = new Random();
            for(int i = 0; i < 10; ++i)
            {
                int tmp = random.Next() % 3;
                
                switch (tmp)
                {
                    case 0:
                        shape.Add(new Circle());
                        break;
                    case 1:
                        shape.Add(new Rectangle());
                        break;
                    case 2:
                        shape.Add(new Triangle());
                        break;

                    default:
                        break;
                }
            }

            foreach (var item in shape)
            {
                item.Draw();
            }
        }
    }
}
