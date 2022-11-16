using System;

namespace Asma_Elbaik_Oreivation
{
    class Program
    {


        static void Main(string[] args)
        {
            int nJobs;
            int ninstance;

            

            do
            {
                Console.WriteLine("Please enter the number of jobs in the day");
                nJobs = Convert.ToInt32(Console.ReadLine());
            } while (0 > nJobs && nJobs > 10000);

            //lets say the number of instance of each job is 5

            int[][] startTime = new int[nJobs][];
            int[][] endTime = new int[nJobs][];
            int[][] profit = new int[nJobs][];
            int[] sum = new int[nJobs];

            for (int j = 0; j < nJobs; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    do
                    {
                        Console.WriteLine("Please entre the start time for the job number "+ j);
                        startTime[j][i] = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("Please entre the end time the job number " + j );
                        endTime[j][i] = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("Please entre the profit the job number " + j);
                        profit[j][i] = Convert.ToInt32(Console.ReadLine());

                    } while (endTime[j][i] < startTime[j][i]);

                    if (!(startTime[j][i] < startTime[j][i + 1] < endTime[j][i])){

                        sum[j] = profit[j][i] + profit[j][i + 1];
                    }


                }
                    Console.WriteLine("the sum profit for job"+j+"is"+ sum);
                     
            }



        }
    }
}
