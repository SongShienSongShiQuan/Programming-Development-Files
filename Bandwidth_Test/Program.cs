﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.NetworkInformation; //Include this
using System.IO.Enumeration;
using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;

namespace Bandwidth_Test
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
                Console.WriteLine("Downloading file....");
                int i = 0;
                while (i < 100000)
                {
                    var watch = new Stopwatch();
                    i++;
                    byte[] data;
                    using (var client = new System.Net.WebClient())
                    {
                        watch.Start();
                        data = client.DownloadData("https://songshiensongshiqu.wixsite.com/portfoliot650idev#" + DateTime.Now.Ticks);
                        client.DownloadData("https://songshiensongshiqu.wixsite.com/portfoliot650idev#" + DateTime.Now.Ticks);
                        client.DownloadData("https://songshiensongshiqu.wixsite.com/portfoliot650idev#" + DateTime.Now.Ticks);
                        client.DownloadData("https://songshiensongshiqu.wixsite.com/portfoliot650idev#" + DateTime.Now.Ticks);
                        watch.Stop();
                    }

                    var speed = data.LongLength / watch.Elapsed.TotalSeconds; // instead of [Seconds] property
                    var data_len = data.Length * 4;
                    var speed_output = speed * 4;
                    Console.WriteLine("Download duration: {0}", watch.Elapsed);
                    Console.WriteLine("File size: {0}", data_len.ToString("N0"));
                    Console.WriteLine("Speed: {0} bps ", speed_output.ToString("N0"));
                }

            }
            catch (Exception Error)
            {
                Console.WriteLine(Error);
            }
            Console.ReadKey();
        }
    }
}