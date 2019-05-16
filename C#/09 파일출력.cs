using System;
using System.IO;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            using (StreamWriter writer = new StreamWriter(@"test.txt"))
            {
                string line;
                while (true)
                {
                    line = Console.ReadLine();
                    string tmp = line.ToLower();
                    if (tmp == "exit")
                        break;

                    writer.WriteLine(line);
                }
            }
        }
    }
}
