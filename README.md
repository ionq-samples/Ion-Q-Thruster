# Ion-Q-Thruster
UnitaryHACK2024 Challenge to create custom optimizer/transpiler for Qiskit to Native Gates.

1. **Understand the Main Objective:**
   - The main goal is to write a custom optimizer or transpiler that outperforms Qiskit's built-in optimization for native gates.
2. **Identify Potential Blockers:**
   - Recognize that understanding the Qiskit transpiler might be challenging and necessary for this project.
   - Ensure the custom IonQ (or trapped-ion) method is better optimized than Qiskit's transmon-qubit optimizer, using all-to-all connectivity.
3. **Break Down the Project:**
   - Consider splitting the project into smaller tasks:
     - Overriding Qiskit's optimizer.
     - Performing basic matrix optimizations.
     - Implementing trapped-ion optimizations.
4. **Phrase the Issue Clearly:**
   - Describe the issue as you would for a backlog issue, focusing on engaging newcomers. Make it clear and detailed to facilitate understanding and contribution.
5. **Team Review:**
   - Have team members like Spencer, Vadim, and Jon review the issue descriptions to ensure clarity and completeness.
6. **Specific Project Recommendations:**
   - Define performance metrics: Investigate and demonstrate the performance of the optimizer across a range of common algorithms (e.g., AQ benchmarking suite).
   - The optimizer should aim to use the most efficient circuits (e.g., prefer ZZ gates over MS gates if they are easier to implement).
   - Focus initially on Qiskit, with potential for future porting to Pennylane and Cirq.
