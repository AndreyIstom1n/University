using Npgsql;
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

namespace WindowsFormsApp1
{
    public partial class books : Form
    {
        public NpgsqlConnection con;
        DataTable dt=new DataTable();
        DataSet ds = new DataSet();
        public books(NpgsqlConnection con)
        {
            this.con=con;
            InitializeComponent();
        }
        public void update_book ()
        {
            String sql = "Select * from library";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dt = ds.Tables[0];
            dataGridView1.DataSource = dt;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dataGridView1.Columns[0].HeaderText = "ID";
            dataGridView1.Columns[1].HeaderText = "Название";
            dataGridView1.Columns[2].HeaderText = "Автор";
            dataGridView1.Columns[3].HeaderText = "Год издания";
            dataGridView1.Columns[4].HeaderText = "Издание";
            this.StartPosition = FormStartPosition.CenterScreen;
        }
        private void addbook(int book_id, string book_name, string author, int year, string publisher)
        {
            new_book f = new new_book(con, book_id, book_name, author, year, publisher);
            f.ShowDialog();
            update_book();
        }
        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            addbook(-1, "", "",0,"");
        }

        private void books_Load(object sender, EventArgs e)
        {
            update_book();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            var result = MessageBox.Show("Удалить данную запись?","Удаление", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                try {
                    string sql = "Delete from library where book_id=:book_id";
                    int book_id = (int)dataGridView1.CurrentRow.Cells["book_id"].Value;
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("book_id", book_id);
                    com.ExecuteNonQuery();
                }
                catch { MessageBox.Show("Данная книга числится в таблице 'Получение/Возврат книг'. Перед удалением книги необходимо удалить связанные с ней данные из таблицы 'Получение/Возврат книг'", "Удаление книги", MessageBoxButtons.OK, MessageBoxIcon.Error); }
            }
            update_book();
        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {
            int book_id = (int)dataGridView1.CurrentRow.Cells[0].Value;
            string book_name = (string)dataGridView1.CurrentRow.Cells[1].Value;
            string author = (string)dataGridView1.CurrentRow.Cells[2].Value;
            int year = (int)dataGridView1.CurrentRow.Cells[3].Value;
            string publisher= (string)dataGridView1.CurrentRow.Cells[4].Value;
            addbook(book_id,book_name,author,year,publisher);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
