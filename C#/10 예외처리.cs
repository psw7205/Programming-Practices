using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class ExceptionExample
    {
        static void Main(string[] args)
        {
            Console.Write("입력 : ");
            string input = Console.ReadLine();

            try
            {
                int idx = int.Parse(input);
                Console.WriteLine("입력숫자" + idx);
            }
            catch(Exception e)
            {
                Console.WriteLine(e.GetType() + " 예외 실행");
                return;
            }

            Console.WriteLine("프로그램 종료");
           
        }
    }
}
