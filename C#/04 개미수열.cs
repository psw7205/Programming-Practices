using System;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "1";
            int end = int.Parse(Console.ReadLine());

            for (int k = 0; k < end; k++)
            {
                int cnt = 0;
                char tmp = input[0];
                string output = "";

                Console.WriteLine(k + 1 + "번째 >> " + input);

                for (int i = 0; i < input.Length; i++)
                {
                    if (tmp == input[i])
                        cnt++;
                    else
                    {
                        output = output + tmp + cnt;
                        tmp = input[i];
                        cnt = 1;
                    }
                }

                output = output + tmp + cnt;
                input = output;
            }
        }
    }
}
