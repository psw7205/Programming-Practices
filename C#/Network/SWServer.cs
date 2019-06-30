using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class SWServer
    {
        static void Main()
        {
            TcpListener tcpListener = new TcpListener(IPAddress.Parse("127.0.0.1"), 123);
            tcpListener.Start();
            Console.WriteLine("서버 시작");

            TcpClient tcpClient = tcpListener.AcceptTcpClient();
            NetworkStream ns = tcpClient.GetStream();

            using (StreamWriter sw = new StreamWriter(ns))
            {
                sw.AutoFlush = true;
                sw.WriteLine(false);
                sw.WriteLine(1234);
                sw.WriteLine(3.14f);
                sw.WriteLine("hello");
            }

            ns.Close();
            tcpListener.Stop();
            Console.WriteLine("서버 종료");
        }
    }
}
