using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chapter05
{
    class Program
    {
        static void Main(string[] args)
        {
            int answer = new Random().Next(0, 500);

            while(true)
            {
                Console.Write("숫자를 입력해주세요 : ");
                int tmp = int.Parse(Console.ReadLine());

                if(tmp > answer)
                {
                    Console.WriteLine(tmp + "보다는 작은 숫자입니다.\n");
                }
                else if(tmp < answer)
                {
                    Console.WriteLine(tmp + "보다는 큰 숫자 입니다.\n");
                }
                else
                {
                    Console.WriteLine("정답입니다!!\n");
                    break;
                }
            }

        }
    }
}
