using System;
using System.Net.Sockets;
using System.Text;

namespace ConsoleApp1
{
    class NSClient
    {
        static void Main()
        {
            /*
             TcpClient 
             -> 서버와 클라이언트 모두 사용
             -> 연결 및 요청
            */

            //TcpClient tcpClient = new TcpClient("127.0.0.1", 123);
            TcpClient tcpClient = new TcpClient();
            tcpClient.Connect("127.0.0.1", 123);

            if (tcpClient.Connected)
            {
                Console.WriteLine("서버 연결 성공");
                NetworkStream ns = tcpClient.GetStream();

                string str = Console.ReadLine();
                byte[] sendMsg = Encoding.ASCII.GetBytes(str);
                ns.Write(sendMsg, 0, sendMsg.Length);

                byte[] recvMsg = new byte[128];
                ns.Read(recvMsg, 0, 128);
                str = Encoding.ASCII.GetString(recvMsg);
                Console.WriteLine(str);


                ns.Close();

            }
            else
                Console.WriteLine("서버 연결 실패");


            tcpClient.Close();
        }
    }
}
