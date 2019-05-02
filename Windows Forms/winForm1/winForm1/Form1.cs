using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace winForm1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void button1_Click(object sender, EventArgs e)
        {
            string str = textBox1.Text;

            try
            {
                int tmp = int.Parse(textBox1.Text);
                label1.Text = (tmp * 2.54) + " cm";
            }
            catch (FormatException)
            {
                MessageBox.Show("숫자만 입력하세요", "오류", MessageBoxButtons.RetryCancel);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string str = textBox2.Text;

            try
            {
                int tmp = int.Parse(textBox2.Text);
                label2.Text = (int)(tmp * 0.453592) + " kg";
            }
            catch (FormatException)
            {
                MessageBox.Show("숫자만 입력하세요", "오류", MessageBoxButtons.RetryCancel);
            }
        }
        
    }
}
