using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Npgsql;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        NpgsqlConnection con;
        public Form1(NpgsqlConnection con)
        {
            this.con= con;
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            books f = new books(con);
            f.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            students f = new students(con);
            f.ShowDialog();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button5_Click(object sender, EventArgs e)
        {
            universitys f = new universitys(con);
            f.ShowDialog();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            contracts f = new contracts(con);
            f.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            report_students f = new report_students(con);
            f.ShowDialog();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            report_books f = new report_books(con);
            f.ShowDialog();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
