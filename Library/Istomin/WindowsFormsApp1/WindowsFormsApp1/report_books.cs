using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Office.Interop.Excel;
using Npgsql;
using DGVPrinterHelper;
namespace WindowsFormsApp1
{
    public partial class report_books : Form
    {
        System.Data.DataTable dt = new System.Data.DataTable();
        DataSet ds = new DataSet();
        NpgsqlConnection con;
        public report_books(NpgsqlConnection con)
        {
            this.con = con;
            InitializeComponent();
        }


        public void update_report2()
        {
            try
            {
                string sql = "SELECT s.grade, COUNT(CASE WHEN con.status = 'Получена' THEN 1 END) AS IssuedBooks, COUNT(CASE WHEN con.status LIKE '%Возвращена (просрочено)%' THEN 1 END) AS NotReturnedBooks, COUNT(CASE WHEN con.status = 'Утеряна' THEN 1 END) AS LostBooks FROM contract con JOIN student s ON con.s_id = s.student_id JOIN grade g ON s.grade = g.grade_name JOIN library lib ON con.b_id = lib.book_id where con.end1 >=:begin and con.end1<=:end2 GROUP BY s.grade;";               
                NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
                da.SelectCommand.Parameters.AddWithValue("begin", dateTimePicker1.Value.Date);
                da.SelectCommand.Parameters.AddWithValue("end2", dateTimePicker2.Value.Date);
                ds.Reset();
                da.Fill(ds);
                dt = ds.Tables[0];
                dataGridView1.DataSource = dt;
                dataGridView1.Columns[0].HeaderText = "Класс";
                dataGridView1.Columns[1].HeaderText = "Выдано книг";
                dataGridView1.Columns[2].HeaderText = "Возвращено книг (просрочено)";
                dataGridView1.Columns[3].HeaderText = "Утеряно книг";
                this.StartPosition = FormStartPosition.CenterScreen;
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
        }
        private void report_books_Load(object sender, EventArgs e)
        {
            button4.Visible = false;
            button1.Visible = false;
            dataGridView1.Visible = false;
            update_report2();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            update_report2();
            button3.Visible = false;
            button4.Visible = true;
            dataGridView1.Visible = true;
            button1.Visible = true;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Microsoft.Office.Interop.Excel.Application excelObj = new Microsoft.Office.Interop.Excel.Application();

            Workbook wb = excelObj.Workbooks.Add(XlWBATemplate.xlWBATWorksheet);
            Worksheet wsh = (Worksheet)wb.Sheets[1];
            excelObj.Visible = true;
            for (int i = 1; i <= dataGridView1.Columns.Count; i++)
            {
                wsh.Cells[1, i] = dataGridView1.Columns[i - 1].HeaderText;
                wsh.Columns[i].AutoFit();
            }
            for (int i = 0; i < dataGridView1.Rows.Count - 1; i++)
            {
                for (int j = 0; j < dataGridView1.Columns.Count; j++)
                {
                    wsh.Cells[i + 2, j + 1] = dataGridView1.Rows[i].Cells[j].Value?.ToString() ?? "";
                    wsh.Columns[j + 1].AutoFit();
                }
            }
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "Excel Files|*.xlsx";
            sfd.Title = "Сохранить как Excel файл";
            if (sfd.ShowDialog() == DialogResult.OK)
            {
                wb.SaveAs(sfd.FileName);
            }
            wb.Close();
            excelObj.Quit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DGVPrinter dgv = new DGVPrinter();
            dgv.CreateReport("Отчет о книгах", dataGridView1);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
                
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
