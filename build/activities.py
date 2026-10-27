# Each activity: id, title, instructions, starter, check (JS function body: (out, v, code) -> {ok,msg}),
# solution (reference, Python 2 syntax like the lesson), wrong (an attempt that should be rejected), trinket ids it replaces.
A = []
def add(**k): A.append(k)

add(id="l1-sample-program", lesson=1, trinket=["7b26a963d21f"], title="Sample Python Program",
 instr="Press <b>Run</b> to see what this program does. Then press <b>Check</b>.",
 starter='''# This is a sample Python program.
# Lines that start with # are comments - Python ignores them.
print "Hello, World!"
print "Python can do math too. 7 times 6 is", 7 * 6
''',
 check='''if(!out.trim()) return {ok:false,msg:"Nothing was printed yet. Press Run, or make sure your program has a print line."};
return {ok:true,msg:"It works! Python ran each line from top to bottom and printed the results."};''',
 solution=None, wrong='# print "Hello"\n')

add(id="l1-printing", lesson=1, trinket=["2d95fffc8305"], title="Try it: Printing",
 instr='Write a <code>print</code> statement that displays your favourite number or a greeting message. Text goes inside double quotations " ".',
 starter='''# Write your print statement below this line

''',
 check='''if(!/\\bprint\\b/.test(code)) return {ok:false,msg:"Use the word print (all lowercase - Python is case sensitive!)."};
if(!out.trim()) return {ok:false,msg:"Your program didn't display anything yet. Try: print \\"Hello!\\""};
return {ok:true,msg:"Great! Your program printed: " + out.trim().split("\\n")[0]};''',
 solution='print "Hello, Grade 9 Math!"\nprint 7\n', wrong='# print "Hi"\n')

add(id="l1-variables", lesson=1, trinket=["e63dfa4f002d"], title="Try it: Variables",
 instr="Edit the code below to include <b>your</b> name and age, then print them in a sentence.",
 starter='''# Change the values to your own name and age
name = "Alex"
age = 14

print "Hello, my name is", name
print "I am", age, "years old"
''',
 check='''if(typeof v.name!=="string") return {ok:false,msg:"Make sure you still have a variable called name that stores text in quotes, e.g. name = \\"Sam\\"."};
if(typeof v.age!=="number") return {ok:false,msg:"age should store a number (no quotes), e.g. age = 14."};
if(out.indexOf(v.name)<0) return {ok:false,msg:"Your output doesn't show your name yet. Print the name variable."};
if(!nums(out).some(x=>close(x,v.age))) return {ok:false,msg:"Your output doesn't show your age yet. Print the age variable."};
if(v.name==="Alex") return {ok:false,msg:"Almost! It runs, but change \\"Alex\\" to your own name."};
return {ok:true,msg:"Nice to meet you, "+v.name+"! You stored information in variables and printed it in a sentence."};''',
 solution='name = "Priya"\nage = 15\nprint "Hello, my name is", name\nprint "I am", age, "years old"\n',
 wrong='name = "Priya"\nage = 15\nprint "Hello, my name is"\n')

add(id="l1-math-operations", lesson=1, trinket=["e738f8cfc739"], title="Try it: Basic Math Operations",
 instr='Create two variables with numbers and perform each math operation on them (<code>+ - * / **</code>). Print the results with labels, e.g. <code>"Addition:", a + b</code>.',
 starter='''# Create two variables
a = 10
b = 5

print "Addition:", a + b
# Add lines for subtraction, multiplication, division and powers

''',
 check='''if(typeof v.a!=="number"||typeof v.b!=="number") return {ok:false,msg:"Keep two number variables called a and b."};
if(v.b===0) return {ok:false,msg:"b is 0 - you can't divide by zero! Pick another number."};
const a=v.a,b=v.b, n=nums(out);
const div=(Number.isInteger(a)&&Number.isInteger(b))?Math.floor(a/b):a/b;
const exp=[["Addition (+)",a+b],["Subtraction (-)",a-b],["Multiplication (*)",a*b],["Division (/)",div],["Powers (**)",Math.pow(a,b)]];
const missing=exp.filter(e=>!n.some(x=>close(x,e[1]))).map(e=>e[0]);
if(missing.length) return {ok:false,msg:"Good start! Still missing a printed result for: "+missing.join(", ")+"."};
return {ok:true,msg:"Excellent! All five operations work. Try changing a and b and run it again."};''',
 solution='a = 10\nb = 5\nprint "Addition:", a + b\nprint "Subtraction:", a - b\nprint "Multiplication:", a * b\nprint "Division:", a / b\nprint "Powers:", a**b\n',
 wrong='a = 10\nb = 5\nprint "Addition:", a + b\nprint "Subtraction:", a - b\n')

