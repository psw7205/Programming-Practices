using System;
using System.IO;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class BRClient
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

                using (BinaryReader br = new BinaryReader(ns))
                {
                    Console.WriteLine(br.ReadBoolean());
                    Console.WriteLine(br.ReadInt32());
                    Console.WriteLine(br.ReadDouble());
                    Console.WriteLine(br.ReadString());
                }

                ns.Close();
            }
            else
                Console.WriteLine("서버 연결 실패");


            tcpClient.Close();
        }
    }
}
