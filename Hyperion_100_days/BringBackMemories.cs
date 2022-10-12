using System;
using System.Collections.Generic;

namespace BringBackMemories
{
    internal class Program
    {
        static void Main(string[] args)

        {
            List<int> list1 = new List<int>() { 1, 2, 3, 0, 0, 0 };
            List<int> list2 = new List<int>() { 2,5,6 };

            List<int> results = 
                BringBackMemories(list1, 3, list2, 3); 
            Console.WriteLine(string.Join(",", results));
        }

        static List<int> BringBackMemories
            (
            List<int> nums1,int m, List<int> nums2, int n
            )
        {
         
            for (int i = 0; i < m; i++)
            {
                nums1.RemoveAt(m);
            }
            for (int i = 0; i < n; i++)
            {
                nums1.Add(nums2[i]);
            }
            
            nums1.Sort();            
            return nums1;
        }
    }
}