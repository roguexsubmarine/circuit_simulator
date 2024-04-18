
# Circuit Simulator

A graphical user interface (GUI) built using PyQt6 for a circuit simulator. While the GUI is written in Python, the computational heavy lifting is handled by C programming. This project is a precursor to a larger circuit analyzer project.

In this repository, you'll find the GUI component that allows users to input complex resistive circuits. The system then generates essential matrices—adjacency, resistive, and voltage—for further analysis. With 'Circuit Simulator', understanding and analyzing circuits becomes more accessible, making it a valuable tool for engineers and enthusiasts alike.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)  
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)



## Run Locally

Clone the project

```bash
  git clone https://github.com/roguexsubmarine/circuit_simulator.git
```

Go to the project directory

```bash
  cd cd circuit_simulator/
```

Install Modules

```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  deactivate
```

Make executable

```bash
  chmod +x run.sh
```

Start Program

```bash
  ./run.sh
```

