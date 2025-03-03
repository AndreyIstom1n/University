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
    public partial class lost_book : Form
    {
        NpgsqlConnection con;
        DataTable dt = new DataTable();
        DataSet ds = new DataSet();
        public lost_book(NpgsqlConnection con)
        {
            this.con = con;
            InitializeComponent();
        }
        public void update_lost()
        {
            string sql = "SELECT s.student_id, s.student_name, s.student_surname, con.b_id, lib.book_name FROM contract con JOIN student s ON con.s_id = s.student_id JOIN library lib ON con.b_id = lib.book_id WHERE con.status = 'Утеряна'";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dt = ds.Tables[0];
            dataGridView1.DataSource = dt;
            dataGridView1.Columns[0].HeaderText = "ID студента";
            dataGridView1.Columns[1].HeaderText = "Имя";
            dataGridView1.Columns[2].HeaderText = "Фамилия";
            dataGridView1.Columns[3].HeaderText = "ID книги";
            dataGridView1.Columns[4].HeaderText = "Стоимость";
        }

        private void lost_book_Load(object sender, EventArgs e)
        {
            update_lost();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
