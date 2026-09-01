<div align="center">

✨ Pattern Generator & Number Analyzer

🐍 P-2 — Logic Box

<p>
  <strong>A menu-driven Python console application combining pattern printing and number analysis.</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Logic-Patterns-6F42C1?style=for-the-badge" alt="Patterns">
  <img src="https://img.shields.io/badge/Level-Beginner-2EA44F?style=for-the-badge" alt="Beginner">
</p>

</div>

🚀 Project Overview

Pattern Generator & Number Analyzer is a menu-driven Python program designed to practice programming logic through two main features:

① Generate a Pattern
Create different star patterns by selecting a pattern and entering the required number of rows.

② Analyze a Range of Numbers
Analyze numbers between a selected start and end value, identify each number as Even or Odd, and calculate their total sum.

The program uses a continuous menu so users can perform multiple operations before choosing Exit.

🎯 Learning Objectives

<div align="center">

<table width="100%">
<thead>
<tr>
<th align="center">#</th>
<th align="left">Concept</th>
<th align="left">What You Practice</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">1</td>
<td><code>while</code> loop</td>
<td>Build a continuous menu-driven program</td>
</tr>
<tr>
<td align="center">2</td>
<td><code>match case</code></td>
<td>Handle multiple menu choices</td>
</tr>
<tr>
<td align="center">3</td>
<td><code>for</code> loop</td>
<td>Generate patterns and process number ranges</td>
</tr>
<tr>
<td align="center">4</td>
<td>Nested loops</td>
<td>Build rows, spaces, and star patterns</td>
</tr>
<tr>
<td align="center">5</td>
<td><code>if / else</code></td>
<td>Make logical decisions</td>
</tr>
<tr>
<td align="center">6</td>
<td>Modulo <code>%</code></td>
<td>Determine whether a number is Even or Odd</td>
</tr>
<tr>
<td align="center">7</td>
<td><code>range()</code></td>
<td>Work with rows and number ranges</td>
</tr>
<tr>
<td align="center">8</td>
<td>Input & Conversion</td>
<td>Accept and convert user input using <code>int()</code></td>
</tr>
</tbody>
</table>

</div>

🎛️ Control Center

<div align="center">

<table width="100%">
<tr>
<td align="center" width="33%">

01 ⭐

Generate a Pattern

Create and explore different star patterns.

</td>
<td align="center" width="33%">

02 🔢

Analyze Numbers

Check Even/Odd values and calculate their sum.

</td>
<td align="center" width="33%">

03 🚪

Exit

Safely finish the program.

</td>
</tr>
</table>

</div>

The application continuously displays the main menu, allowing the user to choose a feature and return to the menu after completing an operation.

⭐ Pattern Studio

<div align="center">

Choose a pattern → Enter the size → Watch the logic build it

</div>

The Pattern Studio contains seven different star-pattern challenges, plus an option to return to the Control Center.

🎨 Pattern Library

<div align="center">

<table width="100%">
<tr>
<td align="center" width="50%">

01 🔺

Right Triangle

Builds an increasing triangle using nested loops.

</td>
<td align="center" width="50%">

02 🔻

Inverted Right Triangle

Builds a decreasing triangle row by row.

</td>
</tr>

<tr>
<td align="center" width="50%">

03 🔺

Pyramid

Uses spaces and stars to create a centered pyramid.

</td>
<td align="center" width="50%">

04 🔻

Inverted Pyramid

Reverses the pyramid from the widest row to the smallest.

</td>
</tr>

<tr>
<td align="center" width="50%">

05 💎

Diamond Pattern

Combines an increasing and decreasing pyramid.

</td>
<td align="center" width="50%">

06 ⬜

Hollow Square

Prints stars around the border while leaving the center empty.

</td>
</tr>

<tr>
<td align="center" width="50%">

07 🦋

Butterfly Pattern

Creates a mirrored butterfly using two pattern sections.

</td>
<td align="center" width="50%">

00 ↩️

Back to Control Center

Returns to the main menu.

</td>
</tr>
</table>

</div>



🧪 Pattern Showcase

<div align="center">

<table width="100%">
<tr>
<td width="50%" valign="top">

🔺 01 · Right Triangle

Input: 3 rows

<pre>
*
* *
* * *
</pre>

Increasing number of stars on each row.

</td>
<td width="50%" valign="top">

🔻 02 · Inverted Right Triangle

Input: 3 rows

<pre>
* * *
* *
*
</pre>

Decreasing number of stars on each row.

</td>
</tr>

<tr>
<td width="50%" valign="top">

🔺 03 · Pyramid

Input: 3 rows

<pre>
  *
 ***
*****
</pre>

Uses spaces and stars to create a centered shape.

</td>
<td width="50%" valign="top">

🔻 04 · Inverted Pyramid

Input: 3 rows

<pre>
*****
 ***
  *
</pre>

Starts wide and decreases toward the bottom.

</td>
</tr>

<tr>
<td width="50%" valign="top">

💎 05 · Diamond Pattern

Input: 3 rows

<pre>
  *
 ***
*****
 ***
  *
</pre>

Combines an increasing pyramid with a decreasing pyramid.

</td>
<td width="50%" valign="top">

⬜ 06 · Hollow Square

Input: 3 × 3

