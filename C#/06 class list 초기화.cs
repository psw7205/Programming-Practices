using System;
using System.Collections.Generic;

namespace Csharp
{
    class Program
    {
        class Student
        {
            public string name;
            public int grade;
        }

        static void Main(string[] args)
        {
            List<Student> list = new List<Student>()
            {
                new Student() {name = "윤인성", grade = 1},
                new Student() {name = "연하진", grade = 2},
                new Student() {name = "윤아린", grade = 3},
                new Student() {name = "윤명월", grade = 4},
                new Student() {name = "구지연", grade = 1},
                new Student() {name = "김연화", grade = 2}
            };

            foreach (var item in list)
                Console.WriteLine(item.name + " grade :" + item.grade);

            for(int i = list.Count - 1; i >= 0; i--)
            {
                if(list[i].grade>1)
                {
                    list.RemoveAt(i);
                }
            }

            Console.WriteLine("---------------");
            foreach (var item in list)
                Console.WriteLine(item.name + " grade :" + item.grade);
        }
    }
}
