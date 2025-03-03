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
    public partial class students : Form
    {
        NpgsqlConnection con;
        DataTable dt=new DataTable();
        DataSet ds = new DataSet();
        public students(NpgsqlConnection con)
        {
            this.con = con;
            InitializeComponent();
        }

        public void update_stud()
        {
            string sql = "Select * from student";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dt= ds.Tables[0];
            dataGridView1.DataSource = dt;
            dataGridView1.Columns[0].HeaderText = "ID";
            dataGridView1.Columns[1].HeaderText = "Имя";
            dataGridView1.Columns[2].HeaderText = "Фамилимя";
            dataGridView1.Columns[3].HeaderText = "Класс";
            this.StartPosition= FormStartPosition.CenterScreen;
        }
        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            addstud(-1, "","", "");
        }

        private void students_Load(object sender, EventArgs e)
        {
            update_stud();
        }
        private void addstud(int student_id,string student_name, string student_surname, string univer)
        {
            new_student f = new new_student(con, student_id, student_name, student_surname, univer);
            f.ShowDialog();
            update_stud();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            var result = MessageBox.Show("Удалить данную запись?", "Удаление", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                try {
                    string sql = "Delete from student where student_id=:student_id";
                    int student_id = (int)dataGridView1.CurrentRow.Cells["student_id"].Value;
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("student_id", student_id);
                    com.ExecuteNonQuery();
                }
                catch { MessageBox.Show("Данный студент числится в таблице 'Получение/Возврат книг'. Перед удалением студента необходимо удалить связанные с ним данные из таблицы 'Получение/Возврат книг'","Удаление студента",MessageBoxButtons.OK,MessageBoxIcon.Error); }
                }
            update_stud();
        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {
            int student_id = (int)dataGridView1.CurrentRow.Cells[0].Value;
            string student_name = (string)dataGridView1.CurrentRow.Cells[1].Value;
            string student_surname = (string)dataGridView1.CurrentRow.Cells[2].Value;
            string grade = (string)dataGridView1.CurrentRow.Cells[3].Value;
            addstud(student_id, student_name, student_surname, grade);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            lost_book f = new lost_book(con);
            f.ShowDialog();
        }
    }
}
