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
    public partial class new_cont : Form
    {
        NpgsqlConnection con;
        DataTable dt = new DataTable();
        DataTable dt1 = new DataTable();
        DataSet ds = new DataSet();
        DataSet ds1 = new DataSet();
        public int contract_id;
        public DateTime start1;
        public DateTime end1;
        public string status;
        public int b_id;
        public int s_id;
        public List<string> Statuses { get; set; }
        public new_cont(NpgsqlConnection con, int contract_id, DateTime start1, DateTime end1, string status, int b_id, int s_id)
        {
            this.con = con;
            this.contract_id = contract_id;
            this.start1 = start1;
            this.end1 = end1;
            this.status = status;
            this.b_id = b_id;
            this.s_id = s_id;
            InitializeComponent();
        }
        
        private void new_cont_Load(object sender, EventArgs e)
        {
                string sql = "Select * from library";
                NpgsqlDataAdapter da = new NpgsqlDataAdapter(sql, con);
                ds.Reset();
                da.Fill(ds);
                dt = ds.Tables[0];   
                comboBox1.DisplayMember = "book_name";
                comboBox1.ValueMember = "book_id";
                comboBox1.DataSource = dt;

                string sql1 = "Select * from student";
                NpgsqlDataAdapter da1 = new NpgsqlDataAdapter(sql1, con);
                ds1.Reset();
                da1.Fill(ds1);
                dt1 = ds1.Tables[0];               
                comboBox2.DisplayMember = "student_surname";
                comboBox2.ValueMember = "student_id";
                comboBox2.DataSource = dt1;

                Statuses = new List<string>() { "Получена", "Возвращена (вовремя)", "Возвращена (просрочено)", "Утеряна" };
                comboBox3.DataSource = Statuses;
            comboBox2.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox3.DropDownStyle = ComboBoxStyle.DropDownList;
            dateTimePicker1.Value = this.start1;
            dateTimePicker2.Value = this.end1;
           
            comboBox3.Text = this.status;
            int index = comboBox2.FindStringExact(dt1.AsEnumerable()
                                      .FirstOrDefault(row => row.Field<int>("student_id") == this.s_id)?
                                      .Field<string>("student_surname"));

            int index1 = comboBox1.FindStringExact(dt.AsEnumerable()
                                      .FirstOrDefault(row => row.Field<int>("book_id") == this.b_id)?
                                      .Field<string>("book_name"));
            if (index1 >= 0)
            {
                comboBox1.SelectedIndex = index1;
            }
            else { comboBox1.Text = ""; }
            
            if (index >= 0)
            {
                comboBox2.SelectedIndex = index;
                comboBox3.Enabled = false;

            }
            else { comboBox2.Text = ""; }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.contract_id == -1) 
            {
                try
                {
                    string sql = "Insert into contract (start1, end1, status, b_id, s_id) values (:start1, :end1, :status, :b_id, :s_id)";
                    NpgsqlCommand com = new NpgsqlCommand(sql, con);
                    com.Parameters.AddWithValue("start1", dateTimePicker1.Value);
                    com.Parameters.AddWithValue("end1", dateTimePicker2.Value);
                    com.Parameters.AddWithValue("status", comboBox3.SelectedValue);
                    com.Parameters.AddWithValue("b_id", comboBox1.SelectedValue);
                    com.Parameters.AddWithValue("s_id", comboBox2.SelectedValue);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация сохранена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch (Exception ex)
                { 
                    MessageBox.Show(ex.Message);
                }
             }
            else
            {
                try 
                {
                    string sql = "update contract set start1 =:start1, end1=:end1, b_id=:b_id, s_id=:s_id where contract_id =:contract_id";
                    NpgsqlCommand com = new NpgsqlCommand( sql, con);
                    com.Parameters.AddWithValue("start1", dateTimePicker1.Value);
                    com.Parameters.AddWithValue("end1", dateTimePicker2.Value);
                    com.Parameters.AddWithValue("b_id", comboBox1.SelectedValue);
                    com.Parameters.AddWithValue("s_id", comboBox2.SelectedValue);
                    com.Parameters.AddWithValue("contract_id", this.contract_id);
                    com.ExecuteNonQuery();
                    MessageBox.Show("Информация обновлена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Close();
                }
                catch { }
            }
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
