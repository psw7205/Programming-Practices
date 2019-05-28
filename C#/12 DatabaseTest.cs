using System;
using System.Data;
using MySql.Data.MySqlClient;

namespace ConsoleApp1
{
    class DatabaseTest
    {
        static void Main(string[] args)
        {
            SelectUsingReader();
        }

        private static void SelectUsingReader()
        {
            string connStr = "Server=localhost;Database=sample2;Uid=root;Pwd=0000;";

            using (MySqlConnection conn = new MySqlConnection(connStr))
            {
                conn.Open();
                string sql = "SELECT * FROM goods";

                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                while (rdr.Read())
                {
                    Console.WriteLine("{0}: {1}", rdr["goods_id"], rdr["goods_name"]);
                }
                rdr.Close();
            }
        }

       
    }
}
