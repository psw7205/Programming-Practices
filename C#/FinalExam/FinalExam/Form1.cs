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
    /*
     기본 아이디 test0, test1, test2
     비밀번호 0000
    */

    public partial class Form1 : Form
    {
        Form2 form2;
        BindingSource bindingSource;

        public Form1()
        {
            InitializeComponent();
            form2 = new Form2();
            bindingSource = form2.UserData;
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            string name = textBox1.Text;
            string password = textBox2.Text;

            bool tmp = false;
            foreach (var item in bindingSource)
            {
                User user = item as User;

                if(user != null)
                {
                    if (name == user.Name && password == user.Password)
                    {
                        user.Login = true;
                        tmp = true;
                        break;
                    }
                }
            }

            if(tmp)
            {
                this.Visible = false;
                form2.ShowDialog();
                this.Close();
            }
            else
            {
                MessageBox.Show("잘못 입력하셨습니다.");
            }
        }

        private void LinkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            MessageBox.Show("기본 비밀번호는 0000입니다.");
        }

        private void LinkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            MessageBox.Show("아이디 등록은 아직 구현중 입니다.");
        }
    }
}
