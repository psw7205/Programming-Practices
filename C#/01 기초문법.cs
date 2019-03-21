using System;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("문자열 입력 : ");
            string str = Console.ReadLine();

            if (str.Contains("안녕"))
                Console.WriteLine("안녕이 포함됨");
            else
                Console.WriteLine("안녕이 포함 안됨");

            Console.Write("화살표 입력 : ");
            ConsoleKeyInfo info = Console.ReadKey();

            switch (info.Key)
            {
                case ConsoleKey.UpArrow:
                    Console.WriteLine("위로 이동");
                    break;

                case ConsoleKey.DownArrow:
                    Console.WriteLine("아래로 이동");
                    break;

                case ConsoleKey.RightArrow:
                    Console.WriteLine("오른쪽으로 이동");
                    break;

                case ConsoleKey.LeftArrow:
                    Console.WriteLine("왼쪽으로 이동");
                    break;

                default:
                    Console.WriteLine("잘못된 키");
                    break;
            }

            int[] intArray = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            string[] strArray = { "일", "이", "삼", "사" };

            double[] doubleArray = new double[100]; // 100개짜리 배열 생성, 0으로 초기화 되서 생성

            for (char i = '가'; i <= '강'; i++) // C#은 유니코드 지원, 한글가능
                Console.Write(i + " ");

            Console.Write("\n");
            foreach (string tmp in strArray)
                Console.Write(tmp + " ");

            // 모든 문자열 함수는 반환값으로 결과를 보냄
            // 기존 변수는 변함 X
            string input = "Potato Tomato";
            Console.WriteLine(input.ToUpper());
            Console.WriteLine(input.ToLower());

            input = "감자 고구마-토마토/가지";
            string[] inputs = input.Split(new char[] { ' ', '/', '-' });

            foreach (var i in inputs)
                Console.WriteLine(i);

            string newStr = string.Join("+++", inputs);
            Console.WriteLine(newStr); // 문자열 합치기
            
        }
    }
}
