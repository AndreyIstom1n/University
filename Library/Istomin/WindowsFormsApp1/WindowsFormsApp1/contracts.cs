using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Contracts;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Npgsql;
namespace WindowsFormsApp1
{
    public partial class contracts : Form
    {
        public NpgsqlConnection con;
        DataTable dt = new DataTable();
        DataSet ds = new DataSet();
        public contracts(NpgsqlConnection con)
        {
            this.con = con;
            InitializeComponent();
        }

        public void update_cont()
        {
            string sql = "select * from contract";
            NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
            ds.Reset();
            da.Fill(ds);
            dt = ds.Tables[0];
            dataGridView1.DataSource = dt;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dataGridView1.Columns[0].HeaderText = "ID";
            dataGridView1.Columns[1].HeaderText = "Дата получения книги";
            dataGridView1.Columns[2].HeaderText = "Дата возврата книги";
            dataGridView1.Columns[3].HeaderText = "Статус";
            dataGridView1.Columns[4].HeaderText = "ID книги";
            dataGridView1.Columns[5].HeaderText = "ID студента";
            
            this.StartPosition = FormStartPosition.CenterScreen;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }
        private void addcont(int contract_id, DateTime start1, DateTime end1, string status, int b_id, int s_id)
        {
            new_cont f = new new_cont(con, contract_id, start1, end1, status, b_id, s_id);
            f.ShowDialog();
            update_cont();
        }
        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            addcont(-1, DateTime.Today, DateTime.Today, "", 0, 0);
        }

        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {
        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            var result = MessageBox.Show("Удалить данную запись?", "Удаление", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                string sql = "Delete from contract where contract_id=:contract_id";
                int contract_id = (int)dataGridView1.CurrentRow.Cells["contract_id"].Value;
                NpgsqlCommand com = new NpgsqlCommand(sql, con);
                com.Parameters.AddWithValue("contract_id", contract_id);
                com.ExecuteNonQuery();
            }
            update_cont();
        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {
            int contract_id = (int)dataGridView1.CurrentRow.Cells[0].Value;
            DateTime start1 = (DateTime)dataGridView1.CurrentRow.Cells[1].Value;
            DateTime end1 = (DateTime)dataGridView1.CurrentRow.Cells[2].Value;
            string status = (string)dataGridView1.CurrentRow.Cells[3].Value;
            int b_id = (int)dataGridView1.CurrentRow.Cells[4].Value;
            int s_id = (int)dataGridView1.CurrentRow.Cells[5].Value;
            addcont(contract_id, start1, end1, status, b_id, s_id);
        }

        private void contracts_Load(object sender, EventArgs e)
        {
            update_cont();
        }

        private void toolStripLabel4_Click(object sender, EventArgs e)
        {
            try
            {
                int contract_id = (int)dataGridView1.CurrentRow.Cells[0].Value;
                DateTime start1 = (DateTime)dataGridView1.CurrentRow.Cells[1].Value;
                DateTime end1 = (DateTime)dataGridView1.CurrentRow.Cells[2].Value;
                string status = (string)dataGridView1.CurrentRow.Cells[3].Value;
                int b_id = (int)dataGridView1.CurrentRow.Cells[4].Value;
                int s_id = (int)dataGridView1.CurrentRow.Cells[5].Value;
                upd z = new upd(con, contract_id, start1, end1, status, b_id, s_id);
                z.ShowDialog();
                update_cont();
            }
            catch { }
        }
    }
}
