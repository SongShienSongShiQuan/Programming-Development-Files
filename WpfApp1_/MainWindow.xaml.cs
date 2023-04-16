using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Diagnostics;
using System.Collections;
using System.Threading;
using System.Timers;
using System.Windows.Threading;
using System.Reflection.Emit;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.ResizeMode = ResizeMode.NoResize;
        }
        public void command_on_standby()
        {
            label_a1.Text = "COMMAND ON STANDBY";
            label_a1.Foreground = new SolidColorBrush(Colors.Black);
        }
        private void button_click(object sender, RoutedEventArgs e)
        {
            var process_start_w_command = new ProcessStartInfo();
            process_start_w_command.FileName = "C:/Users/Chowfer/Desktop/CODE SPACE/C# WPF/WpfApp1/bin/Debug/net6.0-windows/start.bat";
            process_start_w_command.UseShellExecute = true;
            process_start_w_command.RedirectStandardOutput = false;
            process_start_w_command.CreateNoWindow = false;
            Process.Start(process_start_w_command);
            label_a1.Foreground = new SolidColorBrush(Colors.Red);
            label_a1.Text = "COMMAND RUNNING...";
            DispatcherTimer timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromSeconds(5);
            timer.Tick += (s, args) =>
            {
                command_on_standby();
                timer.Stop();
            };
            timer.Start();
        }

        private void print_button_click(object sender, RoutedEventArgs e)
        {      
            String input = InputTextBox.Text;
            label_a2.Text = ("PRINTED TEXT: " + input);
        }

    }
}
