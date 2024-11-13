<h1>Python Vehicle Diagnostic Tool</h1> <h3>Description</h3> <p><strong>Vehicle Diagnostic Tool</strong> is a Python-based script that simulates an automotive diagnostics system. It randomly generates diagnostic trouble codes (DTCs) to simulate the experience of running a real diagnostic check on a vehicle. This project helps understand how Python can be applied in automotive diagnostics, focusing on functions, dictionaries, and random selection.</p> <h3>Prerequisites</h3> <p>To run this project, make sure you have Python installed on your system.</p> <ul> <li><strong>Install Python</strong>: Download and install the latest version of Python from <a href="https://www.python.org/downloads/">Python.org</a>.</li> </ul> <h3>Installation</h3> <ol> <li><strong>Step 1: Clone the Repository</strong> <ul> <li>Clone the repository to your local machine:</li> <pre><code>git clone https://github.com/kelvintechnical/Vechicle-Diagnostic-Tool.git</code></pre> <li>Navigate into the project directory:</li> <pre><code>cd Vehicle_Diagnostic_Tool</code></pre> </ul> </li> <li><strong>Step 2: Run the Program</strong> <ul> <li>Start the program by running:</li> <pre><code>python diagnostic_tool.py</code></pre> </ul> </li> </ol> <h3>Features</h3> <ul> <li><strong>Simulates Diagnostic Trouble Codes</strong>: Randomly generates diagnostic trouble codes for practice.</li> <li><strong>Realistic Timing</strong>: Uses time delays to simulate actual scanning.</li> <li><strong>Educational Tool</strong>: Learn the basics of Python functions, dictionaries, and random selection.</li> </ul> <h3>Code Overview</h3> <h4>Imports</h4> <p>This program uses two main imports:</p>
python
Copy code
import time
import random
<code>time</code>: Creates delays to mimic the real-time scanning process.
<code>random</code>: Randomly selects error codes from the list to simulate a diagnostic scan.
<h4>Diagnostic Trouble Codes (DTCs)</h4> <p>We define a dictionary with sample DTCs:</p>
python
Copy code
dtc_codes = {
    "P0010": "Camshaft Position Actuator Circuit",
    "P0102": "Mass Air Flow Circuit Low",
    "P0128": "Coolant Thermostat Malfunction",
    "P0300": "Random/Multiple Cylinder Misfire",
}
<h4>Function: <code>run_diagnostics</code></h4> <p>The main function <code>run_diagnostics</code> simulates a vehicle diagnostics process:</p>
python
Copy code
def run_diagnostics():
    print("Starting vehicle diagnostics..")
    time.sleep(2)
    print("Scanning for error codes..")
    time.sleep(5)
    error_found = random.sample(list(dtc_codes.keys()), 2)
    print("Error codes found")
    for code in error_found:
        print(f'{code}: {dtc_codes[code]}')
    print("Diagnostics complete.")
<h4>Explanation:</h4> <ul> <li><strong>Starting the Diagnostics</strong>: The initial <code>print()</code> statement and a <code>time.sleep(2)</code> delay create a starting message and short pause.</li> <li><strong>Scanning for Error Codes</strong>: Simulates scanning for errors with another <code>print()</code> message and a <code>time.sleep(5)</code> pause.</li> <li><strong>Error Codes Found</strong>: Uses <code>random.sample()</code> to select two random error codes from <code>dtc_codes</code>.</li> <li><strong>Display Results</strong>: Prints each selected code with its description.</li> </ul> <h3>Usage</h3> <p>Run the program to simulate a vehicle diagnostics scan:</p> <pre><code>python diagnostic_tool.py</code></pre>
Example output:

vbnet
Copy code
Starting vehicle diagnostics..
Scanning for error codes..
Error codes found
P0010: Camshaft Position Actuator Circuit
P0300: Random/Multiple Cylinder Misfire
Diagnostics complete.
<h3>What I Learned</h3> <ul> <li><strong>Using Libraries</strong>: Leveraged <code>time</code> and <code>random</code> for simulation and randomness.</li> <li><strong>Dictionaries for Data Storage</strong>: Stored DTC codes and descriptions in a dictionary.</li> <li><strong>Modular Code with Functions</strong>: Structured code within functions for organization and reusability.</li> </ul> <h3>Support & Feedback</h3> <p>If you found this project helpful, please consider leaving feedback to support my growth as a developer. Suggestions are always welcome!</p> <p><a href="https://www.instagram.com/kelvinintech" target="_blank" style="text-decoration: none;"> <button style="background-color: #E4405F; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;"> Follow Me on Instagram </button> </a></p> <p><a href="https://x.com/kelvintechnical" target="_blank" style="text-decoration: none;"> <button style="background-color: #1DA1F2; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;"> Follow Me on Twitter </button> </a></p>
