using System.Windows;
using System.Windows.Input;

namespace KeyboardTrapping
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private void Window_PreviewKeyDown(object sender, KeyEventArgs e)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                if (e.Key == Key.G) MessageBox.Show("Ctrl+G or Ctrl+g", "Keyboard Trapping Demo");
                if (e.Key == Key.T) MessageBox.Show("Ctrl+T or Ctrl+t", "Keyboard Trapping Demo");
            }
            if (Keyboard.IsKeyDown(Key.LeftAlt) || Keyboard.IsKeyDown(Key.RightAlt))
            {
                if (e.Key == Key.G) MessageBox.Show("Alt+G or Alt+g", "Keyboard Trapping Demo");
                if (e.Key == Key.T) MessageBox.Show("Alt+T or Alt+t", "Keyboard Trapping Demo");
            }
            // ... Test for right or left arrow keys and equate those to
            // clicking the right or left arrow buttons.
            // do not forget PreviewKeyDown="Window_PreviewKeyDown" in the XAML.
            if (e.Key == Key.Right) btnRightArrow_Click(sender, e);
            if (e.Key == Key.Left) MessageBox.Show("left arrow key", "Keyboard Trapping Demo");
            // test for other keys
            if (e.Key == Key.A) MessageBox.Show("A or a", "Keyboard Trapping Demo");
            if (e.Key == Key.F2) MessageBox.Show("F2", "Keyboard Trapping Demo");
            if (e.Key == Key.D7) MessageBox.Show("7", "Keyboard Trapping Demo");
            if (e.Key == Key.Space) MessageBox.Show("Space", "Keyboard Trapping Demo");
        }
        private void btnRightArrow_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("You clicked the right arrow button or the right arrow key. " +
                "Thanks for your patronage. Please come again.", "Keyboard Trapping Demo");
        }
        private void OnKeyDownHandler(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Return)
            {
                txtblk.Text = "You Entered: " + txtbox.Text;
            }
        }
    }
}