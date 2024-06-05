import hashlib
from qiskit import transpile
from qiskit.transpiler import PassManager
from rewrite_rules import GPI2_Adjoint, GPI_Adjoint, CommuteGPI2MS, CancelFourGPI2
from qiskit.converters import circuit_to_dag, dag_to_circuit

class IonQ_Transpiler:
    def __init__(self, backend):
        self.backend = backend
        self.pass_manager = self.custom_pass_manager()

    @staticmethod
    def custom_pass_manager():
        pm = PassManager()
        pm.append([
            GPI2_Adjoint(), 
            GPI_Adjoint(),
            CommuteGPI2MS(), 
            CancelFourGPI2()
        ])
        return pm

    def transpile(self, qc):  
        
        ibm_transpiled = transpile(qc, backend=self.backend, optimization_level=3)
        optimized_circuit = ibm_transpiled

        while True:
            previous_dag = circuit_to_dag(optimized_circuit)
            optimized_circuit = self.pass_manager.run(optimized_circuit)
            if circuit_to_dag(optimized_circuit) == previous_dag:
                break

        return optimized_circuit
        