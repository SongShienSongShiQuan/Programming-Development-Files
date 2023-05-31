using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.NetworkInformation; //Include this
using System.IO.Enumeration;
using System.Diagnostics;
using System.Runtime.CompilerServices;

namespace Ping_Web_CSharp
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
                Console.WriteLine("--Ping_Web_CSharp--");
                Console.Write("Enter a packet size: ");
                string Packet = Console.ReadLine();
                Console.Write("Enter a URL or IP ADDRESS(NOT LOCAL): ");
                string IP_ADDRESS_INPUT = Console.ReadLine();
                string IP_ADDRESS_Comp_Syn = ":st\npsping -l "+Packet+"m -n 1 "+IP_ADDRESS_INPUT+":80\ngoto :st";
                System.IO.File.WriteAllText("PSPing.bat", IP_ADDRESS_Comp_Syn);
                var process_Web_Ping = new ProcessStartInfo();
                process_Web_Ping.FileName = "PSPing.bat";
                process_Web_Ping.UseShellExecute = true;
                process_Web_Ping.RedirectStandardOutput = false;
                process_Web_Ping.CreateNoWindow = true;
                Process.Start(process_Web_Ping);
            }
            catch
            {
                Console.WriteLine("ERROR: Syntax error or file missing.");
            }
            Console.ReadKey();
        }
    }
}