using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace winForm3
{
    public partial class Form1 : Form
    {
        Form2 f2;

        public Form1()
        {
            InitializeComponent();

        }

        private void 도움말정보ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            f2 = new Form2();
            f2.strChange("도움말정보");
            f2.Show();
        }

        private void 새로만들기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            f2 = new Form2();
            f2.strChange("새로만들기");
            f2.Show();
        }

        private void 다른이름으로저장ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            f2 = new Form2();
            f2.strChange("다른이름으로저장");
            f2.Show();
        }
    }
}
