using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.NetworkInformation; //Include this
using System.IO.Enumeration;
using System.Diagnostics;
using System.Runtime.CompilerServices;

namespace PingProto
{
    public class Program
    {

        static void Main()
        {
            System.Diagnostics.ProcessStartInfo ON_START = new System.Diagnostics.ProcessStartInfo();
            ON_START.WindowStyle = System.Diagnostics.ProcessWindowStyle.Minimized;
            ON_START.CreateNoWindow = true;
            try
            {
                var process_start_command = new ProcessStartInfo();
                process_start_command.FileName = "IP_netsh.bat";
                process_start_command.UseShellExecute = true;
                process_start_command.RedirectStandardOutput = false;
                process_start_command.CreateNoWindow = false;
                process_start_command.Verb = "runas";
                Process.Start(process_start_command);
            }
            catch
            {
                Console.WriteLine("ERROR: IP_ADDRESS can't be changed, incorrect syntax, or batch file missing.");
            }
            Console.ReadKey();
        }
    }
}