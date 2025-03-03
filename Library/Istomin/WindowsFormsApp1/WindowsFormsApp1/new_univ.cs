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
    public partial class new_univ : Form
    {
        NpgsqlConnection con;
        public int grade_id;
        public string grade_name;
        public string grade_classteacher;
        public new_univ(NpgsqlConnection con, int grade_id, string grade_name, string grade_classteacher)
        {
            this.con=con;
            this.grade_id= grade_id;
            this.grade_name= grade_name;
            this.grade_classteacher = grade_classteacher;
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void new_univ_Load(object sender, EventArgs e)
        {
            if (this.grade_id != -1)
            {
                textBox1.Text = this.grade_name;
                textBox2.Text = this.grade_classteacher;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.grade_id == -1)
            {
                try
                {
                    string sql = "Insert into grade (grade_name,grade_classteacher) values (:grade_name, :grade_classteacher)";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("grade_name", textBox1.Text);
                    com.Parameters.AddWithValue("grade_classteacher", textBox2.Text);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация сохранена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch { }
            }
            else
            {
                try
                {
                    string sql = "update grade set grade_name=:grade_name, grade_classteacher=:grade_classteacher where grade_id=:grade_id";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("grade_name", textBox1.Text);
                    com.Parameters.AddWithValue("grade_classteacher", textBox2.Text);
                    com.Parameters.AddWithValue("grade_id", this.grade_id);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация обновлена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch { }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