add(id="l1-practice-rectangle-area", lesson=1, trinket=["06f822ffc177"], title="Practice Q2: Area of a Rectangle",
 instr="Create a small program that calculates the area of a rectangle. Use variables for the length and width, and print the area.",
 starter='''# Area of a rectangle
# 1. Create variables for the length and width

# 2. Calculate the area

# 3. Print the area

''',
 check='''const k=Object.keys(v).filter(x=>typeof v[x]==="number");
if(k.length<2) return {ok:false,msg:"Create variables for the length and the width first, e.g. length = 8"};
if(!out.trim()) return {ok:false,msg:"Your program needs a print line to show the area."};
const n=nums(out);
for(const p of k) for(const q of k) if(p<q || (p!==q && p>q)) { if(p!==q && n.some(x=>close(x,v[p]*v[q])) && Object.values(v).some(y=>close(y,v[p]*v[q])) ) return {ok:true,msg:"Correct! "+v[p]+" x "+v[q]+" = "+(v[p]*v[q])+". Change the length and width to test another rectangle."}; }
return {ok:false,msg:"Not quite. Store length x width in an area variable (use * to multiply) and print it."};''',
 solution='length = 8\nwidth = 5\narea = length * width\nprint "The area is", area\n',
 wrong='length = 8\nwidth = 5\narea = 2 * length + 2 * width\nprint "The area is", area\n')

add(id="l2-hall-cost", lesson=2, trinket=["52610b6dd5aa"], title="Hall Rental Cost: C = 10n + 500",
 instr='Run the code. What do you notice? Then add the print line from Step 2 and try other values of <code>n</code>.',
 starter='''# number of students attending
n = 10

# cost of renting the hall, in dollars
C = 10 * n + 500
''',
 check='''if(typeof v.n!=="number"||typeof v.C!=="number") return {ok:false,msg:"Keep the variables n and C (capital C - Python is case sensitive)."};
if(!close(v.C,10*v.n+500)) return {ok:false,msg:"Check your equation: C should be 10 * n + 500."};
if(!out.trim()) return {ok:false,msg:"The program runs but doesn't DO anything you can see. Add the print line from Step 2."};
if(!nums(out).some(x=>close(x,v.C))) return {ok:false,msg:"Print the value of C so we can see the cost."};
return {ok:true,msg:"Correct! For "+v.n+" students the hall costs $"+v.C+". Change n to try other party sizes."};''',
 solution='n = 10\nC = 10 * n + 500\nprint "For", n, "students it would cost", C, "dollars to rent the hall"\n',
 wrong='n = 10\nC = 10 + n * 500\nprint "For", n, "students it would cost", C, "dollars to rent the hall"\n')

add(id="l2-height-at-t0", lesson=2, trinket=["6350e2cea13c"], title="Height of a Ball: h = -4.9t² + 20t + 2",
 instr='Add the line <code>height = -4.9 * t ** 2 + 20 * t + 2</code> and a print statement to show the height.',
 starter='''# time in seconds
t = 0

''',
 check='''if(typeof v.t!=="number") return {ok:false,msg:"Keep the variable t for time."};
if(typeof v.height!=="number") return {ok:false,msg:"Create the variable height using the equation: height = -4.9 * t ** 2 + 20 * t + 2"};
const h=-4.9*v.t*v.t+20*v.t+2;
if(!/t\\s*\\*\\*\\s*2|t\\s*\\*\\s*t\\b/.test(code)) return {ok:false,msg:"Check the formula: t squared is written t ** 2 in Python."};
if(!close(v.height,h)) return {ok:false,msg:"Your height doesn't match the equation. Check for ** (exponent) and the signs."};
if(!nums(out).some(x=>close(x,h))) return {ok:false,msg:"Your calculation is right - now print the height so you can see it."};
return {ok:true,msg:"Correct! At t = "+v.t+" s the height is "+(+h.toFixed(4))+" m. Where does the 2 in the equation come from?"};''',
 solution='t = 0\nheight = -4.9 * t ** 2 + 20 * t + 2\nprint "At t =", t, "seconds, height =", height, "meters"\n',
 wrong='t = 0\nheight = -4.9 * t * 2 + 20 * t + 2\nprint "At t =", t, "seconds, height =", height, "meters"\n')

