using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chapter05
{
    class BookInfo
    {
        public string bookName;
        public string firstEditionDate;
        public string author;
        public string publisher;
        public string publish;
        public string chiefEditor;
        public string planner;
        public string editior;
        public string designer;

    }

    class Program
    {
        static void Main(string[] args)
        {
            BookInfo php = new BookInfo()
            {
                bookName = "PHP 프로그래밍 입문",
                firstEditionDate = "2013년 5월 20일",
                author = "황재호",
                publisher = "김태헌",
                publish = "한빛아카데미(주)",
                chiefEditor = "김현용",
                planner = "김이화",
                editior = "김이화",
                designer = "여동일"
            };

        }
    }
}
