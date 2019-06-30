using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class NSServer
    {
        static void Main()
        {
            /*
             TcpListner
             -> 연결대기, TcpClient 생성
             -> 생상자(ip주소, 포트)
             -> TcpListener.Start() / TcpListener.AcceptTcpClient() / TcpListener.Stop()
             */

            TcpListener tcpListener = new TcpListener(IPAddress.Parse("127.0.0.1"), 123);
            tcpListener.Start();
            Console.WriteLine("서버 시작");

            TcpClient tcpClient = tcpListener.AcceptTcpClient();
            NetworkStream ns = tcpClient.GetStream();

            byte[] recvMsg = new byte[128];
            ns.Read(recvMsg, 0, 128);
            string str = Encoding.ASCII.GetString(recvMsg);
            Console.WriteLine("recv message : " + str);

            byte[] sendMsg = Encoding.ASCII.GetBytes("echo message : " + str);
            ns.Write(sendMsg, 0, sendMsg.Length);

            ns.Close();
            tcpListener.Stop();
            Console.WriteLine("서버 종료");
        }
    }
}
