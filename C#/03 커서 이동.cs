using System;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 10, y = 10;
            Console.CursorVisible = false;

            bool flag = true;
            while (flag)
            {
                Console.SetCursorPosition(x, 10);

                ConsoleKeyInfo info = Console.ReadKey();
                switch (info.Key)
                {
                    case ConsoleKey.UpArrow:
                        y--;
                        break;

                    case ConsoleKey.DownArrow:
                        y++;
                        break;

                    case ConsoleKey.RightArrow:
                        x++;
                        break;

                    case ConsoleKey.LeftArrow:
                        x--;
                        break;

                    case ConsoleKey.X:
                        flag = false;
                        break;

                    default:
                        break;
                }

                Console.Clear();
                Console.SetCursorPosition(x, y);
                Console.Write("@");
            }
        }
    }
}
