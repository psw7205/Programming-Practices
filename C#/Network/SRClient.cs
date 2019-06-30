using System;
using System.IO;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class SRClient
    {
        static void Main()
        {
            //TcpClient tcpClient = new TcpClient("127.0.0.1", 123);
            TcpClient tcpClient = new TcpClient();
            tcpClient.Connect("127.0.0.1", 123);

            if (tcpClient.Connected)
            {
                Console.WriteLine("서버 연결 성공");
                NetworkStream ns = tcpClient.GetStream();

                using (StreamReader sr = new StreamReader(ns))
                {
                    string str = sr.ReadLine();
                    Console.WriteLine(str);
                    str = sr.ReadLine();
                    Console.WriteLine(str);
                    str = sr.ReadLine();
                    Console.WriteLine(str);
                    str = sr.ReadLine();
                    Console.WriteLine(str);
                }

                ns.Close();
            }
            else
                Console.WriteLine("서버 연결 실패");


            tcpClient.Close();
        }
    }
}
