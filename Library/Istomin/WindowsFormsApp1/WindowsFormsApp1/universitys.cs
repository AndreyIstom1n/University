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
    public partial class universitys : Form
    {
        NpgsqlConnection con;
        DataTable dt = new DataTable();
        DataSet ds = new DataSet();
        public universitys(NpgsqlConnection con)
        {
            this.con = con;
            InitializeComponent();
        }

        public void update_univ()
        {
            string sql = "Select * from grade";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dt = ds.Tables[0];
            dataGridView1.DataSource = dt;
            dataGridView1.Columns[0].HeaderText = "ID";
            dataGridView1.Columns[1].HeaderText = "Название";
            dataGridView1.Columns[2].HeaderText = "Классный руководитель";
            this.StartPosition = FormStartPosition.CenterScreen;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            adduniv(-1, "", "");
        }
        private void adduniv(int grade_id, string grade_name, string grade_classteacher)
        {
            new_univ f = new new_univ(con, grade_id, grade_name, grade_classteacher);
            f.ShowDialog();
            update_univ();
        }

        private void universitys_Load(object sender, EventArgs e)
        {
            update_univ();
        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            var result = MessageBox.Show("Удалить данную запись?", "Удаление", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                try
                {
                    string sql = "Delete from grade where grade_id=:grade_id";
                    int university_id = (int)dataGridView1.CurrentRow.Cells["grade_id"].Value;
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("grade_id", university_id);
                    com.ExecuteNonQuery();
                }
                catch { MessageBox.Show("Данный Класс числится в таблице 'Ученики'. Перед удалением класса необходимо удалить связанные с ним данные из таблицы 'Ученики'", "Удаление класса", MessageBoxButtons.OK, MessageBoxIcon.Error); }
            }
            update_univ();
        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {
            int university_id = (int)dataGridView1.CurrentRow.Cells[0].Value;
            string university_name = (string)dataGridView1.CurrentRow.Cells[1].Value;
            string address = (string)dataGridView1.CurrentRow.Cells[2].Value;
            adduniv(university_id, university_name, address);
        }
    }
}
