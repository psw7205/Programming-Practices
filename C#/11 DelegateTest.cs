using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class DelegateTest
    {
        class Product
        {
            public string Name { get; set; }
            public int Price { get; set; }
        }
        static void Main(string[] args)
        {
            List<Product> products = new List<Product>()
            {
                new Product() {Name = "감자", Price = 500},
                new Product() {Name = "사과", Price = 700},
                new Product() {Name = "고구마", Price = 400},
                new Product() {Name = "배추", Price = 600},
                new Product() {Name = "상추", Price = 300}
            };

            //products.Sort(delegate (Product a, Product b)
            //{
            //    return a.Price.CompareTo(b.Price);
            //});

            products.Sort((a, b) => a.Price.CompareTo(b.Price));

            foreach (var item in products)
            {
                Console.WriteLine(item.Name + " : " + item.Price);
            }
        }
    }
}
