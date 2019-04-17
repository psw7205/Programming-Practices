using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Csharp
{
    class Parent
    {
        public static int counter = 0;
        public int var = 10;
        public void CountParnet()
        {
            Parent.counter++;
        }
    }

    class Child : Parent
    {
        public new string var = "abcd";
        public void CountChild()
        {
            Child.counter++;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Parent parent = new Parent();
            Child child = new Child();

            parent.CountParnet();
            child.CountChild();
            child.CountChild();
            child.CountChild();


            Console.WriteLine(Parent.counter);
            Console.WriteLine(Child.counter);
            
            Console.WriteLine(child.var);
            Console.WriteLine(((Parent)child).var);
        }
    }
}
