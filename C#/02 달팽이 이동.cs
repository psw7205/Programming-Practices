using System;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 1;
            Console.CursorVisible = false;
            while (x < 50)
            {
                Console.Clear();
                Console.SetCursorPosition(x, 10);
                

                if (x % 3 == 0)
                    Console.Write("__@");
                else if(x%3 == 1)
                    Console.Write("_^@");
                else
                    Console.Write("^_@");

                System.Threading.Thread.Sleep(300);
                x++;
            }
        }
    }
}