HEIGHTS_CHECK='''const want=[0,1,2,3,4].map(t=>-4.9*t*t+20*t+2), n=nums(out);
const miss=[0,1,2,3,4].filter((t,i)=>!n.some(x=>close(x,want[i])));
if(!out.trim()) return {ok:false,msg:"Nothing printed yet. Paste the example code from above and press Run."};
if(miss.length) return {ok:false,msg:"Missing (or incorrect) heights for t = "+miss.join(", ")+". Check the formula on each line."};
%s
return {ok:true,msg:%s};'''
add(id="l2-heights-repeated", lesson=2, trinket=["156b31160565"], title="Heights at t = 0, 1, 2, 3, 4",
 instr="Copy the Step 3 example code into the window below to observe the height at each second.",
 starter='# Paste the code from Step 3 here, then press Run\n\n',
 check=HEIGHTS_CHECK % ("", '"All five heights are correct! Notice how many times we repeated the same formula..."'),
 solution=''.join('t = %d\nheight = -4.9 * t ** 2 + 20 * t + 2\nprint "At t =", t, "seconds, height =", height, "meters"\n' % t for t in range(5)),
 wrong='t = 0\nheight = -4.9 * t ** 2 + 20 * t + 2\nprint "At t =", t, "seconds, height =", height, "meters"\n')

add(id="l2-heights-loop", lesson=2, trinket=["156b31160565"], title="Using a Loop",
 instr="Copy the Step 4 loop example into the editor below to see how a loop calculates the height at each second.",
 starter='# Paste the loop code from Step 4 here, then press Run\n\n',
 check=HEIGHTS_CHECK % ('''if(!/\\bfor\\b/.test(code)) return {ok:false,msg:"The heights are right, but this step is about using a for loop. Try the Step 4 example."};
const d=(out.match(/We're done/g)||[]).length;
if(d>1) return {ok:false,msg:"\\"We're done!\\" printed "+d+" times - make sure that print line is NOT indented, so it's outside the loop."};''',
 '"Your loop works! Two indented lines did the work of fifteen."'),
 solution='for t in [0, 1, 2, 3, 4]:\n    height = -4.9 * t ** 2 + 20 * t + 2\n    print "At t =", t, "seconds, height =", height, "meters"\nprint "We\'re done!"\n',
 wrong='for t in [0, 1, 2, 3, 4]:\n    height = -4.9 * t ** 2 + 20 * t + 2\n    print "At t =", t, "seconds, height =", height, "meters"\n    print "We\'re done!"\n')

add(id="l2-practice", lesson=2, trinket=["06f822ffc177"], title="Practice: Profit and Rectangle Programs",
 instr="Q1: alter the value of <code>n</code> to find the maximum profit. Q2: write your rectangle program (perimeter 600 mm) here - use variables named <code>width</code>, <code>length</code> and <code>area</code> so Check can test it.",
 starter='''# Question 1: profit model P = -0.1n^2 + 64n - 4340
n = 300
P = -0.1 * n ** 2 + 64 * n - 4340
print "The profit is $" + str(P)
''',
 check='''let msgs=[], ok=false;
if(typeof v.width==="number"){
  if(typeof v.length!=="number"||!close(v.length,(600-2*v.width)/2)) return {ok:false,msg:"Q2: for a perimeter of 600 mm, length = (600 - 2 * width) / 2. Check your length calculation."};
  if(typeof v.area==="number"){ if(!close(v.area,v.length*v.width)) return {ok:false,msg:"Q2: area should be length * width."}; }
  if(!nums(out).some(x=>close(x,v.length)||(typeof v.area==="number"&&close(x,v.area)))) return {ok:false,msg:"Q2: print your result so you can see it."};
  ok=true; msgs.push("Q2 correct: width "+v.width+" mm gives length "+v.length+" mm"+(typeof v.area==="number"?" and area "+v.area+" mm²":"")+"."+(typeof v.area==="number"&&close(v.area,22500)?" That's the maximum area!":""));
}
if(typeof v.n==="number"&&typeof v.P==="number"){
  const P=-0.1*v.n*v.n+64*v.n-4340;
  if(!close(v.P,P)) return {ok:false,msg:"Q1: P should be -0.1 * n ** 2 + 64 * n - 4340."};
  if(!nums(out).some(x=>close(x,P))) return {ok:false,msg:"Q1: print the profit P."};
  if(!close(P,5900)) return {ok:false,msg:(msgs.length?msgs.join(" ")+" ":"")+"Q1: profit for n = "+v.n+" is $"+(+P.toFixed(2))+". Keep changing n - can you find a bigger profit?"};
  ok=true; msgs.push(close(P,5900)?"Q1: you found the maximum profit, $5900 (n = "+v.n+")!":"Q1: profit for n = "+v.n+" is $"+(+P.toFixed(2))+". Keep changing n - can you find a bigger profit?");
}
if(!ok) return {ok:false,msg:"Use the starter variables n and P (Q1), or width, length and area (Q2), so Check can test your program."};
return {ok:true,msg:msgs.join(" ")};''',
 solution='n = 320\nP = -0.1 * n ** 2 + 64 * n - 4340\nprint "The profit is $" + str(P)\nwidth = 150\nlength = (600 - 2 * width) / 2\narea = length * width\nprint "Length:", length, "Area:", area\n',
 wrong='width = 100\nlength = 600 - width\nprint "Length:", length\n')
