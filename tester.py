import os
from qiskit.converters import circuit_to_dag
from qiskit import transpile
from qiskit_ionq import IonQProvider
from custom_transpiler import IonQ_Transpiler
from qiskit.circuit.random import random_circuit


def compare_circuits(original_circuit, optimized_circuit):
    original_dag = circuit_to_dag(original_circuit)
    optimized_dag = circuit_to_dag(optimized_circuit)

    original_metrics = {
        'depth': original_dag.depth(),
        'size': original_dag.size(),
        'gpi2_count': original_dag.count_ops().get('gpi2', 0),
        'gpi_count': original_dag.count_ops().get('gpi', 0),
        'ms_count': original_dag.count_ops().get('ms', 0),
        'zz_count': original_dag.count_ops().get('zz', 0)
    }

    optimized_metrics = {
        'depth': optimized_dag.depth(),
        'size': optimized_dag.size(),
        'gpi2_count': optimized_dag.count_ops().get('gpi2', 0),
        'gpi_count': optimized_dag.count_ops().get('gpi', 0),
        'ms_count': optimized_dag.count_ops().get('ms', 0),
        'zz_count': optimized_dag.count_ops().get('zz', 0)
    }

    print(f"The circuit size has reduced from {original_metrics.get('size')} to {optimized_metrics.get('size')}")
    
    return original_metrics, optimized_metrics

def print_metrics(metrics):
    print(f"- Depth: {metrics['depth']}")
    print(f"- Size: {metrics['size']}")
    print(f"- GPI2 Count: {metrics['gpi2_count']}")
    print(f"- GPI Count: {metrics['gpi_count']}")
    print(f"- MS Count: {metrics['ms_count']}")
    print(f"- ZZ Count: {metrics['zz_count']}")
    

def run_test_case(qc, backend):
    
    original_circuit = transpile(qc, backend=backend, optimization_level=3)
    #print("IBM transpiled circuit:")
    #print(original_circuit.draw())

    custom_transpiler = IonQ_Transpiler(backend)
    optimized_circuit = custom_transpiler.transpile(qc)
    #print("\nCustom transpiled circuit:")
    #print(optimized_circuit.draw())

    original_metrics, optimized_metrics = compare_circuits(original_circuit, optimized_circuit)
    print("\nIBM transpiled circuit metrics:")
    print_metrics(original_metrics)
    
    print("\nCustom transpiled circuit metrics:")
    print_metrics(optimized_metrics)


# Initialize the IonQ provider and backend
api_key = os.getenv("IONQ_API_KEY") or input("Enter your IonQ API key: ")
provider = IonQProvider(token=api_key)
backend = provider.get_backend("simulator", gateset="native")

# Generate random circuits
num_qubits = 5
depth = 10
num_circuits = 5

random_circuits = [random_circuit(num_qubits, depth, measure=True) for _ in range(num_circuits)]

# Run test cases
for i, qc in enumerate(random_circuits):
    print(f"\nTest Case {i+1}:")
    run_test_case(qc, backend)