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
using System.IO;
using System.Media;
using System.Runtime.InteropServices;
using AudioSwitcher.AudioApi.CoreAudio;

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
            WindowStartupLocation = System.Windows.WindowStartupLocation.CenterScreen;
            ///this.Topmost = true;
            ///this.Top = 0;
            ///this.Left = 0;
        }


        [DllImport("user32.dll")]
        public static extern IntPtr GetDC(IntPtr hWnd);

        [DllImport("gdi32.dll")]
        public static extern bool SetDeviceGammaRamp(IntPtr hDC, ref RAMP lpRamp);

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        public struct RAMP
        {
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
            public UInt16[] Red;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
            public UInt16[] Green;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
            public UInt16[] Blue;
        }
        public static void SetGamma(int gamma)
        {
            if (gamma <= 256 && gamma >= 1)
            {
                RAMP Gammma_Ramp = new RAMP();
                Gammma_Ramp.Red = new ushort[256];
                Gammma_Ramp.Green = new ushort[256];
                Gammma_Ramp.Blue = new ushort[256];
                for (int i = 1; i < 256; i++)
                {
                    int iArrayValue = i * (gamma + 256);

                    if (iArrayValue > 65535)
                        iArrayValue = 65535;
                    Gammma_Ramp.Red[i] = Gammma_Ramp.Blue[i] = Gammma_Ramp.Green[i] = (ushort)iArrayValue;
                }
                SetDeviceGammaRamp(GetDC(IntPtr.Zero), ref Gammma_Ramp);
            }
        }


        public void command_on_standby_setup()
        {
            label_a2_sub_1.Text = "COMMAND ON STANDBY";
            label_a2_sub_1.Foreground = new SolidColorBrush(Colors.White);
        }
        public void init_command_setup()
        {
            label_a2_sub_1.Foreground = new SolidColorBrush(Colors.White);
            label_a2_sub_1.Text = "COMMAND RUNNING...";
        }
        public void setup_python(object sender, RoutedEventArgs e)
        {
            var process_start_w_command = new ProcessStartInfo();
            process_start_w_command.FileName = "start_setup.bat";
            process_start_w_command.UseShellExecute = true;
            process_start_w_command.RedirectStandardOutput = false;
            process_start_w_command.CreateNoWindow = false;
            Process.Start(process_start_w_command);
            init_command_setup();
            DispatcherTimer timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromSeconds(5);
            timer.Tick += (s, args) =>
            {
                command_on_standby_setup();
                timer.Stop();
            };
            timer.Start();
        }

        public void print_button_click(object sender, RoutedEventArgs e)
        {
            string contents = "Hello Mako & Shiro.";
            System.IO.File.WriteAllText("WpfApp1_data.txt", contents);
            String input = InputTextBox.Text;
            String input_int = InputIntBox.Text;
            int input_int_to_int = int.Parse(input_int);
            //int myInt = 123;
            //string myString = myInt.ToString();
            SetGamma(input_int_to_int);
            label_a1.Text = ("PRINTED TEXT: " + input);
            List<int> Numbers_list = new List<int>() { 25, 59, 55 };
            Numbers_list.Add(input_int_to_int);
            string Numbers_list_to_str = string.Join(",", Numbers_list);
            label_a1_sub_1.Text = "LIST: " + Numbers_list_to_str;
        }
        public void command_on_standby_modules()
        {
            label_a3_sub_1.Text = "COMMAND ON STANDBY";
            label_a3_sub_1.Foreground = new SolidColorBrush(Colors.White);
        }
        public void init_command_modules()
        {
            label_a3_sub_1.Foreground = new SolidColorBrush(Colors.White);
            label_a3_sub_1.Text = "COMMAND RUNNING...";
        }
        public void Run_Python_Modules(object sender, RoutedEventArgs e)
        {
            var process_start_w_command = new ProcessStartInfo();
            process_start_w_command.FileName = "Python_Modules.bat";
            process_start_w_command.UseShellExecute = true;
            process_start_w_command.RedirectStandardOutput = false;
            process_start_w_command.CreateNoWindow = false;
            Process.Start(process_start_w_command);
            init_command_modules();
            DispatcherTimer timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromSeconds(5);
            timer.Tick += (s, args) =>
            {
                command_on_standby_modules();
                timer.Stop();
            };
            timer.Start();
        }
        public void KEY_DETECT(object sender, KeyEventArgs e)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                if (e.Key == Key.T)
                {
                    init_command_setup();
                    DispatcherTimer timer = new DispatcherTimer();
                    timer.Interval = TimeSpan.FromSeconds(5);
                    timer.Tick += (s, args) =>
                    {
                        command_on_standby_setup();
                        timer.Stop();
                    };
                    timer.Start();
                }
                else if (e.Key == Key.Add)
                {
                    CoreAudioDevice device = new CoreAudioController().DefaultPlaybackDevice;
                    device.Volume += 10;
                    label_a4_sub_2.Text = ("VOL:" + device.Volume);
                }
                else if (e.Key == Key.Subtract)
                {
                    CoreAudioDevice device = new CoreAudioController().DefaultPlaybackDevice;
                    device.Volume -= 10;
                    label_a4_sub_2.Text = ("VOL:" + device.Volume);
                }
            }
        }

        public void volume_set_add(object sender, RoutedEventArgs e)
        {
            CoreAudioDevice device = new CoreAudioController().DefaultPlaybackDevice;
            device.Volume += 10;
            label_a4_sub_2.Text = ("VOL:" + device.Volume);
        }
        public void volume_set_sub(object sender, RoutedEventArgs e)
        {
            CoreAudioDevice device = new CoreAudioController().DefaultPlaybackDevice;
            device.Volume -= 10;
            label_a4_sub_2.Text = ("VOL:" + device.Volume);
        }
        public void gamma_set_value(object sender, RoutedEventArgs e)
        {
            string input_int_gamma = InputIntBox_Gamma.Text;
            label_a5_sub_1.Text = ("VALUE: " + input_int_gamma);
            int input_int_gamma_to_int = int.Parse(input_int_gamma);
            SetGamma(input_int_gamma_to_int);
        }
        public void gamma_add(object sender, RoutedEventArgs e)
        {
            string input_int_gamma = InputIntBox_Gamma.Text;
            int input_int_gamma_to_int = int.Parse(input_int_gamma);
            int add_gamma_value = (input_int_gamma_to_int + 30);
            string add_gamma_value_to_str = add_gamma_value.ToString();
            InputIntBox_Gamma.Text = add_gamma_value_to_str;
            label_a5_sub_1.Text = ("VALUE: " + add_gamma_value_to_str);
            SetGamma(add_gamma_value);
        }
        public void gamma_sub(object sender, RoutedEventArgs e)
        {
            string input_int_gamma = InputIntBox_Gamma.Text;
            int input_int_gamma_to_int = int.Parse(input_int_gamma);
            int sub_gamma_value = (input_int_gamma_to_int - 30);
            string sub_gamma_value_to_str = sub_gamma_value.ToString();
            InputIntBox_Gamma.Text = sub_gamma_value_to_str;
            label_a5_sub_1.Text = ("VALUE: " + sub_gamma_value_to_str);
            SetGamma(sub_gamma_value);
        }
    }
}