<pre>
* * *
*   *
* * *
</pre>

Prints stars only on the outer border.

</td>
</tr>

<tr>
<td width="50%" valign="top">

🦋 07 · Butterfly Pattern

Input: 3 rows

<pre>
*    *
**  **
******
**  **
*    *
</pre>

Builds a mirrored butterfly using two sections.

</td>
<td width="50%" valign="top">

↩️ 00 · Back

<pre>
0. Back to Main Menu
</pre>

Returns from the Pattern Studio to the main menu.

</td>
</tr>
</table>

</div>

🧠 Pattern Logic

Each pattern is generated using for loops, nested loops, spaces, and star calculations. The program uses match case to select the requested pattern.

🔢 Number Analyzer

Selecting Option 2 asks the user for:

Start of the range
End of the range

The program then checks every number in the range and identifies it as Even or Odd. It also calculates the sum of all numbers in that range.

Example · Range 1 → 10

<pre>
1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd
6 is Even
7 is Odd
8 is Even
9 is Odd
10 is Even

Sum of numbers from 1 to 10 = 55
</pre>

🛡️ Input Validation

The program handles invalid menu choices instead of immediately terminating.

For the Pattern Menu:

Invalid choice! Please try again.

For the Main Menu:

Invalid choice! Please select between 1 and 3.

It also checks whether the start of a number range is greater than the end and displays an invalid-range message when necessary.

📸 Project Outputs

<div align="center">

🖼️ Pattern & Number Analysis Screenshots

</div>

<table width="100%">
<tr>
<td width="50%" align="center">

🔺 Pattern Output

<a href="assets/Output-1.png">
<img src="assets/Output-1.png" alt="Pattern Generator Output" width="100%">
</a>

🔍 Open Full Image

</td>
<td width="50%" align="center">

🔻 Pattern Output

<a href="assets/Output- 2.png">
<img src="assets/Output-%202.png" alt="Pattern Generator Output" width="100%">
</a>

🔍 Open Full Image

</td>
</tr>

<tr>
<td width="50%" align="center">

💎 Pattern Output

<a href="assets/Output- 3.png">
<img src="assets/Output-%203.png" alt="Pattern Generator Output" width="100%">
</a>

🔍 Open Full Image

</td>
<td width="50%" align="center">

🔢 Number Analysis

<a href="assets/Output- 4.png">
<img src="assets/Output-%204.png" alt="Number Analysis Output" width="100%">
</a>

🔍 Open Full Image

</td>
</tr>
</table>

🎥 Project Demonstration

<div align="center">

▶️ Watch the Complete Program Demonstration

<a href="assets/Project%20Demonstration%284%29.mp4">

<strong>▶️ OPEN PROJECT DEMONSTRATION VIDEO</strong>

</a>

<br><br>

<p>Demonstrates pattern generation, number analysis, invalid input handling, and returning/exiting through the menus.</p>

</div>

💡 GitHub Note: If GitHub does not preview the MP4 directly, click the video link above to open the demonstration file.

🔄 Program Flow

<div align="center">

              🐍 START
                  │
                  ▼
          ┌────────────────┐
          │   MAIN MENU    │
          └───────┬────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
       [1]       [2]       [3]
        │         │         │
        ▼         ▼         ▼
   ⭐ PATTERN   🔢 RANGE   🚪 EXIT
      MENU      ANALYSIS
        │         │
        ▼         ▼
   Choose      Start + End
   Pattern       Range
        │         │
        ▼         ▼
   Print ⭐    Even / Odd
        │         │
        │         ▼
        │       Sum
        │         │
        └────┬────┘
             ▼
        🔁 MAIN MENU

</div>

📁 Project Resources

<div align="center">

<table width="100%">
<thead>
<tr>
<th align="left">📄 Resource</th>
<th align="left">🎯 Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>main.py</code></td>
<td>Main Python source code</td>
</tr>
<tr>
<td><code>README.md</code></td>
<td>Project documentation</td>
</tr>
<tr>
<td><code>assets/Output-1.png</code></td>
<td>Pattern generator output screenshot</td>
</tr>
<tr>
<td><code>assets/Output- 2.png</code></td>
<td>Pattern generator output screenshot</td>
</tr>
<tr>
<td><code>assets/Output- 3.png</code></td>
<td>Pattern generator output screenshot</td>
</tr>
<tr>
<td><code>assets/Output- 4.png</code></td>
<td>Number analysis output screenshot</td>
</tr>
<tr>
<td><code>assets/Project Demonstration(4).mp4</code></td>
<td>Complete project demonstration video</td>
</tr>
</tbody>
</table>

</div>

🚀 How To Run

1️⃣ Open the project

Open main.py in:

IDLE

VS Code

PyCharm

Any Python-supported editor

2️⃣ Run the program

python main.py

3️⃣ Select an option

1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

📦 Dependencies

No external Python packages are required.

🧠 Skills Demonstrated

<div align="center">

while loops • for loops • nested loops • match case • if/else • range() • input() • int() • % • pattern logic

</div>

🏁 Final Takeaway

Think → Build Logic → Test → Analyze → Improve

This project turns basic Python syntax into practical programming logic through pattern generation and number analysis.

<div align="center">

⭐ Explore the code. Run the program. Learn the logic.

<br>

Made with 🐍 Python

</div>