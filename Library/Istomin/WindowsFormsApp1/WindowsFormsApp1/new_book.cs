using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Npgsql;

namespace WindowsFormsApp1
{
    public partial class new_book : Form
    {
        NpgsqlConnection con;
        public int book_id;
        public string book_name;
        public string author;
        public int year;
        public string publisher;
        public new_book(NpgsqlConnection con, int book_id, string book_name,string author, int year, string publisher)
        {
            this.con = con;
            this.book_id = book_id;
            this.book_name = book_name;
            this.author = author;
            this.year = year;
            this.publisher = publisher;

            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void new_book_Load(object sender, EventArgs e)
        {
            if (this.book_id != -1)
            {
                textBox1.Text = this.book_name;
                textBox2.Text = this.author;
                numericUpDown1.Value = this.year;
                textBox3.Text = this.publisher;
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(this.book_id == -1)
            {
                try
                {
                    string sql = "Insert into library (book_name,author,year,publisher) values (:book_name, :author, :year, :publisher)";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("book_name", textBox1.Text);
                    com.Parameters.AddWithValue("author", textBox2.Text);
                    com.Parameters.AddWithValue("year", numericUpDown1.Value);
                    com.Parameters.AddWithValue("publisher",textBox3.Text);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация сохранена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch (Exception ex){ MessageBox.Show(ex.Message); }
            }
            else
            {
                try
                {
                    string sql = "update library set book_name=:book_name, author=:author, year=:year, publisher=:publisher where book_id=:book_id";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("book_name", textBox1.Text);
                    com.Parameters.AddWithValue("author", textBox2.Text);
                    com.Parameters.AddWithValue("year", numericUpDown1.Value);
                    com.Parameters.AddWithValue("publisher", textBox3.Text);
                    com.Parameters.AddWithValue("book_id", this.book_id);
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

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
