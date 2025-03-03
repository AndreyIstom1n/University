using Npgsql;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp1
{
    public partial class new_student : Form
    {
        NpgsqlConnection con;
        DataTable dt = new DataTable();
        DataSet ds = new DataSet();
        public int student_id;
        public string student_name;
        public string student_surname;
        public string grade;
        public new_student(NpgsqlConnection con, int student_id, string student_name, string student_surname, string grade)
        {
            this.con = con;
            this.student_id = student_id;
            this.student_name = student_name;
            this.student_surname = student_surname;
            this.grade = grade;
            InitializeComponent();
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.student_id == -1)
            {
                try
                {
                    string sql = "Insert into student ( student_name,student_surname,grade) values (:student_name, :student_surname, :grade)";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("student_name", textBox1.Text);
                    com.Parameters.AddWithValue("student_surname", textBox2.Text);
                    com.Parameters.AddWithValue("grade", comboBox1.SelectedValue);
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
                    string sql = "update student set student_name=:student_name, student_surname=:student_surname, grade=:grade where student_id=:student_id";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("student_name", textBox1.Text);
                    com.Parameters.AddWithValue("student_surname", textBox2.Text);
                    com.Parameters.AddWithValue("grade", comboBox1.SelectedValue);
                    com.Parameters.AddWithValue("student_id", this.student_id);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация обновлена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch { }
            }

        }

        private void new_student_Load(object sender, EventArgs e)
        {
            string sql = "Select * from grade";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dt = ds.Tables[0];
            comboBox1.DataSource = dt;
            comboBox1.DisplayMember = "grade_name";
            comboBox1.ValueMember = "grade_name";
            comboBox1.Text = this.grade;
            textBox1.Text = this.student_name;
            textBox2.Text = this.student_surname;
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
