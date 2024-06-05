# Ion(Q) Thruster

## UnitaryHACK2024 Challenge

Welcome to the Ion(Q) Thruster project, a UnitaryHACK2024 challenge! The goal is to create a custom optimizer/transpiler in Qiskit for IonQ's trapped-ion quantum computers, and outperforms Qiskit's built-in optimization for native gates.

### Main Objective

Develop a custom optimizer or transpiler that efficiently optimizes quantum circuits for IonQ's native gates. This optimizer should achieve better performance metrics, such as reduced gate count and circuit depth, compared to Qiskit's default optimizer.

### Potential Blockers

- Understanding the intricacies of Qiskit's transpiler and optimization passes.
- Implementing and testing optimizations specific to trapped-ion systems.

### Project Breakdown

To manage this project effectively, we recommend splitting it into smaller, manageable tasks:

1. **Overriding Qiskit's Optimizer**: Create a custom pass manager that integrates with Qiskit's transpiler framework.
2. **Basic Matrix Optimizations**: Implement fundamental optimizations that improve the efficiency of quantum circuits.
3. **Trapped-Ion Optimizations**: Add specific optimizations that leverage the unique capabilities of trapped-ion hardware, such as all-to-all connectivity.

### Issues Description

#### Issue 1: Create Custom Optimizer for Qiskit-IonQ

Implement a custom optimizer for Qiskit to work with IonQ's backend. This task involves creating a new pass manager that integrates with Qiskit's transpiler framework and overrides the default optimization passes to apply custom optimizations for IonQ circuits.

#### Issue 2: Add Trapped-Ion-Specific Optimizations to Custom Optimizer

Enhance the custom optimizer with specific optimizations for trapped-ion systems. This includes eliminating unnecessary gates, combining gates, and optimizing for IonQ's unique gate capabilities.

#### Issue 3: Demonstrate Outperformance Against the Default Optimizer

Benchmark the custom optimizer against Qiskit's default optimizer using random circuits. Measure and compare performance metrics such as gate count and circuit depth reduction.

### Specific Recommendations

- **Performance Metrics**: Define and use performance metrics to evaluate the optimizer. Consider common algorithms and benchmarks.
- **Efficient Circuits**: Focus on creating the most efficient circuits, preferring gates that are easier to implement on IonQ hardware.

### Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ionq-samples/Ion-Q-Thruster.git
   cd ion-q-thruster
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Demo Notebook**:
   Open `main.ipynb` in Jupyter Notebook and follow the steps to begin writing and testing your custom optimizer.

### Team Review

Ensure that PR descriptions and documentation are reviewed by team members for clarity and completeness.

### Future Work

While this project focuses on Qiskit, the custom optimizer can be potentially ported to other frameworks like Pennylane and Cirq.

### Contact

For any questions or issues, please open an issue on GitHub or contact us on Discord.
