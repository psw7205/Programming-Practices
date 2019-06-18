using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FinalExam
{
    public partial class Form2 : Form
    {
        public BindingSource UserData
        {
            get { return userBindingSource; }
            set { userBindingSource = value; }
        }

        public Form2()
        {
            InitializeComponent();
            userBindingSource.Add(new User()
            {
                ID = 0,
                Name = "test0",
                Password = "0000",
                Login = false
            }) ;
            userBindingSource.Add(new User()
            {
                ID = 1,
                Name = "test1",
                Password = "0000",
                Login = false
            });
            userBindingSource.Add(new User()
            {
                ID = 2,
                Name = "test2",
                Password = "0000",
                Login = false
            });

            bookBindingSource.Add(new Book()
            {
                Isbn = 123,
                Name = "책1",
                Page = 100,
                Publisher = "세종출판",
                isChecked = false,
            }) ;
            bookBindingSource.Add(new Book()
            {
                Isbn = 456,
                Name = "책2",
                Page = 200,
                Publisher = "세종출판",
                isChecked = false,
            });
            bookBindingSource.Add(new Book()
            {
                Isbn = 789,
                Name = "책3",
                Page = 300,
                Publisher = "세종출판",
                isChecked = false,
            });
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            int isbn = -1;
            int id = -1;
            try
            {
                isbn = int.Parse(textBox1.Text);
                id = int.Parse(textBox3.Text);
            }
            catch (Exception)
            {
                MessageBox.Show("isbn과 id는 숫자만 입력하세요");
            }

            string name = textBox2.Text;


            foreach (var item in bookBindingSource)
            {
                Book book = item as Book;

                if (book != null)
                {
                    if (book.Isbn == isbn)
                    {
                        book.isChecked = true;
                        book.UserID = id;
                        break;
                    }
                }
            }
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            int isbn = -1;
            int id = -1;
            try
            {
                isbn = int.Parse(textBox1.Text);
                id = int.Parse(textBox3.Text);
            }
            catch (Exception)
            {
                MessageBox.Show("isbn과 id는 숫자만 입력하세요");
            }

            string name = textBox2.Text;


            foreach (var item in bookBindingSource)
            {
                Book book = item as Book;

                if (book != null)
                {
                    if (book.Isbn == isbn)
                    {
                        book.isChecked = false;
                        book.UserID = 0;
                        break;
                    }
                }
            }
        }
    }
}
