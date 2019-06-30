using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class BWServer
    {
        static void Main()
        {
            TcpListener tcpListener = new TcpListener(IPAddress.Parse("127.0.0.1"), 123);
            tcpListener.Start();
            Console.WriteLine("서버 시작");

            TcpClient tcpClient = tcpListener.AcceptTcpClient();
            NetworkStream ns = tcpClient.GetStream();

            using (BinaryWriter bw = new BinaryWriter(ns))
            {
                bw.Write(false);
                bw.Write(1234);
                bw.Write(3.14);
                bw.Write("hello");
            }

            ns.Close();
            tcpListener.Stop();
            Console.WriteLine("서버 종료");
        }
    }
}
