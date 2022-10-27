using System;

namespace VariableLearningPrac
{
    public class Program{
        public static void Main(){
            bool data=true;
            Console.WriteLine("Before Negation {0}",data);
            data=!data;
            Console.WriteLine("Before Negation {0}",data);

            int preInc=0;
            int postInc=0;

            Console.WriteLine("Pre : {0}",++preInc);
            Console.WriteLine("Post : {0}",postInc++);
        }
    }
}

// https://csharp-station.com/Tutorial/CSharp/Lesson02


// using System;

// class Unary
// {
//     public static void Main()
//     {
//         int unary = 0;
//         int preIncrement;
//         int preDecrement;
//         int postIncrement;
//         int postDecrement;
//         int positive;
//         int negative;
//         sbyte bitNot;
//         bool logNot;

//         preIncrement = ++unary;
//         Console.WriteLine("pre-Increment: {0}", preIncrement);

//         preDecrement = --unary;
//         Console.WriteLine("pre-Decrement: {0}", preDecrement);

//         postDecrement = unary--;
//         Console.WriteLine("Post-Decrement: {0}", postDecrement);

//         postIncrement = unary++;
//         Console.WriteLine("Post-Increment: {0}", postIncrement);

//         Console.WriteLine("Final Value of Unary: {0}", unary);

//         positive = -postIncrement;
//         Console.WriteLine("Positive: {0}", positive);

//         negative = +postIncrement;
//         Console.WriteLine("Negative: {0}", negative);

//         bitNot = 0;
//         bitNot = (sbyte)(~bitNot);
//         Console.WriteLine("Bitwise Not: {0}", bitNot);

//         logNot = false;
//         logNot = !logNot;
//         Console.WriteLine("Logical Not: {0}", logNot);
//     }
// }