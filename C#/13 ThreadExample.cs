using System;
using System.Threading;

namespace ConsoleApp1
{
    class ThreadExample
    {
        static void Main(string[] args)
        {
            int length = 1000;
            Thread thread = new Thread(() =>
            {
                for (int i = 0; i < length; i++)
                {
                    Console.Write("A");
                }
            });


            Thread thread2 = new Thread(delegate() {
                for (int i = 0; i < length; i++)
                {
                    Console.Write("B");
                }
            });

            Thread thread3 = new Thread(TestMethod);

            thread.Start();
            thread2.Start();
            thread3.Start();
        }

        public static void TestMethod()
        {
            for (int i = 0; i < 1000; i++)
            {
                Console.Write("C");
            }
        }
    }
}
