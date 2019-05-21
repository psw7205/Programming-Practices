using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace winForm4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            List<string> list = new List<string>();

            foreach (var item in Controls)
            {
                if (item is CheckBox)
                {
                    CheckBox checkBox = (CheckBox)item;
                    if (checkBox.Checked)
                    {
                        list.Add(checkBox.Text);
                    }
                }
            }

            string str = string.Join(",", list);
            if (str == "")
                label1.Text = "label1";
            else
                label1.Text = str;
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            List<string> list = new List<string>();

            foreach (var items in Controls)
            {
                if (items is GroupBox)
                {
                    foreach (var item in ((GroupBox)items).Controls)
                    {
                        RadioButton rbtn = item as RadioButton;
                        if (rbtn != null && rbtn.Checked)
                        {
                            list.Add(rbtn.Text);
                        }
                    }
                }
            }

            string str = string.Join(",", list);
            if (str == "")
                label2.Text = "label2";
            else
                label2.Text = str;
        }
    }
}
