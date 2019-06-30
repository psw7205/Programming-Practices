using System;
using System.Net;

namespace ConsoleApp1
{
    class IPAddressPractices
    {
        static void Main()
        {
            /*
             IPAddress -> ip
             - IPHostEntr -> ip + hostname
             - IPEndPoint -> ip + port
             - Dns -> ip + domain
             */

            // IPAddress 클래스
            string addr = "127.0.0.1";
            IPAddress ip = IPAddress.Parse(addr);
            Console.WriteLine("ip : {0}", ip.ToString());
            Console.WriteLine("=========================");

            // Dns 클래스 GetHostAddresses 메소드
            IPAddress[] ip2 = Dns.GetHostAddresses("www.naver.com");

            foreach (var item in ip2)
            {
                Console.WriteLine($"{item}");
            }

            Console.WriteLine("=========================");

            // IPHostEntry
            IPHostEntry info = Dns.GetHostEntry("www.naver.com");

            foreach (var item in info.AddressList)
            {
                Console.WriteLine($"{item}");
            }

            Console.WriteLine(info.HostName);

            Console.WriteLine("=========================");

            // IPEndPoint
            IPEndPoint ep = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 13);
            Console.WriteLine($"ip : {ep.Address}, port : {ep.Port}");
            Console.WriteLine(ep.ToString());
        }
    }
}
