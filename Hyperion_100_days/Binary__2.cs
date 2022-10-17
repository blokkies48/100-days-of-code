using System;

namespace Binary___2_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Boilerplate just to print results to console
            // And calling functions
            int[] randomB = RandomNumberGenerator(3, 5);
            Console.WriteLine("This is the input arry");
            foreach (int j in randomB)
            {
                
                Console.Write(j + " ");
            }
            Console.WriteLine();
            Array.Sort(randomB);
            int[] sortedB = SortedArray(randomB);
            Console.WriteLine("This is the output arry");
            foreach (int j in sortedB)
            {

                Console.Write(j + " ");
            }
            Console.WriteLine() ;

        }

        // Made a random num generator to keep it interesting
        static int[] RandomNumberGenerator(int max, int length)
        {
            int[] arryb = new int[length];

            Random randNum = new Random();
            for (int i = 0; i < arryb.Length; i++)
            {
                arryb[i] = randNum.Next(0, max);
            }

            return arryb;
        }
        // Created own sorting function very stantard type of thing you memorize
        static int[] SortedArray(int[] arry)
        {
            // Works by looping over the arry initially
            int placeHolder;
            for(int i = 0; i < arry.Length; i++)
            {
                // Then loops over it again
                for(int j = 0; j < arry.Length; j++)
                {
                    // Checks if the top loops value is less than the second loop's value
                    if (arry[i] < arry[j]) 
                    {
                        // Then it just reassigns values 
                        placeHolder = arry[i];
                        arry[i] = arry[j]; // This will basically remove the value from the list
                        arry[j] = placeHolder;// This will insert the value where needed
                        // In python you will have 2 list where you will remove then append that value
                        // This is similar but arrays are can't be changed
                        // https://www.c-sharpcorner.com/blogs/sort-array-in-c-sharp-without-using-inbuilt-function
                    }
                }
               
            }
            return arry;
        }
    }
}