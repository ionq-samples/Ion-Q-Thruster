from qiskit import transpile
from qiskit.transpiler import PassManager, PassManagerConfig
from qiskit.transpiler.preset_passmanagers.plugin import PassManagerStagePlugin
from rewrite_rules import GPI2_Adjoint, GPI_Adjoint, CommuteGPI2MS, CancelFourGPI2
from qiskit.converters import circuit_to_dag
    
class IonQ_Transpiler:
    def __init__(self, backend):
        self.backend = backend
        self.pass_manager = self.custom_pass_manager()

    @staticmethod
    def custom_pass_manager(): # custom pass manager for optimization 
        pm = PassManager()
        pm.append([
            GPI2_Adjoint(), 
            GPI_Adjoint(),
            CommuteGPI2MS(), 
            CancelFourGPI2()
        ])
        return pm

    def transpile(self, qc):  
        
        ibm_transpiled = transpile(qc, backend=self.backend, optimization_level=3) # TODO: Replace with the custom transpiler 
        optimized_circuit = self.pass_manager.run(ibm_transpiled)

        # Run the pass manager until no further optimizations are possible
        while True:
            previous_dag = circuit_to_dag(optimized_circuit)
            optimized_circuit = self.pass_manager.run(optimized_circuit)
            if circuit_to_dag(optimized_circuit) == previous_dag:
                break
        
        return optimized_circuit
        