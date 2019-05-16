using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace winForm2
{
    public partial class Form1 : Form
    {
        class MyForm : Form { }

        public Form1()
        {
            InitializeComponent();
            IsMdiContainer = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
     
            MyForm myForm = new MyForm();
            myForm.MdiParent = this;
            myForm.Show();
        }
    }
}
