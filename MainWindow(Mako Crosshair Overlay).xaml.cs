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

namespace Mako_Crosshair_Overlay
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public static class Globals
        {
            public static string duplicate_preventer = "false";
        }
        public MainWindow()
        {
            InitializeComponent();
            ///this.ResizeMode = ResizeMode.NoResize;
            WindowStartupLocation = System.Windows.WindowStartupLocation.CenterScreen;
            this.Topmost = true;
            this.Top = 0;
            this.Left = 0;
        }
        public void KEY_DETECT(object sender, KeyEventArgs e)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                if (e.Key == Key.T) 
                {
                    if (Globals.duplicate_preventer == "false")
                    {
                        Globals.duplicate_preventer = "true";
                        Set_Opacity.Opacity = 1;
                        PRINT.Text = Globals.duplicate_preventer;
                    }
                    else if (Globals.duplicate_preventer == "true")
                    {
                        Globals.duplicate_preventer = "false";
                        Set_Opacity.Opacity = 0;
                        PRINT.Text = Globals.duplicate_preventer;
                    }
                } 
            }
        }
        public void KEY_DETECT_AGAIN(object sender, KeyEventArgs e)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                if (e.Key == Key.T)
                {
                    if (Globals.duplicate_preventer == "true")
                    {
                        Globals.duplicate_preventer = "false";
                        Set_Opacity.Opacity = 0;
                        PRINT.Text = Globals.duplicate_preventer;
                    }
                }
            }
        }
        public void KEY_DETECT_DEBUG(object sender, KeyEventArgs e)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                if (e.Key == Key.R)
                {
                    PRINT.Text = Globals.duplicate_preventer;
                }
            }
        }
    }
}
