using System;
using System.Collections.Generic;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> myList = new List<int>();

            for (int i = 0; i < 30; i++)
            {
                myList.Add(new Random().Next(1, 100));
            }

            foreach (var item in myList)
            {
                Console.Write(item + " ");
            }
        }
    }
}
