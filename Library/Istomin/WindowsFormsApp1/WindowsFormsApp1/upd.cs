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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
namespace WindowsFormsApp1
{
    public partial class upd : Form
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
        public upd(NpgsqlConnection con, int contract_id, DateTime start1, DateTime end1, string status, int b_id, int s_id)
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

        private void upd_Load(object sender, EventArgs e)
        {
            Statuses = new List<string>() { "Получена", "Возвращена (вовремя) ", "Возвращена (просрочено) ", "Утеряна" };
            comboBox1.DataSource = Statuses;;
            //comboBox1.SelectedText = (this.status);
            comboBox1.Text = this.status;
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            try
            {
                dateTimePicker1.Value=DateTime.Now;
                string dtp = dateTimePicker1.Text;
                string res;
                string sql = "update contract set status=:status where contract_id =:contract_id";
                if (comboBox1.SelectedValue.ToString().Contains("Возвращена"))
                {
                    res = comboBox1.SelectedValue.ToString() + dtp;
                }
                else { res = comboBox1.SelectedValue.ToString(); }
                NpgsqlCommand com = new NpgsqlCommand(sql, con);
                com.Parameters.AddWithValue("status", res);
                com.Parameters.AddWithValue("contract_id", this.contract_id);
                com.ExecuteNonQuery();
                MessageBox.Show("Информация обновлена", "Выполнение функции", MessageBoxButtons.OK, MessageBoxIcon.Information);
                Close();

            }
            catch { MessageBox.Show("Невозможно изменить статус! Пустое значение таблицы.", "Изменение статуса", MessageBoxButtons.OK, MessageBoxIcon.Error); }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }
    }
}
