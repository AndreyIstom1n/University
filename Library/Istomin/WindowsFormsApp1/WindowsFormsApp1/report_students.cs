using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Diagnostics.Contracts;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Office.Interop.Excel;
using Npgsql;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
namespace WindowsFormsApp1
{
    public partial class report_students : Form
    {
        System.Data.DataTable dt = new System.Data.DataTable();
        DataSet ds = new DataSet();
        System.Data.DataTable dt1 = new System.Data.DataTable();
        DataSet ds1 = new DataSet();
        NpgsqlConnection con;
        List<string> list = new List<string>();
        public report_students(NpgsqlConnection con)
        {
            this.con= con;
            InitializeComponent();
        }
        public void update_report()
        {
            
            try
            {

                //string sql = "select s.student_id, s.student_name, s.student_surname, s.univer, u.university_name, con.contract_id, con.status, con.end1, con.s_id " +
                //             "from contract con " +
                //             "join student s on con.s_id = s.student_id " +
                //             "join university u on s.univer = u.university_name " +
                //             "where con.status LIKE '%Возвращена (просрочено)%' and con.end1 < :select_end1 and s.univer = ANY(:select_univer)";
                string sql = @"WITH RankedContracts AS ( SELECT s.student_id, s.student_name, s.student_surname, s.grade, g.grade_name, con.contract_id, con.status, con.end1, con.s_id, ROW_NUMBER() OVER (PARTITION BY s.student_id ORDER BY con.contract_id) AS rn FROM contract con JOIN student s ON con.s_id = s.student_id JOIN grade g ON s.grade = g.grade_name WHERE con.status LIKE '%Возвращена (просрочено)%' AND con.end1 <:select_end1 AND s.grade = ANY(:select_univer)) SELECT student_id, student_name, student_surname, grade, grade_name, contract_id, status, end1, s_id FROM RankedContracts WHERE rn = 1;";

                for (int i = 0; i < checkedListBox1.CheckedItems.Count; i++)
                {
                    list.Add(checkedListBox1.CheckedItems[i].ToString());
                }
                NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
                da.SelectCommand.Parameters.AddWithValue("select_end1", dateTimePicker1.Value.Date);
                da.SelectCommand.Parameters.AddWithValue("select_univer", list.ToArray());
                da.Fill(ds);
                dt = ds.Tables[0];


                    dataGridView1.DataSource = dt;
                    dataGridView1.Columns[0].HeaderText = "ID студента";
                    dataGridView1.Columns[1].HeaderText = "Имя студента";
                    dataGridView1.Columns[2].HeaderText = "Фамилия студента";
                    dataGridView1.Columns[3].HeaderText = "Класс";
                    dataGridView1.Columns[4].Visible = false;
                    dataGridView1.Columns[5].Visible = false;
                    dataGridView1.Columns[6].Visible = false;
                    dataGridView1.Columns[7].Visible = false;
                    dataGridView1.Columns[8].Visible = false;
                    this.StartPosition = FormStartPosition.CenterScreen;
                }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
        }
       

        private void button3_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void report_students_Load(object sender, EventArgs e)
        {
            string sql12 = "select grade_name from grade";
            NpgsqlCommand cmd1 = new NpgsqlCommand(sql12, con);
            NpgsqlDataReader reader1 = cmd1.ExecuteReader();

            while (reader1.Read())
            {
                string select_univer = reader1["grade_name"].ToString();
                checkedListBox1.Items.Add(select_univer);
            }
            reader1.Close();


            update_report();
        }

        private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            update_report();
            if (checkedListBox1.CheckedItems.Count == 0) 
            {
                dataGridView1.DataSource = null;       
            }
            button1.Visible = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try {

                Microsoft.Office.Interop.Excel.Application excelObj = new Microsoft.Office.Interop.Excel.Application();

                Workbook wb = excelObj.Workbooks.Add(XlWBATemplate.xlWBATWorksheet);
                Worksheet wsh = (Worksheet)wb.Sheets[1];
                excelObj.Visible = true;
                for (int i = 1; i < 5; i++)
                {
                    wsh.Cells[1, i] = dataGridView1.Columns[i - 1].HeaderText;
                    wsh.Columns[i].AutoFit();
                }
                for (int i = 0; i < dataGridView1.Rows.Count-1; i++)
                {
                    for (int j = 0; j < dataGridView1.Columns.Count - 5; j++)
                    {

                        wsh.Cells[i + 2, j + 1] = dataGridView1.Rows[i].Cells[j].Value.ToString();
                        wsh.Columns[i + 2].AutoFit();
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
            catch (Exception ex)
            { MessageBox.Show(ex.Message); }
            }

        private void button4_Click(object sender, EventArgs e)
        {try {
                dataGridView1.DataSource = null;
            }
            catch (Exception ex) {  MessageBox.Show(ex.Message); }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
