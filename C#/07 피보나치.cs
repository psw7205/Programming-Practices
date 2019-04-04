using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Csharp
{
    class Fibonacci
    {
        // 중복 호출
        public long Fibo1(int i)
        {
            if (i < 0) return 0;
            if (i == 1) return 1;
            return Fibo1(i - 2) + Fibo1(i - 1);
        }

        // 딕셔너리를 이용한 메모이제이션
        private static Dictionary<int, long> memo = new Dictionary<int, long>();
        public long Fibo2(int i)
        {
            if (i < 0) return 0;
            if (i == 1) return 1;

            if (memo.ContainsKey(i)) return memo[i];
            else
            {
                long tmp = Fibo2(i - 2) + Fibo2(i - 1);
                memo[i] = tmp;
                return tmp;
            }
        }

    }

    class Program
    {

        static void Main(string[] args)
        {
            Fibonacci fibonacci = new Fibonacci();
            Stopwatch sw = new Stopwatch();

            sw.Start();
            Console.Write(fibonacci.Fibo1(30));
            sw.Stop();
            Console.WriteLine(" : " + sw.ElapsedMilliseconds.ToString() + "ms");

            sw.Reset();
            sw.Start();
            Console.Write(fibonacci.Fibo2(30));
            sw.Stop();
            Console.WriteLine(" : " + sw.ElapsedMilliseconds.ToString() + "ms");
        }
    }
}
